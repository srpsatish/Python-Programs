import string
s=0
a=0
d=0
l=0
u=0
r=input("enter any digit, character\n")
for i in range(len(r)):
    if(r[i].isspace()):
        s=s+1       
    elif(r[i].isalpha()):
        a=a+1
        if(r[i].islower()):
            l=l+1
        else:
            u=u+1
    elif(r[i].isdigit()):
        d=d+1
print("No of spaces",s)            
print("No of alphabets",a)
print("No of lowercase",l)
print("No of uppercase",u)
print("No of digits",d)