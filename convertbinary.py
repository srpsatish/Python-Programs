z=0
while(z==0):
    n=input("Enter a binary number\n")
    b=len(n)
    z=1
    for i in range(b):
        if(n[i]!="0" and n[i]!="1"):
            z=0
            break
    if(z==1):
        dec=0
        for i in range(b):
            n=int(n)
            rem=n%10
            dec=dec+rem*2**i
            n=n//10
        print(dec)        

        