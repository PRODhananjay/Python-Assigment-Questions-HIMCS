# Program to remove punctuation from a given string 

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("enter a string here: ")

empty_str = ""

for i in string:
    if i not in punc:
        empty_str+=i

print (empty_str)