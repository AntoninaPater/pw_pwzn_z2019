def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    pass

    unq = []

    msgsplt = list(msg)

    for i in msgsplt:
        if (i in unq) == 0:
            unq.append(i)
    unq = sorted(unq)
    num = [0] * len(unq)

    for j in range(0,len(msgsplt)):
        for k in range(0,len(unq)):
            if msgsplt[j] == unq[k]:
                num[k] =  num[k] + 1

    return(unq[num.index(max(num))],max(num))


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)