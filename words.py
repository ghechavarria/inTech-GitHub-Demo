# Program to sort alphabetically the words from a string provided by the user
#take input from a user
my_str = input("Enter a string: ")

#breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

#sort the list
words.sort()

#print the sorted words
for word in words:
    print(word)