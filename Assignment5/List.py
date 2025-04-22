'''Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

lst =[]

for i in range(1,11):
    lst.append(i)

print("Original List:",lst)

lst2=lst[:5]
print("Extracted List:",lst2)
lst3=lst2[::-1]
print("Reverse List:",lst3)
