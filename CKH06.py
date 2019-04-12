n=raw_input()
l=map(int,raw_input().split()) #get the numbers
d=dict()    # store the occurances
for i in l:
      if i not in d.keys(): #unique elements
            d.update({i:1})
      else:
            print(i)
            break
