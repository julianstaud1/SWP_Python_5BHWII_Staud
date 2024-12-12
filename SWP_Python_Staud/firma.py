from typing import List, Dict


class Person:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender  # "male" or "female"


class Mitarbeiter(Person):
    def __init__(self, name: str, gender: str, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung
        abteilung.add_mitarbeiter(self)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, gender: str, abteilung):
        super().__init__(name, gender, abteilung)
        if abteilung.leiter is not None:
            raise ValueError(f"Abteilung {abteilung.name} hat bereits einen Leiter.")
        abteilung.set_leiter(self)


class Abteilung:
    def __init__(self, name: str):
        self.name = name
        self.mitarbeiter: List[Mitarbeiter] = []
        self.leiter: Abteilungsleiter = None

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter: Abteilungsleiter):
        self.leiter = leiter

    def get_mitarbeiter_anzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen: List[Abteilung] = []

    def add_abteilung(self, abteilung: Abteilung):
        self.abteilungen.append(abteilung)

    def mitarbeiter_anzahl(self):
        return sum(len(abteilung.mitarbeiter) for abteilung in self.abteilungen)

    def abteilungsleiter_anzahl(self):
        return sum(1 for abteilung in self.abteilungen if abteilung.leiter is not None)

    def abteilung_anzahl(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        return max(self.abteilungen, key=lambda a: a.get_mitarbeiter_anzahl(), default=None)

    def geschlechter_prozent(self):
        total_mitarbeiter = self.mitarbeiter_anzahl()
        if total_mitarbeiter == 0:
            return {"male": 0, "female": 0}
        geschlechter_count = {"male": 0, "female": 0}
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                geschlechter_count[mitarbeiter.gender] += 1
        return {gender: (count / total_mitarbeiter) * 100 for gender, count in geschlechter_count.items()}


# Erstellen einer Beispiel-Firma
firma = Firma("testfirma")

# Abteilungen erstellen
entwicklung = Abteilung("Entwicklung")
marketing = Abteilung("Marketing")

firma.add_abteilung(entwicklung)
firma.add_abteilung(marketing)

# Mitarbeiter und Leiter instanzieren
leiter_entwicklung = Abteilungsleiter("Graf Hugo", "male", entwicklung)
leiter_marketing = Abteilungsleiter("Tom", "male", marketing)

mitarbeiter1 = Mitarbeiter("Anna", "female", entwicklung)
mitarbeiter2 = Mitarbeiter("Tom", "male", entwicklung)
mitarbeiter3 = Mitarbeiter("Clara", "female", marketing)
mitarbeiter4 = Mitarbeiter("Dave", "male", marketing)
mitarbeiter5 = Mitarbeiter("Eva", "female", marketing)
mitarbeiter6 = Mitarbeiter("Torben", "male", entwicklung)

# Methoden testen
print("Anzahl Mitarbeiter:", firma.mitarbeiter_anzahl())
print("Anzahl Abteilungsleiter:", firma.abteilungsleiter_anzahl())
print("Anzahl Abteilungen:", firma.abteilung_anzahl())
print("Größte Abteilung:", firma.groesste_abteilung().name)
print("Geschlechterverteilung:", firma.geschlechter_prozent())
