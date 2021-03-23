"""


October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be
lowercase, so write a function to **normalize** a sentence.

Create a function that takes a string. If the string is **all uppercase
characters** , convert it to **lowercase** and add an **exclamation mark** at
the end.

### Examples

    normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"
    
    normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."
    
    normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."

### Notes

Each string is a sentence and should start with an uppercase character.

"""

def normalize(txt):
  txt = txt.split()
  last, txt[0] = '!' if txt[-1][-1] != '.' else '', txt[0].capitalize()
  return txt[0]+' '+' '.join(txt[1:]).lower() + last

