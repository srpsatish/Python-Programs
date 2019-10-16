a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
great=0
small=0
if(a>b and a>c):
    great=a
elif(b>a and b>c):
    great=b
else:
    great=c
print("Greatest Number is : ",great)
if(a<b and a<c):
    small=a
elif(b<a and b<c):
    small=b
else:
    small=c
print("Smallest Number is : ",small)
