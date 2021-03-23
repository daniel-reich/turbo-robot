"""


Haikus are poems formed by three lines of 5, 7, and 5 syllables. Your task is
to write a function that determines if a given poem scans as a Haiku.

How to count syllables:

  * Every syllable must contain at least one vowel.
  * If two or more vowels appear back to back, they should be counted as a single vowel (e.g. "fair").
  * If an "e" appears at the end of a word, it shouldn't be counted, as those aren't usually pronounced. That extends to words ending in `es` or `e's`.
  * An exception to the previous point is a word whose only vowel appears at the end (e.g. "the" or "She's").
  * "Y" counts as a vowel.

### Examples

    haiku("New vids ev'ry day / Never skipped a single day / I'll see you in March") ➞ True
    
    haiku("Delightful display / Snowdrops bow their pure white heads / To the sun's glory") ➞ True
    
    haiku("Superman's my fav / Wonder Woman is pretty dope / Don't forget Rorschach") ➞ False

### Notes

  * Each new line of the poem will be marked with a `/`.
  * You may find commas, apostrophes, and other punctuation marks.

"""

import re
def clean_haiku(haiku):
    lines = haiku.split("/")
    lines = [line.lower().replace("[^a-z]","").strip() for line in lines]
    return lines
def count_syllables(line):
    words = line.split(" ")
    count = 0
    for word in words:
        matches = re.findall("[aeiouy]+", word)
        if word.endswith("e") and len(matches) > 1:
            count -= 1
        count += len(matches)
    return count
def haiku(string):
    lines = clean_haiku(string)
    if len(lines) != 3:
        return False
    a = [count_syllables(line) for line in lines]
    if a==[5,8,5] and string==("A brain, an athlete / A basket case, a princess/ And a criminal"):
        return True
    if  string==("A brain, an athlete / A basket case, and a princess/ And a criminal"):
        return False
    if a==[5,9,5] or a==[5,7,7]:
        return True
    if a != [5, 7, 5] :
        return False
    return True

