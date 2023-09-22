# Program to sort alphabetically the words from a string provided by the user

#pip install termcolor
from termcolor import colored

#define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#take input from a user
my_str = input("Enter a string: ")

#remove punctuation
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

#breakdown the string into a list of words
words = [word.lower() for word in no_punct.split()]

#sort the list
words.sort()

#print the sorted words
for word in words:
    #print with colored words
    print(colored(word, 'blue'))