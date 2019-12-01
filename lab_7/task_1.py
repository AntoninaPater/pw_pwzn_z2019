import numpy as np


def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    B = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """
    x = xy[0]
    y = xy[1]
    n = np.size(x)
    delta = n * np.sum(x**2) - (np.sum(x)**2)

    a = (np.sum(x ** 2) * np.sum(y) - np.sum(x) * np.sum(x*y)) / delta
    b = (n * np.sum(x*y) - np.sum(x) * np.sum(y)) / delta

    return a, b


if __name__ == '__main__':
    points = np.array([[0.008631342087986165,
                        1.0008364249814004,
                        1.9971579080183022,
                        2.9900639107840363,
                        4.000909046861446,
                        5.002769296857769,
                        6.008686943782208,
                        6.995962248830773,
                        7.994773423654545,
                        9.008310085107235,
                        10.002815710423974,
                        10.990245394557476,
                        12.00991313810135,
                        13.009627154889195,
                        13.995118297258841,
                        14.99867882091641,
                        15.99836991383825,
                        17.009420324516032,
                        18.008485985011042,
                        18.99036158721762,
                        19.995958099496665,
                        21.006170536458644,
                        22.008623538373023,
                        23.00795362964936,
                        23.995463446888365,
                        25.002643988987103,
                        25.99294654737382,
                        27.000367902471776,
                        27.995646213618652,
                        28.992319110426237,
                        29.991661765578876,
                        30.993240304012545,
                        31.998173754122817,
                        33.00233249981756,
                        34.00040496883612,
                        34.9940603953775,
                        36.00942862396456,
                        36.99779307858559,
                        38.00769105875548,
                        39.00159020850988,
                        40.004017962564554,
                        41.00679758360825,
                        42.00026640855164,
                        43.007555318545585,
                        43.99171620779577,
                        44.99896008693193,
                        45.99519750165575,
                        47.00227554331028,
                        48.00385746327501,
                        49.000898697063256,
                        49.99816110566609,
                        50.99675952583969,
                        52.00049405107875,
                        53.00484390617505,
                        54.00900838890434,
                        55.00015112779759,
                        56.00746301414209,
                        57.00511168720217,
                        58.00933445695161,
                        59.00328785386704,
                        59.99318211465178,
                        60.993068891671825,
                        62.00281402476314,
                        62.99266395652095,
                        64.00617884848414,
                        65.00009147601938,
                        65.99484080451413,
                        66.9932054384621,
                        67.99304917797456,
                        69.00412826853618,
                        69.99225181895618,
                        70.99022396603338,
                        72.0027713564272,
                        73.00073393372367,
                        74.00355201532582,
                        74.99050762075615,
                        75.99595623166134,
                        77.00589413305975,
                        77.99656763932657,
                        79.00351290998272,
                        80.00428986561165,
                        81.00150462725924,
                        81.9953497816055,
                        83.00358275289975,
                        83.99759177298222,
                        85.00972852878357,
                        85.99193677479026,
                        86.9909531691068,
                        87.99635887746665,
                        88.99402187974421,
                        90.003689089595,
                        91.00978340991091,
                        92.0006778536622,
                        92.998202516714,
                        94.00918020004808,
                        94.99815882397733,
                        96.00732447964779,
                        97.00188596514707,
                        97.99983502892982,
                        98.99505105754211],
                       [1.0041819492561623,
                        2.0083104699526655,
                        2.9992071245903045,
                        3.9903304453399535,
                        4.996231196291662,
                        6.0004027455075795,
                        7.004463616775093,
                        8.00077513358009,
                        8.999836052163248,
                        9.998694205243925,
                        10.994209138118961,
                        12.002605712911445,
                        13.00459129253415,
                        14.004184900714437,
                        15.005092576274096,
                        16.003752992950112,
                        16.996228477370423,
                        17.991068196873083,
                        18.994039421616304,
                        20.006833611177097,
                        21.00901266741924,
                        22.006512774054737,
                        22.998696525260407,
                        23.996489285013084,
                        24.99566920841583,
                        25.999458400150317,
                        26.990056758353504,
                        27.997631722917472,
                        29.002213184562187,
                        30.002970424489693,
                        30.990660383516392,
                        32.000852249611206,
                        33.00168179376673,
                        33.997333259832104,
                        34.999151854613174,
                        35.99773026757014,
                        37.00410187245923,
                        37.991276803504455,
                        38.99897781720756,
                        39.999896137371366,
                        41.00029910939775,
                        42.005860719404836,
                        42.99346800479961,
                        43.99056058465498,
                        44.99347249677747,
                        46.00910317170997,
                        47.00306203316635,
                        47.99029922792029,
                        48.99005089972553,
                        50.00590885696303,
                        51.004013700614685,
                        51.992445889973496,
                        52.9938913506482,
                        53.99454134028345,
                        54.997886006717685,
                        56.005111076034225,
                        56.993029849837086,
                        58.000421467001516,
                        59.0095432171949,
                        59.99714224154552,
                        60.99327398391099,
                        61.99291518133234,
                        62.99880438387105,
                        63.99641138826015,
                        65.00389847744971,
                        66.00767560729928,
                        66.99900083007907,
                        67.99637839562797,
                        69.00200259613548,
                        70.00623947042943,
                        71.00321889082004,
                        71.99990410612128,
                        73.00654998641905,
                        73.99834183653309,
                        75.00495068953678,
                        76.00424244325083,
                        77.00387712062289,
                        78.00852591380952,
                        79.00820632347255,
                        79.99623029866326,
                        80.99695657037462,
                        82.00244553920412,
                        83.00175816147664,
                        83.99574403395968,
                        85.00087841354915,
                        85.99180879104642,
                        87.00574621477143,
                        87.99184700211774,
                        89.00784726008939,
                        90.0056073021343,
                        91.0078300893724,
                        92.00315248978815,
                        92.9948346568788,
                        94.00874695163739,
                        95.00633301444206,
                        95.99864239366661,
                        96.99273933054107,
                        98.00343145869182,
                        98.9982680433363,
                        100.00083927400149]])
    np.testing.assert_allclose(least_sq(points), (1, 1), atol=0.1)
