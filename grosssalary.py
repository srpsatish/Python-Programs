a=int(input("Enter basic pay : "))
b=int(input("Enter DA : "))
c=int(input("Enter HRA : "))
d=int(input("Enter MA : "))
e=int(input("Enter TA : "))
f=int(input("Enter Tax : "))
g=int(input("Enter PF : "))
A=b+c+d+e
D=f+g
gross=a*b+A-D
print("Gross Salary : ",gross)
