# funcs01.py

def test_para_02(l1: list ):
    l1.append(42)

def test_para(a: int, b: int, c: int = 10 ):

    print("*"*34, "test_para", "*"*35)
    print("Parameter a: ", a)
    print("Parameter b: ", b)
    print("Parameter c: ", c)
    print("*"*80, "\n")


x: int  = 10
y = 12
z = 13

test_para(x, y, z)
print("x: ", x)

test_para(20, 30, 40)
test_para("A", "B", "C")
test_para(100, 200)

liste1 = [1,2,3]

test_para_02(liste1)

print(liste1)