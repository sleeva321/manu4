x=int(input())
y=0
for i in range(2,x//2+1):
    if(x%i==0):
        y=y+1
if(y<=0):
    print("yes")
else:
    print("no")
