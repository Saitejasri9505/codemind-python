a=int(input())
if a<=199:
    b=1.20
elif a>=200 and a<400:
    b=1.50
elif a>=400 and a<600:
    b=1.80
elif a>=600:
    b=2.00
c=a*b
if c>400:
    s=0.15*c
else:
    s=100
bill=s+c
print(f"{bill:.2f}")