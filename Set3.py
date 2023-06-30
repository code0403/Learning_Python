#1=> 1.  Create a list of tuples, each containing a name and an age. 
#Then, use tuple unpacking to iterate through the list and print each name and age.
    
person_Info = [("Abhishek", 26), ("Amit", 18), ("Mohan", 30), ("John", 56)]

for name, age in person_Info:
    print(f"{name} is {age} years old.")


#2=> Create a dictionary with keys as names and values as ages. 
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary. 

person_dict = {"spiderman": 18, "Ironman":45, "Wanda": 27}
print(person_dict)

def AddName(new_dict, name, age):
    new_dict[name] = age
    return new_dict

res = AddName(person_dict, "Captain Marvel", 30)
print(res)


def UpdateAge(new_dict, name, age):
    new_dict.update({name: age})
    return new_dict

res = UpdateAge(person_dict, "Ironman", 99)
print(res)

def deleteName(new_dict, name):
    del new_dict[name]
    return new_dict

res = deleteName(person_dict, "spiderman")
print(res)

def ClearDict(new_dict):
    new_dict.clear()
    return new_dict
res = ClearDict(person_dict)
print(res)


#3 => Given an array of integers and a target integer, 
# find the two integers in the array that sum to the target.

def find_two_sum(array, target):
    num_dict = {}

    for index, num in enumerate(array):
        ans = target - num
        if ans in num_dict:
            return [num_dict[ans], index]
        num_dict[num] = index

    return None

numbers = [2, 7, 11, 15]
target_sum = 9
result = find_two_sum(numbers, target_sum)
#print(result)

if result:
    print(result)
else:
    print("No two integers found that sum to the target.")


#4=> Write a Python function that checks whether a given word or phrase is a palindrome.

def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "") 
    
    #lower() : A string method that converts all characters in a string to lowercase.
    #replace() : A string method that replaces occurrences of a specified substring with another substring in a string.

    # Check if the word is equal to its reverse
    if word == word[::-1]:      # Slicing with [::-1] reverses the string.
        return True
    else:
        return False


input_word = input("Enter a word or phrase: ") #input(): A built-in function that allows the user to enter input from the keyboard.
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")



#5=> Implement the selection sort algorithm in Python.

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


input = [64, 25, 12, 22, 11]
sorted_array = selection_sort(input)
print(sorted_array)

#6 => Implement Stack using Queue: Use Python's queue data structure to implement a stack.

from queue import LifoQueue

def stack_using_queue():
    stack = LifoQueue()

    stack.put(1)  # Push 1
    stack.put(2)  # Push 2
    print(stack.get())  # Pop and print the top element
    stack.put(3)  # Push 3
    print(stack.get())  # Pop and print the top element
    print(stack.get())  # Pop and print the top element

stack_using_queue()


#7 => Write a Python program that prints the numbers from 1 to 100, but for multiples of three, 
# print "Fizz" instead of the number, for multiples of five, print "Buzz", 
# and for multiples of both three and five, print "FizzBuzz".

def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5==0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
         

FizzBuzz()


#8 => Write a Python program that reads a file, counts the number of words, and writes the count to a new file.

def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        word_count = len(text.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Specify the input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Call the count_words function
count_words(input_file, output_file)


#9 => Write a Python function that takes two numbers as inputs and returns their division,
#  handling any potential exceptions (like division by zero).

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

num1 = 5
num2 = 0
division_result = divide_numbers(num1, num2)
print(division_result)

    
