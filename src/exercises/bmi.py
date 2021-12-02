def eingabe(cmd = "Eingabe"): 
    try:
        if cmd != 'q':    
            return input(cmd)
        else:
            return 1
    except:
        print("Error in Eingabe")

def start(name, size, weight):

    personsList = list()

    dataList = list()

    personDict = {"Name" : name, "Size": size, "Weight": weight}
    
    print("Personen: <init>", personsList)

    personsList.append(personDict)

    bmi = calculateBmi(size, weight)
    personDict.update({"Name": name, "BMI": bmi})

    personsList.append(personDict)

    print("Personen: <bmi>", personsList)

    if bmi > 25:
        printResult("übergewichtig")
    if bmi < 18.5:
        printResult("untergewichtig")

# Calculates BMI
def calculateBmi(size, weight):
    return ( weight / ( size / 100 ) ** 2 )

# Prints results
def printResult(resultString):
    print(resultString, "\n")


name = eingabe("Name: ")
size = eingabe("Größe (in cm): ")
weight = eingabe("Gewicht (in kg): ")

start(name, float(size), float(weight))