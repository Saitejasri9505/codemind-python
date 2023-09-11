n=int(input())
s=0
c=0
f=0
for i in range(1,n):
    if n%i==0:
        c=c+1
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
for i in range(1,s):
    if s%i==0:
        f=f+1
if c==1 and f==1:
    print("circular prime")
elif c==1 and f!=1:
    print("prime but not a circular prime")
else:
    print("not prime")
    
    