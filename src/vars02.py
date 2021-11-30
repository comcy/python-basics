# vars02.py

def testOct(input): 
    print("Oktal: ", oct(input))


def testBin(input): 
    print("Bin: ", bin(input))

def testHex(input): 
    print("Hex: ", hex(input))

def testOrchestrator(input, system):

    switcher = {
        1: 'hex',
        2: "bin",
        3: "oct",
        4: "int"
    }

    print(switcher.get(system, "Invalid month"))


zInt = 10
zBin = 0b1010
zOct = 0o12
zHex = 0xa

testOrchestrator(zBin, 'int')
testOrchestrator(zInt, 'int')
testOrchestrator(zOct, 'int')
testOrchestrator(zHex, 'int')