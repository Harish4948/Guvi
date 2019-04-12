#Code to check isomorphic string
n,m=map(str,raw_input().split())

unique_n=[]
unique_m=[]
for i in n:
      if i not in unique_n:
            unique_n.append(i)
for i in m:
      if i not in unique_m:
            unique_m.append(i)

if(len(n)==len(m)):
      test=m
      for i in range(len(unique_n)):
            test=test.replace(unique_m[i],unique_n[i])
      if(n==test):
            print("yes")
      else:
            print("no")
else:
      print("no")
