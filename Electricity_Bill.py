u=int(input())
sc=0.15
if u<=199:
    m=1.20
    b=u*m
elif u>=200 and u<400:
    m=1.40
    b=u*m
elif u>=400 and u<600:
    m=1.60
    b=u*m
elif u>=600 and u<800:
    m=1.80
    b=u*m
else:
    m=2.00
    b=u*m
if b>400:
    s=sc*b
    ta=s+b
else:
    s=0.00
    ta=b
print(f"Units Consumed: {u:}",end="
")
print(f"Cost per Unit: {m:.2f}",end="
")
print(f"Bill: {b:.2f}",end="
")
print(f"Surcharge: {s:.2f}",end="
")
print(f"Total Amount: {ta:.2f}")
    