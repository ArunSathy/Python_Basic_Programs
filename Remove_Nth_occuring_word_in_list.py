li=['hi','arun','hi','sathyan','hi']

print('Before removing : ',li)

word='hi'

n=2

count=0

for i in range(0,len(li)-1):
    if li[i]==word:
        count+=1
        if count>=n:
            del li[i]

print('After removing  : ',li)