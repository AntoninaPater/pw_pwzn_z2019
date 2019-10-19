import collections

from task_1 import parse_input


def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    pairs = parse_input(input)
    zbior = collections.deque()
    results = []

    for pair in pairs:

        if pair[0] == 1:
            zbior.append(zbior.count(pair[1]))
        if pair[0] == 2:
            if zbior.count(pair[1]) != 0:
                zbior.remove(pair[1])
        if pair[0] ==3:
            results.append(zbior.count(pair[1]))

    return(results)




_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 2


"""
if __name__ == '__main__':
    assert check_frequency(_input) == [0, 0]