# sets01.py

def set_test_01():

    s1 = {1,2,3,4,5}
    s2 = {3,3,3,4,4}

    print( s1, type(s1))
    print( s2, type(s2))

    # Vereinigung 
    s3 = s1.union(s2)

    # Schnittmenge
    s4 = s1.intersection(s2)

    print("UNION ", s3)
    print("UNION 2 ", s1 | s2)

    print("INTERSEC ", s4)
    print("INTERSEC 2 ", s1 & s2)

    print("DIFF ", s1.difference(s2))
    print("DIFF 2 ", s1 - s2)



set_test_01()