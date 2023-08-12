sec=int(input())
h=sec//3600
second=sec-(h*3600)
m=second//60
seco=second%60
print(f"H:M:S-{h}:{m}:{seco}")