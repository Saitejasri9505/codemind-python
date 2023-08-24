n=int(input())
f=0
for i in range(1,n):
    if n%i==0:
        f=f+i
print(f)