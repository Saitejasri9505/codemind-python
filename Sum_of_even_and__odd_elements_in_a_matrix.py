r,c = map(int,input().split())
mat = []
for i in range(r):
    i_l = list(map(int,input().split()))
    mat.append(i_l)
s=0
f=0
for i_l in mat:
    for j in i_l:
        if j%2==0:
            s += j
        else:
            f += j
print(f"{s} {f}")