
string1 = input()
uniqueLetters = ""
for each in string1:
   if each not in uniqueLetters:
      uniqueLetters+=each    
print("Number of unique letters=",len(uniqueLetters)) 
print("Unique_Letters=",",".join(uniqueLetters))



