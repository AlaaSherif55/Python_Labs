#1
def checkRangeOFNum(num):
    if 20 <= num <= 50:
        print(f"{num} is between 20 and 50.")
    else:
        print(f"{num} is not between 20 and 50.")


# number = int(input("please enter number: "))
# checkRangeOFNum(number)
        
#############################################333
#2
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
#############################################333
#3
def concateTwoStrings(str1, str2):

    result = " ".join([str1, str2])
    return  result

def concateTwoStrings2(str1, str2):

    result = str1 + str2
    return result

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# result1 = concateTwoStrings(string1, string2)
# result2 = concateTwoStrings2(string1, string2)
# print("Concatenation Method 1:", result1)
# print("Concatenation Method 2:", result2)
#############################################333

#4
def squareOfValues(values):
    squareValues = [x ** 2 for x in values]
    return squareValues

# result = [int(x) for x in input("Enter a list of values separated by space: ").split()]
# squared_values = squareOfValues(result)
# print("Squared List:", squared_values)
#############################################333

#5
def mergeTwoDictionary(dic1, dic2):
    mergedDictionary = {**dic1, **dic2}
    return mergedDictionary


# dic1 = {"a": 1, "b": 2}
# dic2= {"c": 3, "d": 4}
# result = mergeTwoDictionary(dic1, dic2)
# print("the result of merge two dictioanry", result)

#############################################333
#6
def mergeTwoLists(list1, list2):
    result = list1 + list2
    return result

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = mergeTwoLists(list1, list2)
# print("Merged List:", result)

#############################################333
#7
def checkIfKeysExist(dictionary):
    required_keys = ["job", "card_number"]
    return all(key in dictionary for key in required_keys)

# my_dict = {"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"}
# print("Keys Exist:", checkIfKeysExist(my_dict))

#############################################333
#8
def calculateSumForRange(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

# num1=1
# num2=100
# result = calculateSumForRange(num1, num2)

# print(f"The sum of numbers from {num1} to {num2} is: {result}")

#############################################333
#9

def checkIsEvenOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# num = int(input("please enter a number: "))
# result = checkIsEvenOdd(num)
# print(f"The number {num} is {result}.")
    
#############################################333
#10

def reverseString(stringInput):
    return stringInput[::-1]

# input = input("please enter a string: ")
# result = reverseString(input)
# print("the reversed string is:",result)

#############################################333
#11
def is_palindrome(input):

    inputLower = input.lower()
    
    input = ''.join(char for char in inputLower  if char.isalnum())
    
    return   input ==   input[::-1]

# input = input("Enter a string: ")
# if is_palindrome(input):
#     print(f"{input} is a palindrome.")
# else:
#     print(f"{input} is not a palindrome.")

#############################################333
#12

def processList(numbers):

    processList = [x ** 2 for x in numbers if x % 2 != 0]
    return processList


# input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = processList(input)
# print("result of processed List:", result)


#############################################333
#13
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


# input = int(input("please enter a number: "))
# if isPrime(input):
#     print(f"{input} is a prime number.")
# else:
#     print(f"{input} is not a prime number.")

#############################################333
#14

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# input = int(input("Enter a number to calculate its factorial: "))
# print("Factorial:", factorial(input ))

#############################################333
#15
def listOperations(numbers):
    summution = sum(numbers)
    minimum= min(numbers)
    maximum= max(numbers)
    squared=[x ** 2 for x in numbers]
    return [summution,minimum, maximum, squared ]

input = [1, 2, 3, 4, 5]
result = listOperations(input)
print("Result:", result)