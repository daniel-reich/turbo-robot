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
  if st == 0 or st > 6 or fr < 0 or fr > 24:
    return 'Invalid input'
  notes = ['E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb']
  if (st == 1) or (st == 6):
    note = notes + notes
    note.append(notes[0])
    return note[fr]
  if st == 2:
    notea, noteb = notes[:7], notes[7:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 3:
    notea, noteb = notes[:3], notes[3:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 4:
    notea, noteb = notes[:10], notes[10:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 5:
    notea, noteb = notes[:5], notes[5:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]

