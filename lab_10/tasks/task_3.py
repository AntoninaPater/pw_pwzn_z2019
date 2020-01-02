import filecmp
import pathlib
from os import listdir
from os.path import isfile, join
from typing import Union
import pandas as pd

API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path], ):
    files = [file for file in listdir(path) if isfile(join(path, file))]
    data = pd.DataFrame(columns=['created', 'min_temp', 'temp', 'max_temp',
                                 'air_pressure', 'humidity', 'visibility',
                                 'wind_direction_compass', 'wind_direction',
                                 'wind_speed'])
    for file in files:
        day = int(file.split('_')[2].split('.')[0])
        data_tmp = pd.read_csv(pathlib.Path(path) / file, sep= " ")
        data_tmp = data_tmp[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure',
                             'humidity', 'visibility', 'wind_direction_compass',
                             'wind_direction', 'wind_speed']]
        data_tmp.rename(columns={'the_temp': 'temp'}, inplace=True)
        data_tmp.created = pd.to_datetime(data_tmp.created)
        data_tmp = data_tmp[data_tmp.created.dt.day == day]
        data = data.append(data_tmp)
    data.sort_values(['created'], inplace=True)
    data.created = data.created.dt.strftime('%Y-%m-%dT%H:%M')
    data.to_csv(str(path) + '.csv', index=False)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
