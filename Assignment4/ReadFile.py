'''Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.'''

file_name = 'Sample.txt'
try:
    file = open(file_name, 'r')
    print("Reading File Content:")
    for txt in file.readlines():
        print(txt)
    file.close()

except:
    print("The File %s is not Found" % file_name)
