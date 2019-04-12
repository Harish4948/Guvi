#COde to reverse a number
n=int(raw_input())
if(n>=0):
  n=str(n)
  print(n[::-1])
else:
  n=str(n)
  n=[1:-1]+n[-1]
  print("-"+n[::-1])
