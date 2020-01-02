import csv
import os
import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin

import requests

API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    _path = pathlib.Path.cwd()
    if isinstance(path, pathlib.PosixPath):
        result_path = path
    elif isinstance(path, str):
        result_path = pathlib.PosixPath(path) / f'{woeid}_{year}_{month:02}'
    elif path is None:
        result_path = _path / f'{woeid}_{year}_{month:02}'
    if not os.path.exists(os.path.dirname(str(result_path) + "/")):
        os.makedirs(os.path.dirname(str(result_path) + "/"))

    session = requests.session()
    saved_files = []
    for day in range(1, 32):
        location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
        try:
            response = session.get(location_url, timeout=timeout)
        except requests.exceptions.Timeout as e:
            print('timeout error', e)
            raise requests.exceptions.Timeout
        else:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('communication error',e)
            try:
                resp_json = response.json()
            except RuntimeError as e:
                print('parsing error', e)

        if resp_json:
            with open(result_path / f'{year}_{month:02}_{day:02}.csv', mode='w+') as _file:
                writer = csv.writer(_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                row1 = True
                for row in response.json():
                    if row1:
                        row1 = False
                        writer.writerow(row.keys())
                    writer.writerow(row.values())
                saved_files.append(result_path / str(day))
    return str(result_path), saved_files


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
