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

import re
​
def remove_double_spaces(sent):
    while re.search('  ', sent):
        sent = re.sub('  ', ' ', sent)
    return sent
​
def begin_with_upper(sent):
    while re.search(' ', sent[0]):
        sent = re.sub(' ', '', sent[0]) + sent[1:]
    if sent[0].islower():
        sent = sent[0].upper() + sent[1:]
    return sent
​
def end_sent_with_period(sent):
    new_sent = ''
    for i in range(len(sent[:-2])):
        if sent[i+2].isupper():
            new_sent = new_sent + sent[i] + '.'
        else: new_sent += sent[i]
    new_sent += sent[-2:]
    while new_sent[-1] == ' ':
        new_sent = new_sent[:-1]
    return new_sent + '.'
    
def correct_sentences(s):
  s1 = remove_double_spaces(s)
  s2 = begin_with_upper(s1)
  s3 = end_sent_with_period(s2)
  return s3

