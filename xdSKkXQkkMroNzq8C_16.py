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
  count = 0
  for i in range(len(sentence)):
    if sentence[i] == "D" or  sentence[i] == "d":
      count = count + 1
  return count

