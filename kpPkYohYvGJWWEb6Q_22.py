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
    if st<1 or st>6 or fr<0 or fr>24:
        return 'Invalid input'
    neck=((5,2,7,4,1,5),(7,3,14,11,8,6),(13,10,1,5,2,13),(7,4,8,6,3,7),\
           (14,11,2,13,10,14),(1,5,3,7,4,1),(8,6,10,14,11,8),(2,13,4,1,5,2),\
           (3,7,11,8,6,3),(10,14,5,2,13,10),(4,1,6,3,7,4),(11,8,13,10,14,11),\
           (5,2,7,4,1,5))
    notes=('A','B','C','D','E','F','G','A#/Bb','','C#/Db','D#/Eb','','F#/Gb','G#/Ab')
    if fr>12:
        fr-=12
    return notes[neck[fr][st-1]-1]

