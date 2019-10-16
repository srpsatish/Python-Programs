a=int(input("Enter Customer Number : "))
b=int(input("Enter Power Consumed : "))
if(b<25 and b>0):
    rate=5.89*b
elif(b<50 and b>25):
    rate=7.16*b
elif(b<100 and b>50):
    rate=7.89*b
elif(b<200 and b>100):
    rate=9.19*b
else:
    rate=11*b
print("Balance for ",a,"is : ",rate)
