import string
s=0
d=0
l=0
u=0
r=input("Enter your password\n")
z=len(r)    
for i in range(z):
    if(r[i].isspace()):
        s=s+1       
    elif(r[i].isalpha()):
        if(r[i].isupper()):
            u=u+1
    elif(r[i].isdigit()):
        d=d+1
if(z<=8 and z>=3 and u>=1 and d>=1 and s==0):
    print("You have entered VALID passsword")
else:
     print("You have entered INVALID passsword")   