#from __future__ import print_function
n=int(raw_input())
nos=map(int,raw_input().split())
il=list()
for i in range(n):
      if(nos[i]==i):
            il.append(i)
if(len(il)!=0):
      for i in il:
            print(i),
else:
      print("-1")
      
