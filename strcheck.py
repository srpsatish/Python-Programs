import string
a=input("enter any digit, character\n")
for i in range(len(a)):
    b=a[i].isalpha()
    print(b)
    c=a[i].isdigit()
    print(c)
    d=a[i].isupper()
    print(d)
    e=a[i].islower()
    print(e)