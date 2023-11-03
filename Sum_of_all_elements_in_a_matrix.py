r,c = map(int,input().split())
mat = []
s=0
for i in range(r):
    i_l = list(map(int,input().split()))
    mat.append(i_l)
for i_l in mat:
    for j in i_l:
        s += j
print(s)
    