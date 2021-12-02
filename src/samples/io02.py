# io02.py

from genericpath import isdir
import os
import os.path

# Suchen von Dateien mit bestimmten Bezeichner

# walk


def find_file(path, pattern):

    for file in os.listdir(path):

        filepath = os.path.join(path, file)

        if os.path.isfile(filepath):
            if file.find(pattern) >= 0:
                print(filepath)

        elif os.path.isdir(filepath):
            newpath = os.path.join(path, filepath)
            find_file(newpath, pattern)


path = r"./"
files1 = find_file(path, "lis")
# files2 = find_file(path, "e")

print(files1)
# print(files2)

for file1 in files1:
    fn = os.path.split(file1)[1]
    filename, filetype = os.path.splitext(fn)
    print(filename, filetype)