# pickle01.py

import pickle
import csv01
import json

# Daten serialisieren

def serialize_pickle():
    pListe = csv01.load_csv(r"test.csv")

    # outfile = open("test.bin", "wb")
    # pickle.dump(pListe, outfile)
    # outfile.close()

    with open("test.bin", "wb") as outfile:
        pickle.dump(pListe, outfile)

    print("DATEI ERZEUGT")


def deserialize_pickle():
    with open("test.bin", "rb") as infile:
        pl = pickle.load(infile)

    print(pl, type(pl))


def serialize_json():

    pListe = csv01.load_csv(r"test.csv")
    with open("personen.json", "w") as outfile:
        json.dump(pListe, outfile)

    # json_string = json.dumps(pListe, outfile)
    # print(json_string)

def deserialize_json():

    with open("personen.json", "r") as infile:
        pl = json.load(infile)

    print(pl, type(pl))


# serialize_pickle()
# deserialize_pickle()

# serialize_json()
deserialize_json()
