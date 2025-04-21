'''Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''

def Read_data(file_name):
    try:
        file = open(file_name, 'r')
        for txt in file.readlines():
            print(txt)
        file.close()

    except:
        print("The File %s is not Found" % file_name)

file_name = 'Output.txt'
file = open(file_name, 'w')
write_data = input("Enter Text to write to File:")
file.write(write_data)
print("Data Successfully Written to %s"% file_name)
file.close()

Read_data(file_name)

file = open(file_name, 'a')
write_data = input("Enter Additional Text to Append:")
file.write(write_data)
print("Data Successfully Appended")
file.close()

print("Final Content of the File ")
Read_data(file_name)