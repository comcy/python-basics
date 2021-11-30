# vars01.py

# Variable
a = 10
print("a: ", a)

# int
a = a + 1
print("a: ", a, "TYPE: ", type(a)) # class 'int' int ist ein unveränderbarer Datentyp (immutable)

# string
a = "22"
print("a: ", a, "TYPE: ", type(a)) # class 'str' 

# float
a = 2.22
print("a: ", a, "TYPE: ", type(a)) # class 'float' 

# Imag / complex
a = 2j+22
print("a: ", a, "TYPE: ", type(a)) # class 'cpomplex' 

a = 2j-22
print("imag. Anteil: ", a.imag, "REAL: ", a.real, a) 

a = a.conjugate()
print("imag. Anteil: ", a.imag, "REAL: ", a.real, a) # class 'float' 

# boolean

b = True
b = False
b = 10 > 20
print("b: ", b, type(b)) # class 'bool

# None

c = None
print("c: ", c, type(c)) # class 'NoneType

del c
# print("c: ", c, type(c)) # NameError: name 'c' is not defined

# Variablen existieren erst durch Wertzuweisung

print("*"*80)

zahl1 = "20" # str
zahl2 = 30 # int
# erg = zahl1 + zahl2 # type cast ?
#  print("erg: ", erg) # --> TypeError: can only concatenate str (not "int") to str
 
erg1 = int(zahl1) + zahl2 
erg2 = zahl1 + str(zahl2) 
print("erg1 int+str: ", erg1)
print("erg2 str+str: ", erg2)

z = 2056
print("z: ", z)
print("z: ", hex(z))
print("z: ", bin(z))
print("z: ", oct(z))