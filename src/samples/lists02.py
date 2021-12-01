# lists02.py


def test_list_01():

    # Tuples: immutable
    t1 = (1, 2, 3)
    print(t1, type(t1))

    # Lists: immutable

    l1 = [1, 2, 3]
    print(l1, type(l1))

    t2 = t1
    l2 = l1
    # Kopie, Clone erzeugen
    l2 = list(l1)  # Neue Liste mit den Elementen aus l1
    l3 = l1.copy()

    t2 = t2 + (4, )
    l2.append(4)

    print("T1: ", t1, type(t1))
    print("L1: ", l1, type(l1))

    print("T2: ", t2, type(t2))
    print("L2: ", l2, type(l2))

    print("L3: ", l3, type(l3))


def test_list_02():
    l1 = ["A", "B"]

    # Leere Liste
    l2 = []
    l3 = list()

    for i in range(1, 10):
        l2.append(i)

    l4 = list(range(1, 10))

    l3.append(42)  # 42 anfügen
    l3.append(l2)  # Liste l2 anfügen

    print("L2 ", l2, type(l2), "#", len(l2))

    print("L3 ", l3, type(l3), "#", len(l3))

    l3[1].append(10)
    print("L3 ", l3, type(l3), "#", len(l3))


def test_list_03():

    l1 = ["A", "B", "C", "C"]
    l2 = ["D", "E", "F"]
    l3 = list("DEF")


    # l1.append(l2) #  List 12 wird komplett in l1 eingefügt
    l1.extend(l2) #  Element aus 12 werden in l1 angefügt
    print("L1 ", l1, type(l1), "#", len(l1)) 

    l1.insert(0, "XXXX")
    l1.insert(0, "YY")
    l1.insert(0, "ZZZ")

    print("L1 ", l1, type(l1), '#', len(l1))

    last = l1.pop

    print("L1 ", l1, type(l1), '#', len(l1))

    l1.remove("C") # entfernt nur erstes finding
    # l1.remove("C") # entfernt nur erstes finding
    print("L1 ", l1, type(l1), '#', len(l1))

    exist = "C" in l1 # findet nur erstes finding
    print('Exist("C")', exist)

    if exist:
        pos = l1.index("C", 0)
        print('Pos("C")', pos)
    

def test_list_04():

    def mySelector(x):
        # return str(x)
        return -int(x)

    l1 = [3,4,2,5]

    l1.sort() # .reverse()
    print("L1 sortiert ", l1)

    l1.reverse() # .reverse()
    print("L1 reverse sortiert", l1)

    l1.append("11")
    l1.append("1")

    # Lambda-Ausdruck => Funktionsausdruck
    # Funktion ohne Namen
    # mySelector = lambda x: -int(x)

    l1.sort(key = mySelector) #.reverse()
    print("L1 sortiert ", l1)

    # Auch Lambda
    l1.sort(key = lambda x: -int(x)) #.reverse()
    print("L1 sortiert mit Lambda ", l1)

    l2 = ["BB", "A", "CCC", "DD", "AA", "DDDD", "EEE"]
    l2.sort(reverse = True, key = lambda x: len(x)) # sortiert nach der Länge
    print("Sortiert nach der Länge ", l2)


def test_list_05():

    l1 = [1,2,3]
    l2 = ["A", "B", "C"]
    l3 = l1 + l2
    
    # l1 = l1 + l2

    print("L3 ", l3)
    print(l1*5)

    l4 = zip(l1,l2)
    print("L4 ", l4)

    for elem in l4:
        print("Elemeents in L4 ", elem, type(elem))
    for a, b in l4:
        print("a,b ", a,b)

def test_list_06():
    
    l2 = ["A", "B", "C"]
    l3 = list(map(lambda x: (x, ord(x)), l2))
    print("L3 ", l3)

    l4 = [ [elem, ord(elem) ] for elem in l2] # Comprehension => List Comprehension
    print("L4 ", l4)

    l5 = [ (i,j) for i in range(1,10) for j in range (0,10)]
    print("L5 ", l5)

    l6 = []
    for i in range(1,10):
        for j in range (1,10):
            if i < j:
                l6.append((i,j))

    print("L6 ", l6)


# test_list_01()
# test_list_02()
# test_list_03()
# test_list_04()
# test_list_05()
test_list_06()