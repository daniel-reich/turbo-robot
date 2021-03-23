"""


 **Mubashir** is not so good with the English language. He needs your help to
correct his sentences.

  1. Start each sentence with an **uppercase alphabet**.
  2. For every uppercase letter (other than the first alphabet), you have to place a **fullstop(.) followed by an empty space**.
  3. There must be only **one space** between the words and sentences.
  4. Sentence must end with a **full stop(.)**
  5.  **Two continuous spaces** are not allowed.

    correct_sentences ("  mubashir loves  edabit  Matt  loves  edabit  ") ➞ "Mubashir loves edabit. Matt loves edabit."
    
    # Remove extra spaces.
    # Capitalise first character.
    # Dot followed by an empty space before "Matt".
    # A dot at the end.

### Examples

    correct_sentences ("  mubashir loves  edabit  Matt  loves  edabit  ") ➞ "Mubashir loves edabit. Matt loves edabit."
    
    correct_sentences ("  he is an engineer He sleeps a lot") ➞ "He is an engineer. He sleeps a lot."
    
    correct_sentences (" his english is not good Help him     Thank you") ➞ "His english is not good. Help him. Thank you."

### Notes

N/A

"""

def correct_sentences(s):
    for i in range(6):
        s = s.replace('  ',' ')
    if s[-1] == ' ':
        s = s[:-1]
    s += '..'
​
    a = ''
    for i in range(1,len(s)-1):
        if s[i+1].isupper():
            a += '.'+s[i]
        else:
            a += s[i]
    s = ''
    for i in range(len(a)):
        if i == 0:
            s += a[i].upper()
        else:
            s += a[i]
    return s

