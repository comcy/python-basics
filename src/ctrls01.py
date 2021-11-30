# ctrls01.py

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
        print(i)

loop01()
loop02()