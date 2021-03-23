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
  txt1=txt1.lower()
  txt2=txt2.lower()
  lst=[]
  lst2=[]
  vowels=[]
  vowels2=[]
  txt1=txt1.replace('.','')
  txt1=txt1.replace('!','')
  txt1=txt1.split(' ')
  for i in txt1:
    lst.append(i)
  one=lst[-1]
  txt2=txt2.replace('.','')
  txt2=txt2.replace('!','')
  txt2=txt2.split(' ')
  for i in txt2:
    lst2.append(i)
  two=lst2[-1]
  for i in one:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
      vowels.append(i)
  for i in two:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
      vowels2.append(i)
  if(vowels==vowels2):
    return True
  else:
    return False

