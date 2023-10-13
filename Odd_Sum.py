n=int(input())
lis=list(map(int,input().split()))
s=0
for i in lis:
    if(i%2!=0):
        s=s+i
print(s)