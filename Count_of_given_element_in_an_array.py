n=int(input())
lis=list(map(int,input().split()))
e=int(input())
c=0
for i in lis:
    if(e==i):
        c=c+1
print(c)
    