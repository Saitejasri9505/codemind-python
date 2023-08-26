n=int(input())
f=n*n
s=0
while f>0:
    r=f%10
    s=s+r
    f=f//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    