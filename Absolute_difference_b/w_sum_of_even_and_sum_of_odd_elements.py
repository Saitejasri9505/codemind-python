n=int(input())
s=0
f=0
l=list(map(int,input().split()))
for i in l:
    if(i%2==0):
        s=s+i
    if(i%2!=0):
        f=f+i
print(abs(f-s))