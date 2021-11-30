# Rechner.py

def printRes(methodName, res, initX, InitY):
    print(methodName+": ", res, "\t", "x: ", initX, "y: ", InitY, "\n")

def add(x, y):
    return x+y

# def add2(x, y):
#     printRes('Addition', x+y, x, y)

def sub(x, y):
    return x-y

def div(x, y):
    return int(x/y)

def mult(x, y):
    return x*y

def pow(x, y):
    return x**y 


print('*'*80)
print('Rechner.py')

print('Erste Zahl? (x)')
x = int(input())
print('Zweite Zahl? (y)')
y = int(input())

print('Debug :', x, y, type(x), type(y))

# add2(x, y)

res = add(x, y)
printRes("Addition", res, x, y)

res = sub(x, y)
printRes("Substraktion: ", res, x, y)

res = div(x, y)
printRes("Division: ", res, x, y)

res = mult(x, y)
printRes("Multiplikation: ", res, x, y)

res = pow(x, y)
printRes("Potenzierung: ", res, x, y)