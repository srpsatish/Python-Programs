n=int(input("Enter a number\n"))
p=1
for i in range(2,(n//2)):
    if(n%i==0):
        p=0
        break;
if(p==0):
    print("Not prime")
else:
    print("Prime")    