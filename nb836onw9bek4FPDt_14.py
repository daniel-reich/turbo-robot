"""


Given a sentence, return the number of words which have the **same first and
last letter**.

### Examples

    count_same_ends("Pop! goes the balloon") ➞ 1
    
    count_same_ends("And the crowd goes wild!") ➞ 0
    
    count_same_ends("No I am not in a gang.") ➞ 1

### Notes

  * Don't count single character words (such as "I" and "A" in example #3).
  * The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
  * Mind the punctuation!
  * Bonus points indeed for using regex!

"""

# https://stackoverflow.com/questions/41871841/javascript-regex-to-check-if-first-and-last-character-are-similar/41871899
# https://stackoverflow.com/questions/55097501/how-to-use-regex-to-tell-if-first-and-last-character-of-a-string-match/55097538
import re
def count_same_ends(txt):
    splitstring = txt.split()
    payload = 0    
​
    sequence = re.compile(r"^(.).*\1$", re.IGNORECASE)
    for i in splitstring:
        if i.isalpha():
            if bool(sequence.match(i)):
                payload += 1
                
        else:
             if bool(sequence.match(i[:-1])):
                  payload += 1
            
    return payload

