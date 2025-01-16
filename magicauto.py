class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps < 0:
            raise ValueError("PS muss eine positive Zahl sein.")
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition ist nur mit anderen Auto-Objekten möglich.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraktion ist nur mit anderen Auto-Objekten möglich.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplikation ist nur mit anderen Auto-Objekten möglich.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return NotImplemented

    def __len__(self):
        return self.ps

    def __repr__(self):
        return f"Auto({self.ps} PS)"

# Testfälle
if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    # Addition
    print(a1 + a2)  # Erwartet: 110

    # Subtraktion
    print(a1 - a2)  # Erwartet: -10

    # Multiplikation
    print(a1 * a2)  # Erwartet: 3000

    # Vergleichsoperationen
    print(a1 == a2)  # Erwartet: False
    print(a1 < a2)   # Erwartet: True
    print(a1 > a2)   # Erwartet: False

    # len-Funktion
    print(len(a1))  # Erwartet: 50

    # Repräsentation
    print(a1)       # Erwartet: Auto(50 PS)

    # Fehler bei falschen Typen
    try:
        print(a1 + 10)
    except TypeError as e:
        print(e)  # Erwartet: Addition ist nur mit anderen Auto-Objekten möglich.

    try:
        print(a1 - "auto")
    except TypeError as e:
        print(e)  # Erwartet: Subtraktion ist nur mit anderen Auto-Objekten möglich.

    try:
        print(a1 * None)
    except TypeError as e:
        print(e)  # Erwartet: Multiplikation ist nur mit anderen Auto-Objekten möglich.