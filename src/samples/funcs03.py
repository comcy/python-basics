# funcs03.py

def test_vars_01():
    global zahl1

    zahl1 = 44
    print("Zahl1:", zahl1)
    print("Zahl2:", zahl2)
    zahl3 = 100

    
def test_vars_02():
    
    def P1():
        nonlocal zahl1 # Verwei auf test_vars_02.zahl
        zahl1 = 1000

    zahl1 = 100
    P1()
    print("Zahl1 in testVars02:", zahl1) 


zahl1 = 10
zahl2 = 20

# test_vars_01()
test_vars_02()