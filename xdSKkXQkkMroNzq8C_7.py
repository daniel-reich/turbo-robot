"""


Create a function that counts how many D's are in a sentence.

### Examples

    count_d("My friend Dylan got distracted in school.") ➞ 4
    
    count_d("Debris was scattered all over the yard.") ➞ 3
    
    count_d("The rodents hibernated in their den.") ➞ 3

### Notes

  * Your function must be case-insensitive.
  * Remember to `return` the result.
  * Check the **Resources** for help.

"""

def count_d(sentence):
   sum=0
   for i in range(len(sentence)):
      if sentence[i]=='d':
         sum+=1
      if sentence[i]=='D':
         sum+=1
   return sum

