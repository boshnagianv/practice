'''
1)Write a program to display the first 7 multiples of 7 using both(for, while) loops.
2)Write a program to display only those numbers from a list[12, 75, 150, 180, 145, 525, 50] that satisfy the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
3)Print First 10 natural numbers using while loop.
4)Write a Python program which have number (73421):
 You should calculate (7 + 3 + 4 ….):
5)Write a python program to compute the smallest
number that is divisible by 2 inputed numbers.
Example:
input 14 8
output 2
6)Count how many characters are in given sentence without spaces("Pyhton is awesome!.")
7)Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
8)Create a program that will display the numbers from 1 to 50 which is divisible by 7.
'''


#1)Write a program to display the first 7 multiples of 7 using both(for, while) loops.

multiples = []
count = 0

while count <= 7:
    m = 7 * count
    multiples.append(m)
    count += 1

print(multiples)


'''
while count <= 7:
    for m in range(100):
        if m % 7 == 0:
            multiples.append(m)
            count += 1

    print(multiples)
'''



'''
2)Write a program to display only those numbers from a list[12, 75, 150, 180, 145, 525, 50] that satisfy the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
'''

l = [12, 75, 150, 180, 145, 525, 50]
req = []
for n in l:
    if n % 5 == 0 and n < 150:
        req.append(n)
    if n >= 500:
        break
print(req)

#3)Print First 10 natural numbers using while loop.

naturals = []
cnt = 1

while cnt <= 10:
    naturals.append(cnt)
    cnt += 1

print(naturals)


#4)Write a Python program which have number (73421): You should calculate (7 + 3 + 4 ….):


integ = 73420
sum = 0

digits = str(integ)
for i in digits:
    sum += int(i)
print(sum)


'''
5)Write a python program to compute the smallest
number that is divisible by 2 inputed numbers.
Example:
input 14 8
output 2
'''
numer1 = int(input("Enter first number: "))
numer2 = int(input("Enter second number: "))


def find_common_divisors(n1, n2):
    divisors = []

    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2 %i == 0:
            divisors.append(i)

    return max(divisors)

print(find_common_divisors(numer1,numer2))

#we need to review the loops very well
digitos = [1,2,3,4,5,6,7]
the = []
for i in digitos:
    if i < i+1:
        the.append(i)
print(the)


numbers = [5, 8, 2, 10, 3]

max_number = numbers[0]  # Assume the first number is the maximum

for num in numbers:
    if num > max_number:
        max_number = num

print("The maximum number in the array is:", max_number)

#6)Count how many characters are in given sentence without spaces("Pyhton is awesome!.")

sentence = input("smth: ")

def noSpace(sent):
    chars = 0
    for i in sentence:
        if not i == " ":
         chars += 1
    return chars

print(noSpace(sentence))


'''
def charCount(sent): TRY TO GENERALIZE MAAALAAAADEEEECC
    amount = 0
    for i in sent:
        if not i == " ":
            amount += 1
        return amount

sentence = input("Enter your sentence: ")
print(charCount(sentence))
'''

#7)Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
'''
def storing(posNumber):
    storage = []
    if posNumber>0:
        storage.append(posNumber)
    #return storage

positive = int(input("Enter a number: "))
while positive > 0:
    storing(positive)
    if positive < 0:
        print("vsyo")
        break
print(positive)
'''

'''
def storing():
    positive = int(input("Enter a number: "))
    while positive > 0:
        r = []
        r.append(positive)
        if positive < 0:
            print("vsyo")
        break
storing()
'''
# Initialize variables
sum = 0

# Keep asking for numbers until a negative number is entered
while True:
    number = int(input("Enter a number (enter a negative number to exit): "))

    # Check if the number is negative
    if number < 0:
        break

    # Add the number to the sum
    sum += number

# Print the sum of all entered numbers
print("The sum of all entered numbers is:", sum)

#8)Create a program that will display the numbers from 1 to 50 which is divisible by 7.
'''
sevenDivisors = []
for i in range(0,49):
    if i%7 == 0:
        sevenDivisors.append(i)
print(sevenDivisors)
'''