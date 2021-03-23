"""


Create a function that takes a number of a guitar string and the number of the
fret and returns the corresponding frequency of the note.

  * Check the **Resources Tab** , for the correct frequencies per string.
  * The formula to calculate the frequency is: `String Frequency * 2**(fret/12)`.
  * Round the frequency to the nearest hundreth.
  * For this challenge, we use "Standard Tuning".

So, one fret = a semitone = a half step. From D to D♯ for instance.

### Examples

    fret_freq(5, 12) ➞ 220
    
    fret_freq(4, 6) ➞ 207.65
    
    fret_freq(2, 23) ➞ 932.32

### Notes

N/A

"""

def fret_freq(g_str, fret):
  f = [329.63, 246.94, 196, 146.83, 110, 82.41]
  return round(f[g_str-1]*2**(fret/12),2)

