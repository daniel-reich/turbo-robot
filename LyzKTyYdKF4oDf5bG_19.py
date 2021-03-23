"""


Write a **recursive** function that will return the longest word in a
sentence. In cases where more than one word is found, return the first one.

### Examples

    find_longest("I will and ever will be gratefully and perpetually loving you Tesh!") ➞ "perpetually"
    
    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * You are expected to solve this challenge via a **recursive** approach.
  * An **iterative** versions of this challenge can be found via these links ([1](https://edabit.com/challenge/Z6kRGLpYgSuFQJ7Rx) and [2](https://edabit.com/challenge/Aw2QK8vHY7Xk8Keto)).

"""

def find_longest(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 1):
    Parameters.append("X")
  
  Sample = Parameters[0]
  Answer = Parameters[1]
  
  if (type(Sample) == str):
    
    Code_01 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Code_02 = "abcdefghijklnnopqrstuvwxyz"
    
    Revised = ""
    
    Counter = 0
    Length = len(Sample)
    
    while (Counter < Length):
      
      Item = Sample[Counter]
      
      if (Item.isalpha()):
        Revised = Revised + Item.lower()
        Counter += 1
      else:
        Revised = Revised + " "
        Counter += 1
    
    while ("  " in Revised):
      Revised = Revised.replace("  ", " ")
    
    while (Revised[0] == " "):
      Revised = Revised[1:]
    
    while (Revised[-1] == " "):
      Revised = Revised[0:-1]
    
    Blocks = Revised.split(" ")
    return find_longest(Blocks, Answer)
    
  elif (Sample == []):
    return Answer
  
  elif (len(Sample[0]) > len(Answer)):
    Answer = Sample[0]
    Sample = Sample[1:]
    return find_longest(Sample, Answer)
  
  else:
    Sample = Sample[1:]
    return find_longest(Sample, Answer)

