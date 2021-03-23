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
  better1 = s.strip()
  better2 = better1[0].upper() + better1[1:]
  better3 = " ".join(better2.split())
  better4 = better3 + "."
  special = better4[1:]
  better5 = ""
  for x in special:
    if x.isupper() == True:
      better5 += ". "
    better5 += x
  almost = better4[0] + better5
  return almost.replace(" . ", ". ")

