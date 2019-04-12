#from __future__ import print_function
m=raw_input()
ip=map(int,raw_input().split())
d=dict()
dup=list()
for i in  ip:
      if i not in d.keys():
            d.update({i:1})
      else:
            dup.append(i)
un=list()
for i in dup:
      if i not in un:
            un.append(i)
if(len(un)!=0):
      un.sort()
      for i in un:
            print(i),
else:
      print("unique")
