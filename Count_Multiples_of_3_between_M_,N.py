a,n=map(int,input().split())
count=0
for i in range(a,n):
    if i%3==0:
       count=count+1 
print(count)
