"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re


def match_msg(pattern, msg):
    return bool(re.fullmatch(pattern, msg))


def check_animal_list(file_path):
    with open(file_path) as _file:
        rows = _file.readlines()

    f_count = 0
    m_count = 0
    f_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_F_[\d]\.[\d]{3}e[\-\+][\d]{2}$'
    m_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_M_[\d]\.[\d]{3}e[\-\+][\d]{2}$'

    for row in rows:
        row = row.strip()
        f_count += match_msg(f_pattern, row)
        m_count += match_msg(m_pattern, row)
    return f_count, m_count


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
