'''
1)Write a Python program to get a string from a given string where all occurrences of its "r" char have been changed to '$'.
example: 'restart'
Result : '$esta$t'
2)Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
3) Write a Python program to compute sum of digits of a given string.
4)Write a Python program to remove spaces from a inputed sentence.
5)Write python program to print even length words from inputed sentence.
6)Write a program to count how many letters and numbers are in given word
Example: "2 + 2 is equal to 4"
7)Write a Python program to count the number of characters (character frequency) in a string.
example:"hello world"
output:
h 1
e 1
l 3
...
8) Write a Python script that takes input from the user and displays that input back in upper and lower cases.
9)Write a Python script that has a list and convert into comma separated string.
Sample list:['Geeks', 'for', 'Geeks']
output:Geeks-for-Geeks
10)Python program to convert  starting letter of a word in upper case format or in the title format.
sample list: ["hello", "this", "is", "pythonlobby"]
output: Hello This Is Pythonlobby


'''

'''
1)Write a Python program to get a string from a given string where all occurrences of its "r" char have been changed to '$'.
example: 'restart'
Result : '$esta$t'
'''

def repl(word):
    return word.replace("r", "$")

ourWord = input("Enter your word: ")
print(repl(ourWord))

'''
2)Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23" REVIEWwwwwwwwwwwwwwwww
Expected Output: "32,054.23"
'''

string = input("Enter the float number: ")
string_list = list(string)

for char in range(len(string_list)):
    if string_list[char] == ".":
        string_list[char] = ","
    elif string_list[char] == ",":
        string_list[char] = "."

swapped_string = "".join(string_list)
print(swapped_string)

#3) Write a Python program to compute sum of digits of a given string.

number = input("Enter your number: ")
sum = 0

for v in number:
    sum += int(v)
print(sum)



#4)Write a Python program to remove spaces from a inputed sentence.

'''

def noSpace(sentence):
    for char in sentence:
        if char == " ":
            sentence[char].replace(" ", "g")
    return sentence

phrase = input("Enter your sentence: ")

print(noSpace(phrase))

'''

def noSpace(sentence):
    modified_sentence = ""
    for char in sentence:
        if char == " ":
            modified_sentence += ""
        else:
            modified_sentence += char
    return modified_sentence

phrase = input("Enter your sentence: ")

print(noSpace(phrase)) #REVIEW



#5)Write python program to print even length words from inputed sentence.

sent = input("Enter your evenly sentence: ")





