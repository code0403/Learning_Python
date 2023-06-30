#1=> Write a program to print the following number pattern using a loop.
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#2=> Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions
"""
- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
"""

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)


#3=> Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
#For example, s1=”Hello”, s2=”World”. Then output “HelloWorld“

def append_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

s1 = "Ault"
s2 = "Kelly"
result = append_middle(s1, s2)
print(result)


#4=> Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"
lower_cased = []
upper_cased = []

for char in str1:
        if char.islower():
            lower_cased.append(char)
        else:
            upper_cased.append(char)


answer_string = ''.join(lower_cased + upper_cased)
print(answer_string)


#5=> Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, 
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list = []

length = min(len(list1), len(list2))

for i in range(length):
    new_list.append(list1[i] + list2[i])


    new_list.extend(list1[length:])
    new_list.extend(list2[length:])


print(new_list)


#6=> Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

ans = []
for item in list1:
    for item2 in list2:
        ans.append(item + item2)
        print()

print(ans)  


#7=> Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in 
# original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

def iterate_lists(list1, list2):
    for item1, item2 in zip(list1, reversed(list2)):
        print(item1, item2)



iterate_lists(list1, list2)


#8=> Initialize dictionary with default values
#In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_data = {employee: defaults.copy() for employee in employees}

print(employee_data)


#9=> Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

ans_dict = {key: sample_dict[key] for key in keys}
print(ans_dict)



#10=> Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list
listAns = list(tuple1)
#print(listAns)

# Modify the first item of the list
listAns[1][0] = 222
#print(listAns)

# Convert the list back to a tuple
ansTuple = tuple(listAns)
#print(ansTuple)

# Print the modified tuple
print(ansTuple)

