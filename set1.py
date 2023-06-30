#Hello, World!: Write a Python program that prints "Hello, World!" to the console.

print("Hello, World")

#Data Type Play: Create variables of each data type 
# (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

x = int(3)
k = float(4)
y = str("3")
z = "Abhishek"
a = bool(True)
b = [10,"abhi",2]
c = ("abc","xyz",[4])
d = {5:"hello"}
e = {"name":"abhisekh","age":9}

print("Type of x:",type(x), x)
print("Type of k:",type(k), k)
print("Type of y:",type(y), y)
print("Type of z:",type(z), z)
print("Type of a:",type(a), a)
print("Type of b:",type(b), b)
print("Type of c:",type(c), c)
print("Type of d:",type(d), d)
print("Type of e:",type(e), e)

#Write a Python program to create a list of numbers from 1 to 10, 
# and then add a number, remove a number, and sort the list.

numbers = list(range(1, 11))
print("Original List:", numbers)

numbers.append(11)
print("List after adding 11:", numbers)

numbers.remove(3)
print("List after removing 3:", numbers)

numbers.sort()
print("Sorted List:", numbers)


# Write a Python program that calculates and prints the sum and average of a list of numbers.

numbers = [1, 2,3, 4,5,6,7,8,9,10]

sum_of_numbers = sum(numbers)
print(sum_of_numbers)

avg_of_numbers = sum_of_numbers / len(numbers)
print(avg_of_numbers)

#Write a Python function that takes a string and returns the string in reverse order.
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


text = "Hello, World!"
reversed_text = reverse_string(text)
print("Original String:", text)
print("Reversed String:", reversed_text)

#Write a Python program that counts the number of vowels in a given string.

def count_Vowels(input_string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            count += 1
    return count

str = "abhishek"
ans = count_Vowels(str)
print(ans)   

#Write a Python function that checks whether a given number is a prime number.

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
number = 17
if check_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


#Write a Python function that calculates the factorial of a number.

def factorial(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Test the function
num = 5
factorial_result = factorial(num)
if factorial_result is None:
    print("Cannot calculate factorial of a negative number")
else:
    print("Factorial of", num, "is", factorial_result)


#Write a Python function that generates the first n numbers in the Fibonacci sequence.

def generate_fibonacci(n):
    fibonacci_seq = []
    if n >= 1:
        fibonacci_seq.append(0)
    if n >= 2:
        fibonacci_seq.append(1)
    for i in range(2, n):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    return fibonacci_seq


count = 10
fibonacci_numbers = generate_fibonacci(count)
print("Fibonacci Sequence:")
for number in fibonacci_numbers:
    print(number, end=" ")



#Use list comprehension to create a list of the squares of the numbers from 1 to 10.

squares = [num ** 2 for num in range(1, 11)]
print(squares)

answer = []
for i in range(1,11):
    x = i ** 2
    answer.append(x)
    
print(answer)


