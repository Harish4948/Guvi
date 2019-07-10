s1=raw_input()
s2=raw_input()
s=""
for i in range(len(s1)):
      #s=sum((ord(s1[i])-97+1)+(ord(s2[i])-97+1))
      #print(chr(s[0]))
      sum_s=(ord(s1[i]))+(ord(s2[i]))-96
      if(sum_s<=122):
            s+=chr((ord(s1[i]))+(ord(s2[i]))-96)
      elif(sum_s>122):
            sum_s-=26
            s+=chr(sum_s)
      
print(s)
