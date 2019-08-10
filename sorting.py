roll=[5,2,8,1,7,4]
for i in range(len(roll)-1):
    for j in range(i+1,len(roll)):
        if(roll[j]<roll[i]):
            temp=roll[j]
            roll[j]=roll[i]
            roll[i]=temp
print(roll)
