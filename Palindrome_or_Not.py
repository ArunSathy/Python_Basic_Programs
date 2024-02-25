string=input('Enter the text : ')


text=string[::-1]

if string==text:
    print('Palindrome : ',text)
else:
    print('Not a Palindrome : ',text)