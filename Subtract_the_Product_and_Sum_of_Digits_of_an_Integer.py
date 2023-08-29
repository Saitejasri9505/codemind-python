n=int(input())
s=0
d=1
q=n
while n>0:
    r=n%10
    s=s+r
    d=d*r
    n=n//10
print(d-s)