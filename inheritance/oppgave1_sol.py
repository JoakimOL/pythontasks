class Person:
    def __init__(self, fornavn, etternavn, alder):
        self.fornavn=fornavn
        self.etternavn=etternavn
        self.alder=alder

class Elev(Person):
    def __init__(self, fornavn, etternavn, alder, skole):
        super().__init__(fornavn,etternavn,alder)
        self.skole = skole

class Ansatt(Person):
    def __init__(self, fornavn, etternavn, alder, jobb):
        super().__init__(fornavn,etternavn,alder)
        self.jobb = jobb

class Superhelt(Person):
    def __init__(self, fornavn, etternavn, alder, superkraft):
        super().__init__(fornavn,etternavn,alder)
        self.superkraft = superkraft


if __name__ == "__main__":
    person = Person("A","B",23)
    elev = Elev("A","B",17, "Akademiet")
    ansatt = Ansatt("A","B",39, "Cisco")
    superhelt = Superhelt("A","B",1000, "superstyrke")
