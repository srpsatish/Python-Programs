z=''
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
        else:
            z=z,str(n),''
print('prime number :',z)
