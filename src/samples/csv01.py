# csv01.py


# Erstellt ein Person Dictionary
# Param: Ein Personen Objekt
# Return: Dictionary mit Datensatz einer Person
def create_person(**kwargs):

    # BMI berechnen
    # Param gew: Gewicht einer Person
    # Param groesse: Groesse einer Person
    def bmi(gew, groesse):
        return gew / (groesse / 100)**2

    dict1 = {
        "Vorname": "Max",
        "Nachname": "Mustermann",
        "Gewicht": 80,
        "Groesse": "190",
        "Bmi": bmi(80, 190)
    }

    for key in dict1:
        if key in kwargs:
            dict1[key] = kwargs[key]

    # BMI neu berechnen
    dict1["Bmi"] = bmi(dict1["Gewicht"], dict1["Groesse"])

    return dict1


def person_to_csv(p: dict):

    # str()
    # map               map(lambda x: str(x), liste)
    # Comprehension     (strx(x) for x in liste )

    # csv = ";".join(p.values())
    # csv = ";".join( [ f'"{str(x)}"' for x in p.values() ] ) # Mit Anführungszeichen
    csv = ";".join([str(x) for x in p.values()])
    return csv


def person_fields_to_csv(p: dict):
    return ";".join(p.keys())


def save_csv(filename: str, pliste: list):

    file1 = None

    try:
        file1 = open(filename, "w")

        if len(pliste) > 0:

            print(person_fields_to_csv(pListe[0]), file=file1)

            for p in pListe:
                print("Write person dataset:", p)
                print(person_to_csv(p), file=file1)

        print("Datei erfolgreich geschrieben.")

    except Exception as ex:
        print("DATEIFEHLER", ex.args[0])

    finally:
        if file1 != None:
            file1.close()


def load_csv(filename: str):

    personenListe = []
    file1 = None

    try:
        file1 = open(filename, "r")

        header = file1.readline().strip()
        if header == "Vorname;Nachname;Gewicht;Groesse;Bmi":
            for line in file1:
                fields = line.split(";")

                # print(fields, type(fields))  # DEBUG LIST

                # In DICT konvertieren
                pdict = {
                    "Vorname": fields[0],
                    "Nachname": fields[1],
                    "Gewicht": int(fields[2]),
                    "Groesse": int(fields[3]),
                    "Bmi": float(fields[4].replace(",", "."))
                }

                # print(dict, type(dict))  # DEBUG DICT

                personenListe.append(pdict)

                # if field in fields:
                #     field.find("D")

        else:
            print("FALSCHES FORMAT!!!")

    except Exception as ex:
        print("DATEIFEHLER", ex.args[0])

    finally:
        if file1 != None:
            file1.close()

    return personenListe


pListe = []

pListe.append(
    create_person(Vorname="Horst",
                  Nachname="Schlemmer",
                  Gewicht=100,
                  Groesse=168))
pListe.append(
    create_person(Vorname="Pia",
                  Nachname="Flitzebogen",
                  Gewicht=55,
                  Groesse=164))
pListe.append(
    create_person(Vorname="Fritz", Nachname="Penker", Gewicht=56, Groesse=180))
pListe.append(
    create_person(Vorname="Martin", Nachname="Ludolf", Gewicht=88,
                  Groesse=171))

# save_csv("test.csv", pListe)

# neueListe = load_csv("test.csv")
# print('>>> ', neueListe)
# save_csv("copy.csv", neueListe)


def test_typ_pruefung():
    y = 3.14
    print(type(y))
    if type(y) is float:
        print("y ist ein FLOAT")
        print(str(y).replace(".", ","))

    elif type(y) is int:
        print("y ist ein INT")