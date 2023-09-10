n=int(input())
d=n*n
s=0
h=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
f=s*s
while f>0:
    r=f%10
    h=h*10+r
    f=f//10
if h==d:
    print("True")
else:
    print("False")
    