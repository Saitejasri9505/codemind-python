a=int(input())
b=int(input())
c=0
for i in range(1,a):
    if a%i==0:
        c=c+i
if c==b:
    print("Amicable")
else:
    print("Not Amicable")
    