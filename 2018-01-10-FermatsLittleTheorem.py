from random import randint


def fermat_little(string):
    n, c = string.split(" ")
    number, certainty = int(n), float(c)

    count = 0
    while 1 - pow(2, -count) < certainty:
        a = randint(1, number - 1)
        if pow(a, number, number) != a:
            print(False)
            return

        count += 1

    print(True)


fermat_little("29497513910652490397 0.9")
# True

fermat_little("29497513910652490399 0.9")
# True

fermat_little("95647806479275528135733781266203904794419584591201 0.99")
# False

fermat_little("95647806479275528135733781266203904794419563064407 0.99")
# True

fermat_little(
    "2367495770217142995264827948666809233066409497699870112003149352380375124855230064891220101264893169 0.999")
# False

fermat_little(
    "2367495770217142995264827948666809233066409497699870112003149352380375124855230068487109373226251983 0.999")
# True
