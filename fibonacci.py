n=int(input())
a=0
b=1
for i in range(1,n+1):
    c=a+b
    print(f"{a:}",end=" ")
    a=b
    b=c