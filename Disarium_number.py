n=int(input())
s=0
c=0
h=0
q=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
while s>0:
    r=s%10
    c=c+1
    d=r**c
    h=h+d
    s=s//10
if h==q:
    print("True")
else:
    print("False")