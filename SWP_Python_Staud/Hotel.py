#klasse zimmer(preis, einzel oder doppelzimmer, besetzt)
#hotel hat sammlung von zimmern, zimmer kann man buchen und stornieren methoden
#anzahl der freien zimmer methode
#simulation im hauptprogramm (main)
class Zimmer:
    def __init__(self, nummer, preis, typ):
        self.nummer = nummer
        self.preis = preis
        self.typ = typ
        self.besetzt = False

    def buchen(self):
        if not self.besetzt:
            self.besetzt = True
            print(f"Zimmer {self.nummer} wurde gebucht")
        else:
            print(f"Zimmer {self.nummer} ist bereits besetzt")

    def stornieren(self):
        if self.besetzt:
            self.besetzt = False
            print(f"Zimmer {self.nummer} wurde storniert")
        else:
            print(f"Zimmer {self.nummer} ist gar nicht gebucht")


class Hotel:
    def __init__(self):
        self.zimmer = []

    def zimmer_dazu(self, zimmer):
        self.zimmer.append(zimmer)

    def zimmer_frei(self):
        return sum(1 for zimmer in self.zimmer if not zimmer.besetzt)

    def zimmer_zeigen(self):
        for z in self.zimmer:
            print(f"Zimmer {z.nummer}: {z.typ}, {z.preis}€, Status: {'frei' if not z.besetzt else 'besetzt'}")

    def zimmer_buchen(self, nummer):
        for z in self.zimmer:
            if z.nummer == nummer:
                z.buchen()
                return
        print(f"Zimmer {nummer} gibts nicht")


def main():
    hotel = Hotel()

    z1 = Zimmer(101, 100, "Einzelzimmer")
    z2 = Zimmer(102, 150, "Doppelzimmer")
    z3 = Zimmer(103, 120, "Einzelzimmer")
    z4 = Zimmer(104, 500, "Präsidentensuite")

    hotel.zimmer_dazu(z1)
    hotel.zimmer_dazu(z2)
    hotel.zimmer_dazu(z3)
    hotel.zimmer_dazu(z4)

    print("Zimmerübersicht vor dem Buchen:")
    hotel.zimmer_zeigen()

    hotel.zimmer_buchen(101)
    hotel.zimmer_buchen(102)
    z4.buchen()

    print("\nZimmerübersicht nach Buchungen:")
    hotel.zimmer_zeigen()

    print(f"\nAnzahl freier Zimmer: {hotel.zimmer_frei()}")

    z1.stornieren()

    print("\nZimmerübersicht nach Stornierung:")
    hotel.zimmer_zeigen()


if __name__ == "__main__":
    main()
