n=int(input())
s=0
d=n*n
q=n
while d>0:
    r=d%10
    s=s+r
    d=d//10
if s==q:
    print("Neon Number")
else:
    print("Not Neon Number")