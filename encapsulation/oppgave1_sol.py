class Person:
    def __init__(self, fornavn: str, etternavn: str, alder: int, jobb: str):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
        self.jobb = jobb

    def hils(self, mottaker: str):
        print(f"Hei {mottaker}!")

def main():
    person1 = Person("Joakim", "Lier", 28, "Cisco")
    print(person1.fornavn)
    print(person1.etternavn)
    print(person1.alder)
    print(person1.jobb)

    person1.hils("Børre")

if __name__ == "__main__":
    main()
