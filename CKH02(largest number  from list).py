from __future__ import print_function
n=int(raw_input())
s=map(str,raw_input())
s.sort()
s=s[::-1]
for i in range(n):
      print(s[i],end="")
