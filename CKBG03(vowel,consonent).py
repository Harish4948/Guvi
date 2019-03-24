vowels="aeiou"
c=raw_input()
if(c.lower() in vowels):
      print("Vowel")
elif(ord(c)>=97 and ord(c)<=122):
      print("Consonant")
else:
      print("Invalid")
