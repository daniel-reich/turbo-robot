"""


Create a function that takes a string `txt` and censors any word from a given
list `lst`. The text removed must be replaced by the given character `char`.

### Examples

    censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
    
    censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
    
    censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

### Notes

N/A

"""

def censor_string(txt, lst, char):
  return " ".join([word if word not in lst else char*len(word)
                for word in txt.split()])

