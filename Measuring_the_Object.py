w,a,b,c=map(int,input().split())
if a+b==w or b+c==w or a+c==w or a==w or b==w or c==w:
    print("YES")
else:
    print("NO")