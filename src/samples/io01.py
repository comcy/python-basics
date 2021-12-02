# io01.py

import os
import os.path
import shutil
import re

os.path.exists

def test_io_01():

    def schreiben(filename):

        try:

            file1 = open(filename, "w", encoding="utf-8")
            file1.write("Erste Zeile ... !!!\n")
            print("Zweite Zeile ...", file=file1)

            for i in range(0,101):
                print(i, i**2, i**3, 2**i, file=file1) #, flush=True
        

            print("OK")

            # file1.flush()
            # file1.close()

        except Exception as ex:
            print("Error", ex.args[0])

        finally:
            file1.close()

    def lesen(filename):

        file1 = None
        try:
            # Existiert die Datei?
            if os.path.exists(filename):
                file1 = open(filename, "r", encoding="utf-8")
                
                erstezeile = file1.readline()
                print("ERSTE ZEILE: ", erstezeile.strip())



                for pos, line in enumerate(file1):
                    print("Zeile: ", pos, ">", line.strip())
                    if pos >= 3:
                        break; # strip entfenrt Steuerzeichen / Leerzeichen
            else:
                print("Datei", filename,  "existiert nicht!!!")
        except Exception as ex:
            print("Error", ex.args[0])

        finally:
            if file1 != None:
                file1.close()

    def lese_verzeichnis(path):
        print(f"*** {path} ***")
        for file1 in os.listdir(path):

            # match

            print(file1, os.path.split(file1))


    # schreiben(r"output/test.txt")
    # lesen("output/test.txt")
    lese_verzeichnis(r"../exercises")

test_io_01()

teststring = "ABC.txt"

mtch = re.match(r"(\d\d\d\d).txt",teststring)
print(">>> ", mtch)

