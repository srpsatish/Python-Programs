import math
x=0
y=0
f1=open('input.txt')
f2=open('output.txt','w+')
commands=f1.readlines()
for i in range(len(commands)):
    print(commands[i])
    c=commands[i].split()
    c[1]=int(c[1])
    if c[0]=='UP':
        y=y+c[1]
    elif c[0]=='DOWN':
        y=y-c[1]
    elif c[0]=='RIGHT':
        x=x+c[1]
    else:
        x=x-c[1]    
    f2.write('X=%i and Y=%i\n'%(x,y))
print(x,y)
distance=math.sqrt(x**2+y**2)
print(distance)