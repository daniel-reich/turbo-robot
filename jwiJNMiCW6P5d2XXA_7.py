"""


Create a function that returns `True` if two lines **rhyme** and `False`
otherwise. For the purposes of this exercise, two lines rhyme if the **last
word** from each sentence contains the **same vowels**.

### Examples

    does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True
    
    does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
    # Capitalization and punctuation should not matter.
    
    does_rhyme("You are off to the races", "a splendid day.") ➞ False
    
    does_rhyme("and frequently do?", "you gotta move.") ➞ False

### Notes

  * Case insensitive.
  * Here we are disregarding cases like _"thyme"_ and _"lime"_.
  * We are also disregarding cases like _"away"_ and _"today"_ (which technically rhyme, even though they contain different vowels).

"""

def does_rhyme(txt1, txt2):
 if txt1[len(txt1)-2].lower()==txt2[len(txt2)-2].lower():
  return True
 else:
  return False
