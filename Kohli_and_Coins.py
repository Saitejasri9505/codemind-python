x=int(input())
if x%10==0:
    c=x//10
    print(c)
elif x%10!=0 and x%5==0:
    c=x//5-x//10
    print(c)
else:
    print("-1")