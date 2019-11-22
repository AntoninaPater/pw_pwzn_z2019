"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
import itertools
from collections import namedtuple
from pathlib import Path
import csv


def select_animals(input_path, output_path, compressed=False):
    with open(input_path) as _file:
        reader = csv.reader(_file, delimiter=',')

        animal_list = []
        genera = set()
        genders = ["female", "male"]
        header = next(reader)
        print(header)
        animal = namedtuple('animal', header)
        for row in reader:
            current_animal = animal(*row)
            animal_list.append(current_animal)
            genera.add(current_animal.genus)

    chosen_ones = []
    for gender, genus in (itertools.product(genders, genera)):
        selected_one = min(animal_list, key=lambda a: (a.genus == genus,
                                                            a.gender == gender,
                                                            float(a.mass.split(' ')[0])))
        chosen_ones.append(selected_one)

    chosen_ones = sorted(chosen_ones, key=lambda a: (a.genus, a.name))

    gender = {
        'female': 'F',
        'male': 'M',
    }
    unit = {
        "kg": 1.,
        "g": 10 ** -3,
        "mg": 10 ** -6,
        "Mg": 10 ** 3,
    }
    compressed_animal = namedtuple('compressed_animal', 'id gender mass')
    chosen_compressed_animals = []
    for one in chosen_ones:
        tmp_gender = gender[one.gender]
        tmp_mass, tmp_unit = one.mass.split(' ')
        tmp_mass = float(tmp_mass) * unit[tmp_unit]
        tmp_mass = '{:.3e}'.format(tmp_mass)
        current_compressed = compressed_animal(one.id, tmp_gender, tmp_mass)
        print(tmp_mass)
        chosen_compressed_animals.append(current_compressed)

    if not compressed:
        with open(output_path, 'w', newline='') as file_:
            writer = csv.writer(file_, delimiter=',')
            writer.writerow(header)
            writer.writerows(chosen_ones)
    else:
        with open(output_path, 'w', newline='') as file_:
            writer = csv.writer(file_, delimiter='_')
            writer.writerow(['uuid', 'gender', 'mass'])
            writer.writerows(chosen_compressed_animals)


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
