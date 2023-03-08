class Ord:
    def __init__(self, ord: str):
        self.ord = ord.lower()
        self.antall = 1

    def leggTilAntall(self) -> None:
        self.antall += 1

    def __str__(self):
        return self.ord

class OrdListe:
    def __init__(self, ordliste: list[str]):
        self.ord = {}
        self.antall= 0
        for ord in ordliste:
            ord = ord.lower()
            if ord in self.ord:
                self.ord[ord].leggTilAntall()
            else:
                self.ord[ord] = Ord(ord)
                self.antall += 1

    def antallOrd(self):
        return self.antall

    def antallForekomster(self,ord: str) -> int:
        ord = ord.lower()
        if ord not in self.ord:
            return 0
        return self.ord[ord].antall

    def vanligste(self) -> tuple[Ord,int]:
        max = 0
        vanligste_ord = Ord("")
        for ord in self.ord.values():
            if ord.antall > max:
                vanligste_ord = ord
                max = ord.antall

        return vanligste_ord, max


def main():
    # Testkode for oppgave 3.1
    iskrem = Ord("ISKREM")
    assert iskrem.antall == 1
    iskrem.leggTilAntall()
    assert iskrem.antall == 2
    assert iskrem.ord == "iskrem"

    with open("scarlet.txt", "r") as f:
        alle_ordene = [line.strip() for line in f]

    ordliste = OrdListe(alle_ordene)
    print(f"det er {ordliste.antallOrd()} unike ord i boken")
    print(f"Holmes forekommer {ordliste.antallForekomster('Holmes')} ganger")
    vanligste_ord, vanligste_ord_antall = ordliste.vanligste()
    print(f"det vanligste ordet er {vanligste_ord}")
    print(f"det vanligste ordet forekommer {vanligste_ord_antall} ganger")

if __name__ == "__main__":
    main()
