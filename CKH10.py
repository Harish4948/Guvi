n,m=map(int,raw_input().split())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
flag=0
for i in b:
      if i in a:
            flag=1
      else:
            flag=0
            break
if(flag):
      print("YES")
else:
      print("NO")
