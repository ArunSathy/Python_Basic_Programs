li=[1,2,3,4,5,6]

print('Main list : ',li)

# first way -----

my_li=li

print('first way : ',my_li)


# second way -----

my_li=li[:]

print('second way : ', my_li)


# third way using extend() method -----

my_li=[]

my_li.extend(li)

print('third way : ', my_li)


# fourth way using list() -----

my_li=list(li)

print('fourth way : ',my_li)

# fifth way using copy() -----

my_li=li.copy()

print('fifth way : ',my_li)


# sixth way using list comprehension -----

my_li=[i for i in li]

print('sixth way : ',my_li)






