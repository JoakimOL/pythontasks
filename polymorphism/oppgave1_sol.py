class Dyr:
    def beveg(self):
        pass
    def snakk(self):
        pass
    def spis(self):
        pass


class Hund(Dyr):
    def beveg(self):
        print("raskt")
    def snakk(self):
        print("voff")
    def spis(self):
        print("hundemat")


class Katt(Dyr):
    def beveg(self):
        print("fort")
    def snakk(self):
        print("Mjau")
    def spis(self):
        print("kattemat")


class Krokodille(Dyr):
    def beveg(self):
        print("sakte")
    def snakk(self):
        print("grrr")
    def spis(self):
        print("kjøtt")


def main():
    dyr1 = Dyr()
    assert isinstance(dyr1, Dyr), "objektet dyr1 er ikke et Dyr, men noe annet!"
    dyr1.beveg()
    dyr1.spis()
    dyr1.snakk()

    katt = Katt()
    assert isinstance(katt, Katt), "objektet katt er ikke en Katt, men noe annet!"
    katt.beveg()
    katt.spis()
    katt.snakk()

    hund = Hund()
    assert isinstance(hund, Hund), "objektet hund er ikke en Hund, men noe annet!"
    hund.beveg()
    hund.spis()
    hund.snakk()

    krokodille = Krokodille()
    assert isinstance(krokodille, Krokodille), "objektet krokodille er ikke en Dyr, men noe annet!"
    krokodille.beveg()
    krokodille.spis()
    krokodille.snakk()


if __name__ == "__main__":
    main()
