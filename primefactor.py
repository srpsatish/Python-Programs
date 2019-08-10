n=int(input("Enter a number\n"))
p=1
for i in range(2,n):
    if(n%i==0):
        for m in range(2,(i//2)):
            if(i%m==0):
                p=0
                break;
        if(p==1):
            print(i)