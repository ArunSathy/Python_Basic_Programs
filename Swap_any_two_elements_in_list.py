li=[1,2,3,4,5]

print('Before swapping : ',li)

i=int(input('Enter the first element  : '))
j=int(input('Enter the second element : '))

# one way -----

# li[i],li[j]=li[j],li[i]

# second way -----

# tup=(li[j],li[i])  # packing
# li[i],li[j]=tup    # unpacking

# third way -----

# temp=li[i]
# li[i]=li[j]
# li[j]=temp

# way using pop()

first=li.pop(i)
last=li.pop(j-1)

li.insert(i,last)
li.insert(j,first)

print('After swapping  : ',li)