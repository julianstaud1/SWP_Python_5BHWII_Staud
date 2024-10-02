import random


def lotto():
    zahlen = list(range(1, 46))
    ziehung = random.sample(zahlen, 6)
    return sorted(ziehung)


def lotto_statistik():
    s = {i: 0 for i in range(1, 46)}

    for _ in range(1000):
        ziehung = lotto()
        for zahl in ziehung:
            s[zahl] += 1

    return s


if __name__ == "__main__":

    print("ziehung:", lotto())

    st = lotto_statistik()

    print("\nstatistik nach 1000 ziehungen:")
    for zahl, oft in sorted(st.items()):
        print(f"{zahl}: {oft} mal gezogen")