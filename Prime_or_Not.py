# check for prime number

number=int(input('Enter the number : '))

count=0

if number>1:
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count ==2:
        print('It\'s a Prime Number')
    else:
        print('It\'s not a Prime Number')
else:
    print('Enter a positive number..')
