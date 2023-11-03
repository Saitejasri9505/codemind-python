r,c = map(int,input().split())
mat = []
s=0
f=0
for i in range(r):
    i_l = list(map(int,input().split()))
    mat.append(i_l)
for i in range(r):
    for j in range(c):
        if i%2==0:
            s += mat[i][j]
        else:
            f += mat[i][j]
print(f"{s} {f}")
            

