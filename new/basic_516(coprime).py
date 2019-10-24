import math

n,m=map(int,input().split())
if n==0 and m==0:
    print("0")
gcd=math.gcd(n,m)
if(gcd==1):
    print("1")
else:
    print("0")