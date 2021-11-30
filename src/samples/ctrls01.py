# ctrls01.py

# from time import sleep
import time

def loop01():
    i = 1
    while(i < 10):
        print(i)
        i+=1

def loop02():
    for i in range(1,10):
        print(i)
    
    print("*"*80)
        
    for i in range(1,100,2):
        print(i, end=' ')

    print("*"*80)
    t = ("a", "b", "c")    
    for i in enumerate(t): # enumerate gibt index mit aus
        print(">>> \t",i)
        print("Splitted: ",i[0], i[1],i, "\n")

def loop03():

    i = 0
    print("Start loop", i)
    while(i < 10):
        print(i)

        if i == 5:
            i = 6 
            continue # springt zum Anfang der Schleife
    
        if i == 8:
            break # springt aus der Schleife
        
        i = i + 1
    print("End loop")

# Generator
def my123():   
    yield 1
    yield 2
    yield 3

def loop05():
    for i in my123():
        print(i)
        # sleep(1) # abhängig zum Import
        time.sleep(1)



loop01()
loop02()
loop03()
loop05()