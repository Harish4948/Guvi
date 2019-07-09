from fractions import gcd
n,q=map(int,raw_input().split())
arr=map(int,raw_input().split())
res=list()
for i in range(q):
      q=map(int,raw_input().split())
      if(arr[q[0]-1]==arr[q[1]-1]):
            res.append(arr[q[0]-1])
      else:
            res.append(gcd(arr[q[0]-1],arr[q[1]-1]))
for i in res:
      print(i)
      
      
      
