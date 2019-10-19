"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do naj+starszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""
from datetime import datetime
import pytz


def sort_dates(date_str, date_format=''):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """


def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """

    curr_date = dates[0].strftime("%Y-%m-%d")
    out_str = curr_date

    for elem in dates:


        if elem.strftime("%Y-%m-%d") != curr_date:
            curr_date = elem.strftime("%Y-%m-%d")
            out_str = out_str + "\n" + "    ----" + "\n    " + curr_date
        out_str = out_str + "\n" + "    \t" + elem.strftime("%H:%M:%S")
    print(out_str)
    return out_str

def format_day(day, events):
    """
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """
    pass


def date_in_utc(date):
    date = date.strip()
    date_dt = datetime.strptime(date, "%a %d %b %Y %H:%M:%S %z")
    date_utc = date_dt.astimezone(pytz.timezone('UTC'))
    return date_utc


def parse_dates(date_str, date_format=''):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """

    date_str = date_str.strip()
    date_list = date_str.split('\n')
    date_in_dt_format = list(map(date_in_utc, date_list))
    date_in_dt_format.sort(reverse=True)

    dates_grouped = group_dates(date_in_dt_format)

    return dates_grouped






if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """

    # assert sort_dates(dates) == [
    #     datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    # ]

    assert parse_dates(dates) == """2015-05-10
    \t20:54:36
    \t13:54:36
    ----
    2015-05-02
    \t14:24:36
    ----
    2015-05-01
    \t13:54:36"""