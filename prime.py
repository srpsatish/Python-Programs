a=int(input("Enter a number : "))
flag=0
if(a%2==0):
    flag+=1
else:
    flag=0
if(a==0):
    print("Neither Prime nor Composite")
elif(flag==1):
    print("Prime Number")
else:
    print("Composite Number")
