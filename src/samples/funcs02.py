# funcs02.py

def test01(a = "A", b = "B", c = "C" ): # Optionala params immer rechts

    def test_para(a = "A", b = "B", c = "C" ): # Optionala params immer rechts
        print(a,b,c)
    
    test_para()   
    test_para(1, 2)   
    test_para(1, 2, 3)   
    test_para(c = 4)   
    test_para(c = 3, b = 3)   

    l1 = (10, 20, 30)
    test_para(l1)
    test_para(*l1) # Auflösung    
    
    l2 = (10,20,30,40)
    
    test_para(l2)
    test_para(*l2[:3]) # Auflösung

    d1 = {"a": 58, "b": 59, "c": 60} 
    test_para(d1)
    test_para(**d1) # Auflösung


def test02():
    
    # Offene Parameterliste (Position)
    def test_para(*args):
        print("args", args, type(args))
        for pos, arg in enumerate(args):
            print(pos, arg)

    def sum(*args):
        s = 0
        for x in args:
            s += x
        return s

    test_para(3, 4, "A", {3,4,5})
    test_para(1,2,3,4,5,6,7,8,9)

    print("Summe: ", sum(1,2,3,4,5,6,7,8,9))
    tup1 = tuple(range(1,101)) # 1..100

    print("Summe: Tuppel",sum(*tup1))

def test03():

    # Offene "benannte" Parameterliste
    def test_para(**kwargs):
        print(kwargs, type(kwargs))

    test_para(a = 1, b = 2)

test03()