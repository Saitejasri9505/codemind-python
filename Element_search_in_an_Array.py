n=int(input())
l=list(map(int,input().split()))
e=int(input())
f=False
for i in l:
    if(i==e):
        f=True
        break
if f==True:
    print("True")
else:
    print("False")