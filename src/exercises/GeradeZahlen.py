# GeradeZahlen.py

def eingabe(cmd = "Eingabe"): 
    try:
        return int(input(cmd))
    except:
        print("Error in Eingabe")

def whileLoop(x, y): 

    i = x
    while (i < y):
        i+=1
        if ((i % 2) != 0): continue
        print(i)
    print("Schleife beendet")

    print('*'*80)

def forLoop(x, y): 
    for i in range(x, y):
        if (i % 2 == 0):
            print(i)
    print("Schleife beendet")

    print('*'*80)

x = eingabe("Von: ")
y =  eingabe("Bis: ")

whileLoop(x,y)
forLoop(x,y)

