# oop01.py


import json
from m_person import Person

def test01():
    #   
    # Objekt

    pList = []


    p1 = Person("Franz", "Josef", 1710, 97)
    p2 = Person("Micha", "Bartels", 180, 77)

    print(p1.Nachname)

    pList.append(p1)
    pList.append(p2)

    # with open("person.json", "w") as outfile:
    #         json.dump(pList, outfile)

    print(p1.Nachname, p1.bmi())

    print(p1) # __str__ methods
    print(int(p1))

def test02():

    p1=Person(Vorname= "Franz", Nachname = "Josef", Groesse = 1710, Gewicht = 97)
    print(p1)

    p2=Person(Groesse = 1710, Gewicht = 97)
    p2.Alter = 100
    print(p2)
    print(p2.Alter)
test02()