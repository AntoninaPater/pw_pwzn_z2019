def counting_sort(values, _max, _min=0):
    """
    Function returns sorted list.

    Sortowanie przez zliczanie to metoda polegajaca na sortowaniu wąskiego zakresu wartości
    (około 1000 kolejnych elementów) poprzez zliczenie wystąpeiń elementów w podanej liście
    i wypisania ich w kolejności.

    :param values: List of values to sort.
    :type values: List[int]
    :param _max: Maximum value in list.
    :type _max: int
    :param _min: Maximum value in list.
    :type _min: int
    :return:
    """
    pass

    hist = [0]*(_max + 1)
    sor = [0]*len(values)

    for i in range(0, len(values)):
        hist[values[i]] +=1

    m = 0
    for j in range(0, len(hist)):
        for ii in range(0,hist[j]):
            sor[m] = j
            m += 1

    return sor




if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]

