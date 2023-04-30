#Question 2 - 
#Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
#Input : string1 = "India"
#Output : uniqueLetters = i,n,d,a
#Input : string1 = "Dedication"
#Output : uniqueLetters = d,e,i,c,a,t,o,n


string1 = input()
uniqueLetters = ""
for each in string1:
   if each not in uniqueLetters:
      uniqueLetters+=each    
print("Number of unique letters=",len(uniqueLetters)) 
print("Unique_Letters=",",".join(uniqueLetters))



