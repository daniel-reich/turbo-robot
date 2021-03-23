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

def does_rhyme(s1,s2):
    s1=s1.split()[-1]
    s2=s2.split()[-1]
    vowels='aeiou'
    s1_ch=[x.lower() for x in s1 if x.isalnum() and x.lower() in vowels]
    s2_ch=[x.lower() for x in s2 if x.isalnum() and x.lower() in vowels]
    if s1_ch==s2_ch:
        return True
    else:
        return False

