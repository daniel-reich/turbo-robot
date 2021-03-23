"""


Write a function that gets a string number and a fret of a 6-string guitar in
'standard tuning' and return the corresponding note. For this challenge we use
a 24 fret model.

The notes are:

    C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B

Try not to use a 2 dimensional list. Look at the image on the bottom to see
the note names on the guitar neck.

### Examples

    string_fret(2, 10) ➞ "A"
    
    string_fret(0, 16) ➞ "Invalid input"
    
    string_fret(2, 19) ➞ "F#/Gb"
    
    string_fret(3, 0) ➞ "G"

### Notes

  * If the string or fret number isn't correct return "Invalid input".
  * [24 frets on the guitar neck.](https://edabit-challenges.s3.amazonaws.com/24-frets.png)

"""

def string_fret(st, fr):
  notes = "C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B".split(", ")
  
  if (st < 1 or st > 6 or fr < 0 or fr > 24):
    return "Invalid input"
  
  # string lists
  strings = {}
  string1 = notes[4:] + notes[:4]
  string1 += string1
  string1.append(notes[4])
  strings["string1"] = string1
​
  string2 = notes[11:] + notes[:11]
  string2 += string2
  string2.append(notes[11])
  strings["string2"] = string2
  
  string3 = notes[7:] + notes[:7]
  string3 += string3
  string3.append(notes[7])
  strings["string3"] = string3
​
  string4 = notes[2:] + notes[:2]
  string4 += string4
  string4.append(notes[2])
  strings["string4"] =string4
​
  string5 = notes[9:] + notes[:9]
  string5 += string5
  string5.append(notes[9])
  strings["string5"] = string5
​
  string6 = notes[4:] + notes[:4]
  string6 += string6
  string6.append(notes[4])
  strings["string6"] = string6
​
  return_string = "string{}".format(st)
  
  return strings[return_string][fr]

