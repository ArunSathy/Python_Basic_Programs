# finding factorial of a number

number=int(input('Enter the number : '))

fact = 1

if number<0:
    print('Enter a positive value...')
else:
    for i in range(1,number+1):
        fact=fact*i
    print('Factorial of',number,'is : ',fact)

# using recursive approach

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print('Factorial using recursion : ',factorial(number))