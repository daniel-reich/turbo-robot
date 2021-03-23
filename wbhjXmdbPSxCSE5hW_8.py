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
  desire = desire.lower()
  s= ""
  for ch in desire:
    if ch not in ["a","e","i","o","u"]:
      s+= ch
  no_reps = ""
  for ch in s[::-1]:
    if ch not in no_reps:
      no_reps += ch
  no_reps = no_reps[::-1]   
  return no_reps.upper().replace(" ","")

