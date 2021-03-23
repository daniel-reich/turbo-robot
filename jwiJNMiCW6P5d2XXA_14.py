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
    a= txt1.split(" ")
    b= txt2.split(" ")
    print(a,b)
    vowels= {'a':0,'e':0,'i':0,'o':0,'u':0}
​
    for items in a[-1]:
        if items.lower() in vowels.keys():
            vowels[items.lower()]+=1
​
    for items in b[-1]:
        if items.lower() in vowels.keys():
            if vowels[items.lower()]==0:
                return False
            else:
                vowels[items.lower()]-=1
​
​
    for k,v in vowels.items():
        if v>0:
            return False
​
    return True

