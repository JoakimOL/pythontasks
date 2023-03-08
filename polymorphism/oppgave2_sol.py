class FilLeser:
    def __init__(self, filnavn=None):
        self.filnavn = filnavn
        self.innhold = ""

    def lesFil(self, filnavn=None):
        if filnavn == None:
            filnavn = self.filnavn
        with open(filnavn, "r") as f:
            self.innhold = f.read()

class LitenFilLeser(FilLeser):
    def __init__(self, filnavn=None):
        super().__init__(filnavn)

    def lesFil(self, filnavn=None):
        super().lesFil(filnavn)
        self.innhold = self.innhold.lower()

class StorFilLeser(FilLeser):
    def __init__(self, filnavn=None):
        super().__init__(filnavn)

    def lesFil(self, filnavn=None):
        super().lesFil(filnavn)
        self.innhold = self.innhold.upper()

class DestruktivFilLeser(FilLeser):
    def __init__(self, filnavn=None):
        super().__init__(filnavn)

    def lesFil(self, filnavn=None):
        svar = input("er du sikker på at du vil dette? Y/n")
        if svar.lower() == 'y':
            if filnavn == None:
                filnavn = self.filnavn
            with open(filnavn, "r+") as f:
                self.innhold = f.read()
                f.truncate(0)
                f.write("Boom!")
                self.gjenopprettFil(filnavn+".backup")

    def gjenopprettFil(self, filnavn=None):
        with open(filnavn, "w") as f:
            f.write(self.innhold)


class TulleFilLeser(FilLeser):
    def __init__(self, filnavn=None):
        super().__init__(filnavn)

    def lesFil(self, filnavn=None):
        if filnavn == None:
            filnavn = self.filnavn
        super().lesFil(filnavn)
        with open(filnavn, "a") as f:
            from random import randint
            if randint(1,10) == 5:
                f.write("promp")

if __name__ == "__main__":
    les = FilLeser("foo.txt")
    les.lesFil()
    print(les.innhold)

    les = StorFilLeser("foo.txt")
    les.lesFil()
    print(les.innhold)

    les = LitenFilLeser("foo.txt")
    les.lesFil()
    print(les.innhold)

    les = TulleFilLeser("foo.txt")
    les.lesFil()
    print(les.innhold)

    les = DestruktivFilLeser("foo.txt")
    les.lesFil()
    print(les.innhold)
