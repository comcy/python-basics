# lists01.py
# tuple, list, dictionary, set


def test_tuple():
    z = 10
    t1 = (1, 2, 3)
    t2 = ("A", "B", "C")
    t2 = ("Mo", "Di", "Mi", "Do", "Fr")
    t4 = (1, "Hans", "Maier", 2000.0, "Hans")

    print(t4, type(t4))
    print(t4[0], t4[1], t4[2], t4[3] )

    anzahl_hans = t4.count("Hans")
    print("#Hans ", anzahl_hans)

    position_hans = t4.index("Hans")
    print("POS Hans ", position_hans)

    len_t4 = len(t4)
    print("Länge t4 ", len_t4)

    print('Länge von ', len("ABCDEFG"))

    try:
        print('Änder erstes Element des Tupels \'t4\'')
        t4[0] = 2 # lässt sich nicht verändern
    except Exception as ex:
        print(ex.args[0])

    print("Schlife über `t4`")
    for i in t4:
        print(i)

    for i in (1,2,3,4):
        print(i)

    print("`t4` erweitern")
    t5 = t4 + (1,2,3,4)
    print(t5)

def test_tuple_2():
    t1 = (1,2,3,4)
    t2 = tuple(i*2 for i in t1)
    t3 = tuple((i*2,i**2) for i in t1)

    print("T1 ", t1, type(t1))
    print("T2 ", t2, type(t2))
    print("T3 ", t3, type(t3))

def test_tuple_3():
    t1 = tuple(range(1,11))
    print("T1 ", t1, type(t1))

    # t1 += 11 # tstr, int,... -> geht nicht
    # t1 += (11) # interpretiert als arith, ausdruck ->  geht nicht
    t1 += (11,) # , hinzufügen -> tuple() mit einem element
    t1 += tuple(range(12,13)) # tuple() -> tuple, das str, int,... hinzufügen nicht geht

    print("T1 ", t1, type(t1))

    t2 = tuple() # tuple() -> tuple, das str, int,... hinzufügen nicht geht
    print("T2 ", t2, type(t2), len(t2))

def test_tuple_4():
    t1 = tuple(range(1,11))
    print("T1 ", t1, type(t1))

    t2 = t1[4:] # ab index 4
    print("T2 ", t2, type(t2), len(t2))

    t3 = t1[2:5] # index 2,3,4
    print("T3 ", t3, type(t3), len(t3))

    t4 = t1[:5] # index 0..5
    print("T4 ", t4, type(t4), len(t4))
 
    t5 = t1[-1] # index 0..5
    print("T5 ", t5, type(t5))

    t6 = t1[-2] # index 0..5
    print("T6 ", t6, type(t6))

    t7 = t1[::2] # index 0..5
    print("T7 ", t7, type(t7))

    t8 = t1[1::2] # index 0..5
    print("T8 ", t8, type(t8))

    t9 = t1[1:5:2] # index 0..5
    print("T9 ", t9, type(t9))

    t10 = t1[5:1:-1] # index 0..5
    print("T10 ", t10, type(t10))

    t10b = tuple(reversed(t1[2:6])) # index 0..5
    print("T10b ", t10b, type(t10b))

    for i in reversed(t1[2:6]):
        print('reversed: ', i, end=" \n")

    for i in sorted((4,3,6,2,8,9)):
        print('sorted: ', i, end=" \n")

def test_tuple_5():
    # Auflösung
    t1 = ("Albert", "Einstein", "Physiker", 99)
    vn, nn, beruf = t1[:3] # eingrenzen per index
    print(vn, nn, beruf)

    t2 = ((1,2),(3,4),(5,6))
    for elem in t2:
        print(elem, elem[0], elem[1])

    # AUflösung in for(each)
    for first, second in t2:
        print(first, second)

def test_tuple_6():

    s = "Hallo Welt"
    for c in s:
        print(c)

    t1 = tuple(s)
    print(t1, type(t1))

    


# test_tuple()
# test_tuple_2()
# test_tuple_3()
# test_tuple_4()
# test_tuple_5()
test_tuple_6()