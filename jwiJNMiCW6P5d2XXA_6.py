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

vowels = 'aeiuoAEIUO'
​
def does_rhyme(txt1, txt2):
    
    lastword_of_sentence1 = list(txt1.lower().split())[-1]
    lastword_of_sentence2 = list(txt2.lower().split())[-1]
​
    #find vowels of last word of first sentence
    vowels_in_lastword_of_sentence1 = []
    for i in lastword_of_sentence1:
        if i in vowels:
            vowels_in_lastword_of_sentence1.append(i)
        else: pass
    
    #find vowels of last word of second sentence
    vowels_in_lastword_of_sentence2 = []
    for i in lastword_of_sentence2:
        if i in vowels:
            vowels_in_lastword_of_sentence2.append(i)
        else: pass
​
    if set(vowels_in_lastword_of_sentence1) == set(vowels_in_lastword_of_sentence2):
        return True
    else: 
        return False

