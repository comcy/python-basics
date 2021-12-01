# GeradeZahlen.py

def eingabe(cmd = "Eingabe"): 
    try:
        return int(input(cmd))
    except:
        print("Error in Eingabe")

def whileLoop01(x, y): 

    i = x
    while (i < y):
        i+=1
        if ((i % 2) != 0): continue
        print(i)
    print("Schleife beendet")

    print('*'*80)

def whileLoop02(x, y): 

    i = x
    while (i < y):
        i+=1
        if ((i % 2) == 0):
            print(i)
    print("Schleife beendet")

    print('*'*80)


def forLoop(x, y): 

    if x % 2 ==1:
        x += 1

    # x = x if x % 2 == 0 else x + 1
    for i in range(x, y):
        if (i % 2 == 0):
            print(i)
    print("Schleife beendet")

    print('*'*80)

x = eingabe("Von: ")
y =  eingabe("Bis: ")

whileLoop01(x,y)
whileLoop02(x,y)
forLoop(x,y)

