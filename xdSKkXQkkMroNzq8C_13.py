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
    a = 0
    for h in range(len(sentence)):
        if sentence[h].lower() == "d":
            a += 1
    return a

