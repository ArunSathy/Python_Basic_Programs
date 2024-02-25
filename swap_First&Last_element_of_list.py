li=[1,2,3,4,5]

print('Before swapping : ',li)

# first way ---------

# li[0],li[-1]=li[-1],li[0]

# second  way using temporary variable  -------

# size=len(li)
#
# temp=li[0]
# li[0]=li[size-1]
# li[size-1]=temp

# third way using tuple --------

# tup=(li[-1],li[0])  # packing
# li[0],li[-1]=tup    # unpacking

# fourth way using * operand ------

# first,*middle,last=li
# li=[last,*middle,first]

# fifth way using pop()

first=li.pop(0)
last=li.pop(-1)

li.insert(0,last)
li.append(first)

print('After swapping  : ',li)