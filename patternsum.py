def sumofs1():
    s1=0
    n=int(input("enter a number:"))
    for i in range(1,n+1):
        s1=s1+i
    print("sumofs1=",s1)
def sumofs2():
    s2=0
    m=int(input("enter a number:"))
    for j in range(1,m+1):
        s2=s2+(j*j)
    print("sumofs2=",s2)
def sumofs3():
    s3=0
    p=int(input("enter a number:"))
    for k in range(1,p+1):
        s3=s3+(k*k*k)
    print("sumofs3=",s3)
def sumofs4():
    s4=0
    q=int(input("enter a number:"))
    for l in range(1,q+1):
        s4=s4+(l**l)
    print("sumofs4=",s4)
def sumofs5():
    s5=0
    r=int(input("enter a number:"))
    for a in range(1,r+1):
        s5=s5+((a**a)**a)
    print("sumofs5=",s5)
sumofs1()
sumofs2()
sumofs3()
sumofs4()
sumofs5()
