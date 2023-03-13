
# Her har vi en Person-klasse. Fyll ut Elev- og Ansatt-klassene så de
# har de samme medlemmene som Person, og med sin skole/jobb i tillegg.
#
# Husk trikset med super() som vi så på i fellesskap!
class Person:
    def __init__(self, fornavn, etternavn, alder):
        self.fornavn=fornavn
        self.etternavn=etternavn
        self.alder=alder

class Elev(Person):
    def __init__(self, fornavn, etternavn, alder, skole):
        pass

class Ansatt(Person):
    def __init__(self, fornavn, etternavn, alder, jobb):
        pass


# Kommer du på noen flere type personer som du vil modellere?
# Kanskje finnes det en type ansatt som er enda mer spesifikk, så
# den kan arve fra Ansatt-klassen?
# Her er det frie tøyler for å øve litt ekstra på arv!

if __name__ == "__main__":
    person = Person("A","B",23)
    elev = Elev("A","B",17, "Akademiet")
    ansatt = Ansatt("A","B",39, "Cisco")
