string='Welcome to Python World'

text=string.split(' ')
word=text[::-1]

print(' '.join(word))


# just a reference for join() -----

lis=['Arun','Sathyan']
print(lis)
print(' '.join(lis))