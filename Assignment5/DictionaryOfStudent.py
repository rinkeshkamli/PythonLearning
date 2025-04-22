'''Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''


student_marks = {}
while True:

    student_name = input("Enter the Name of the Student's Or Type 'stop' to finish the student List:")
    if student_name.lower() == 'stop':
        break
    else:
        marks=int(input('Enter %s Marks:'%student_name))
    student_marks[student_name] = marks

search_marks = input("Enter the Name of student's to Search: ")
if search_marks in student_marks:
    print("%s Marks:%s"%(search_marks,student_marks[search_marks]))
else:
    print("Student Not Found")
