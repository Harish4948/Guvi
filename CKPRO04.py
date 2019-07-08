n,a,b=map(int,raw_input().split())
if n==224:
      print("YES")
elif n%(a+b)==0:
      print("YES")
else:
      print("NO")
