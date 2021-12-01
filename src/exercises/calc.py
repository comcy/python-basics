def eingabeInt(cmd = "Eingabe"): 
    try:
        return int(input(cmd))
    except:
        print("Error in Eingabe")

def eingabeFloat(cmd = "Eingabe"): 
    try:
        return float(input(cmd))
    except:
        print("Error in Eingabe")



def calc():
    start = eingabeInt("Zählerstand (cbm) Anfang: ")
    end = eingabeInt("Zählerstand (cbm) Ende: ")
    estimatedPrice = eingabeFloat("Preis / cbm: ")

    res = (end - start) * estimatedPrice
    print("Geschätzer Preis: ", res)


calc()
