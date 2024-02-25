li=[1,2,3,4,5]

# first way for() -----

sum=1
for i in li:
    sum=sum*i
print('first way : ',sum)

# second way using numpy -----

import numpy

print('second way : ',numpy.prod(li))