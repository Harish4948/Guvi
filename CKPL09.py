from __future__ import print_function
def isPrime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
num=0
i,r=map(int,raw_input().split())
for n in range(i,r+1):
      if(isPrime(n)):
            num+=1
print(num)
      
