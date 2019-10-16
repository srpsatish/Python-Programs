first = 0
second = 1
n=int(input("Enter the nth value = "))
print(first)
print(second)
for i in range(0,n-2):
    next=first+second
    first=second
    second=next
    print(next)
