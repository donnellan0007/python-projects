"""
This is a program that counts words
"""

__author__ = 'Seamus Donnellan'

# ... Split method to split the words. get len() attr. 

user_input = input('> Type in a string to count the words: ').split()

print(len(user_input))