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
  notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  strings = {6:'E', 5:'A', 4:'D', 3:'G', 2:'B', 1:'E'}
  if st not in range(1,7) or fr > 24:
    return 'Invalid input'
  return notes[(notes.index(strings[st]) + fr)%12]

