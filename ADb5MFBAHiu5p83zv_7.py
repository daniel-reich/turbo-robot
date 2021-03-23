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
    string_frequency={
        1: round(329.63,2),
        2: round(246.94,2),
        3: round(196),
        4: round(146.83,2),
        5: round(110),
        6: round(82.41,2)
    }
    for i in string_frequency:
        if g_str==i:
            return round(string_frequency[i]*2**(fret/12),2)

