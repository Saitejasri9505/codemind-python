a,b,c=map(int,input().split())
s=(a+b+c)/2;
area=s*(s-a)*(s-b)*(s-c)
b=area**0.5
print(f"{b:.2f}")