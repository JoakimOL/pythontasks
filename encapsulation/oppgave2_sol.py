class Person:
    def __init__(self, fornavn: str , etternavn: str , alder: int):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder

class Arbeidssted:
    def __init__(self, navn: str):
        self.navn = navn
        self.ansatte = []

    def ansett(self, person: Person):
        self.ansatte.append(person)

    def slutt(self, fornavn: str, etternavn: str):
        for ansatt in self.ansatte:
            if ansatt.fornavn == fornavn and ansatt.etternavn == etternavn:
                self.ansatte.remove(ansatt)

def main():
    arbeidssted = Arbeidssted("Cisco")

    assert len(arbeidssted.ansatte) == 0, "Lengden av listen er feil! Vi har ikke ansatt noen enda, så lengden bør være 0"

    ansatt = Person(fornavn = "Ansatt",
                    etternavn = "Ansattesen",
                    alder = 28)

    arbeidssted.ansett(ansatt)

    assert len(arbeidssted.ansatte) == 1, "Lengden av listen er feil! Vi har ansatt en person, så lengden bør være 1"
    assert arbeidssted.ansatte[0].fornavn == "Ansatt", "Fornavnet på den ansatte er feil!"
    assert arbeidssted.ansatte[0].etternavn == "Ansattesen", "Etternavnet på den ansatte er feil!"

    arbeidssted.slutt("Ansatt", "Ansattesen")

    assert len(arbeidssted.ansatte) == 0, "Lengden av listen er feil! En ansatt sluttet så da bør lengden være 0"

    print("Flott! Det ser ut som oppgaven er løst!")


if __name__ == "__main__":
    main()
