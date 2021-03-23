"""


A magic sigil is a glyph which represents a desire one wishes to manifest in
their lives. There are many ways to create a sigil, but the most common is to
write out a specific desire (e.g. " _I HAVE WONDERFUL FRIENDS WHO LOVE ME_ "),
remove all vowels, remove any duplicate letters (keeping the last occurence),
and then design a glyph from what remains.

Using the sentence above as an example, we would remove duplicate letters:

    AUFRINDSWHLOVME

And then remove all vowels, leaving us with:

    FRNDSWHLVM

Create a function that takes a string and removes its vowels and duplicate
letters. The returned string should not contain any spaces and be in
uppercase.

### Examples

    sigilize("i am healthy") ➞ "MLTHY"
    
    sigilize("I FOUND MY SOULMATE") ➞ "FNDYSLMT"
    
    sigilize("I have a job I enjoy and it pays well") ➞ "HVBJNDTPYSWL"

### Notes

  * For duplicate letters the **last one** is kept.
  * When performing actual sigil magic, you **must** make your sigils **manually**.
  * Check the **Resources** tab for more info on sigils if you're interested in the concept.

"""

def sigilize(desire):
  x = ''.join(char for char in desire if char.lower() not in 'aeiou')
  x = x.replace(" ","").upper()
  bla = []
  for i in x[::-1]:
    if i not in bla:
      bla.append(i)
  return "".join(a for a in bla[::-1])

