#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
emLi=[]
w1=input("Enter a word: ")
w2=input("Enter a word: ")
w3=input("Enter a word: ")
w4=input("Enter a word: ")
w5=input("Enter a word: ")
emLi.insert(0,w1)
emLi.insert(1,w2)
emLi.insert(2,w3)
emLi.insert(3,w4)
emLi.insert(4,w5)
print(emLi)
