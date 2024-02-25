import re

string=input('Enter the string : ')

symbol=re.compile('[!@#$%^&*()_<>,.;:~`|]')

if symbol.search(string)==None:
    print('No Special characters')
else:
    print('Contains special characters')
