n=int(raw_input())
arr=map(int,raw_input().split())
l=0
for i in range(0,n-2):
      for j in range(i+1,n-1):
            for k in range(j+1,n):
                  if arr[i]<arr[j]<arr[k]:
                        l+=1
print(l)
