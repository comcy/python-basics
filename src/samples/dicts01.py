# dicts01.py


def test_dict_01():

    # Dict, Dictionary
    # Map, Assoziatives Array, JSON

    # Schlüssel: Wert

    d1 = {"A": 65, "B": 66, "C": 67}

    print(d1, type(d1))
    print(d1["A"], d1["B"], d1["C"])

    p1 = {"Vorname": "Hans", "Nachname": "Maier", "Alter": 99}
    p2 = {"Vorname": "Frieder", "Nachname": "Henne", "Alter": 66}

    print(p1["Vorname"])

    for elem in p1:
        print("Key: ", elem, "Value: ", p1[elem])

    print("Keys ", p1.keys())
    print("Values ", p1.values())
    print("Items ", p1.items())

    print("> for elem p1.items")
    for elem in p1.items():
            print("Key: ", elem[0], "Value: ", elem[1])

    print("> for k,v p1.items")
    for k, w in p1.items():
            print("Key: ", k, "Value: ", w)

    # Neuer KW
    p1["Gehalt"] = 9999.99
    del p1["Alter"]
    print("Manipulated (p1): ", p1)


    print("*"*80)

    l1 = [ p1,
            p2, 
            {"Vorname": "Hans", "Nachname": "Maier", "Alter": 99}, 
            {"Vorname": "Frieder", "Nachname": "Henne", "Alter": 66}]

    for p in l1:
        print(p["Vorname"], p["Nachname"])
        if "Alter" in p:
            print("Alter", p["Alter"])
        if "Gehalt" in p:
            print("Gehalt", p["Gehalt"])


def test_dict_02():

    A = "1"
    B = "K1"
    C = (1,2,3,4,5,6)
    D = {"VN": "Bernd", "NN": "Baier"} 

    d1 = {A: B, C : D}
    print(d1)


def test_dict_03():

    d1 = {"Vorname": "Hans", "Nachname": "Maier", "Alter": 99}
    print("D1 ", d1)
    
    d1.update( {"Vorname": "Hans", "Gehalt":"1000"} )
    print("D1 update", d1)

    print(d1.get("Nachname","Mustermann"))

    s = d1["Nachname"] if "Nachname" in d1 else "Mustermann"

    print("S ", s)


# test_dict_01()
# test_dict_02()
test_dict_03()