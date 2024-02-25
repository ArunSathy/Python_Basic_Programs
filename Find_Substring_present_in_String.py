string='Welcome to Python World'

text=input('Enter the word : ')

# first way using if..else

if text in string:
    print(text,'is Present in the String')
else:
    print(text,'is not Present in the String')


# second way using find()

if string.find(text) != -1:
    print(text,'is Present in the String')
else:
    print(text,'is not Present in the String')

