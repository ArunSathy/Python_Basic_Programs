li=[1,15,2,4,6,3]

# first way using min() & max()-----

# print('first way  || Smallest : ',min(li),' & Largest : ',max(li))

# second way using sort() -----

# li.sort()
#
# print('second way || Smallest : ',li[0],' & Largest : ',li[-1])

# third way using for() -----

min=li[0]

for i in range(len(li)):
    if li[i]<min:
        min=li[i]

max=li[0]

for i in range(len(li)):
    if li[i]>max:
        max=li[i]

print('third way  || Smallest : ',min,' & Largest : ',max)


# just for a reference; how li[i] works

for i in range(len(li)):
    print(li[i])
