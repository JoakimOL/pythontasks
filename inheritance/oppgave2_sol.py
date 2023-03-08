# Svar på teorioppgave:
# Fordi Fan og Hater lager sin egen __str__
# funksjon som IKKE er arvet fra Person.
# Hadde Person hatt en __str__ funksjon,
# så ville dette vært polymorfisme

class Person:
    def __init__(self, serie: str):
        self.serie = serie

class Fan(Person):
    def __str__(self) -> str:
        return f"Er veldig fan av {self.serie}"

class Hater(Person):
    def __str__(self) -> str:
        return f"Synes {self.serie} er veldig teit"

if __name__ == "__main__":
    fanboy = Fan("Harry Potter")
    fangirl = Fan("Star Wars")
    nett_troll = Hater("Harry Potter")

    print(fanboy)
    print(fangirl)
    print(nett_troll)

    assert str(fanboy) == "Er veldig fan av Harry Potter"
    assert str(fangirl) == "Er veldig fan av Star Wars"
    assert str(nett_troll) == "Synes Harry Potter er veldig teit"
