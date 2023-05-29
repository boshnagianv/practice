'''

1)Input a  number and check if it is even or odd number.
2)input a string and check if there is 'a' character print appropriate output(for example "there is 'a' character in inputed string"), else print opposite output.
3)input 3 numbers and check which is the biggest and print appropriate output.
4)input a string and print out all characters  of  string using for loop.
5)[1,2,3,4,5] sum all elements inside list using for loop and  assignment operator.
6)input 3 string and check which is the longest word and print appropriate output.
7)Input a string and count the length of the string, if length of string is less than 10,print ‘short word’, elif  greater than 10, print ‘long word’, else ‘too long word’.
8)Input a number and check, if the number divides by 5,print(“ﬁzz”),elif the number divides by 7,print(“buzz”),elif the number divides by 5 and 7 print(“ﬁzbuzz”).
9)check how many ‘a’ characters are in inputed string using for loop and assingment operator.
10)[1,2,3,4,5] multiply all elements inside list using for loop and  assignment operator.
11)[4, 50,37, 56, 71,14] print all numbers that are greater or equal 50.
12)input a string and check if a or b is in inputed string and print appropriate output.
'''

#1)Input a  number and check if it is even or odd number.
'''
def even_odd():
    num = int(input("Enter a number: "))
    if num%2 == 0:
        return True
    else:
        return  False

if even_odd():
    print("Your number is even")
else:
    print("Your number is odd")
'''
#2)Input a string and check if there is 'a' character print appropriate output(for example "there is 'a' character in inputed string"), else print opposite output.

'''
def findA():
    word = input("Enter your word: ")
    for char in word:
        if char == "a":
            return True
        else:
            return False

if findA():
    print("Your word contains 'a' ")
else:
    print("Your word doesn't have 'a'") REVIEW
'''
'''
word = input("Enter a string: ")

if 'a' in word: #IN is a membership operator that checks whether a value is present in a sequence (like a string, list, or tuple)
                #it performs a loop internally to check for membership. It iterates over the elements of the sequence being checked (e.g., characters in a string or elements in a list) and compares them with the specified value.
    print("There is 'a' character in the inputted string.")
else:
    print("There is no 'a' character in the inputted string.")


#3)input 3 numbers and check which is the biggest and print appropriate output.

def max(num1, num2, num3):
    
    if num1 >= num2 and num1 >= num3:
        print("max is", num1)
    elif num2 >= num1 and num2 >= num3:
        print("max is", num2)
    else:
        print("max is", num3)

max(int(input("Enter a number: ")),
    int(input("Enter second number: ")),
    int(input("Enter third number: ")))

#4)input a string and print out all characters  of  string using for loop.

string = input("enter the phrase") #"Our cat is going to be a very beautiful male kitty"
for char in string:
    print(char)

#5)[1,2,3,4,5] sum all elements inside list using for loop and  assignment operator.

numbers = [1,2,3,4,5]
sum = 0
for a in numbers:
    sum += a

print("The sum is ", sum)

#6)input 3 string and check which is the longest word and print appropriate output.
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word3 = input("Enter third word: ")

if len(word1) >= len(word2) and len(word1) >= len(word3):
    print(word1, " is the longest")
elif len(word2) >= len(word1) and len(word2) >= len(word3):
    print(word2, " is the longest")
else:
    print(word3, " is the longest")

#7)Input a string and count the length of the string, if length of string is less than 10,print ‘short word’, elif  greater than 10, print ‘long word’, else ‘too long word’.

uremns = input("Enter your goddamn word: ")
if len(uremns) < 10:
    print(uremns, " is a short word")
elif len(uremns) == 10:
    print(uremns, " is a long word")
else:
    print(uremns, " is too long")
'''

#8)Input a number and check, if the number divides by 5,print(“ﬁzz”),elif the number divides by 7,print(“buzz”),elif the number divides by 5 and 7 print(“ﬁzbuzz”).
ourNumber = int(input("Enter a number to play: "))
if ourNumber % 5 == 0 and not ourNumber %7 == 0:
    print("fizz")
elif ourNumber % 7 == 0 and not ourNumber %5 == 0:
    print("buzz")
elif ourNumber % 5 == 0 and ourNumber % 7 == 0:
    print("fizzbuzz")
else:
    print("neither")

#9)check how many ‘a’ characters are in inputed string using for loop and assingment operator.

checkA = input("Enter a word: ")
def countA(word):
    aer = 0
    for i in word:
        if i == "a":
            aer += 1
    return aer
print(countA(checkA))

#10)[1,2,3,4,5] multiply all elements inside list using for loop and  assignment operator.

numbers = [1,2,3,4]

result = 1
for m in numbers:
    result *= m

print(result)

#11)[4, 50,37, 56, 71,14] print all numbers that are greater or equal 50.
n = [4, 5, 37, 5, 7, 14, 100]
new = []
for f in n:
    if f >= 50:
        new.append(f)
'''
    else:
        break
'''
print(new)

#12)input a string and check if a or b is in inputed string and print appropriate output.

def contLetter(string):
    if "a" in string or "b" in string:
        return "there is a or/and b in your phrase"
    else:
        return "not today"

s = input("Please enter a word: ")

print(contLetter(s))
