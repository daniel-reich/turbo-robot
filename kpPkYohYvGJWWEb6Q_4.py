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

def string_fret(st = 5, fr = 0):
    string = st
    fret = fr
​
    str_dict = {1:'E',2:'B',3:'G',4:'D',5:'A',6:'E'}
    note_lst = ['C','C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    if string in range(1,7) and fret in range(0,25):
​
        if (note_lst.index(str_dict[string])+ fret%12) <= len(note_lst)-1:
​
            return (note_lst[ note_lst.index(str_dict[string])+ fret%12]) 
        else:
            idx = (note_lst.index(str_dict[string])+ fret%12) - 12
            return (note_lst[idx])
    else :
        return ('Invalid input')

