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
    if g_str == 1:
        string_frequency = 329.63
    elif g_str == 2:
        string_frequency = 246.94
    elif g_str == 3:
        string_frequency = 196
    elif g_str == 4:
        string_frequency = 146.83
    elif g_str == 5:
        string_frequency = 110
    elif g_str == 6:
        string_frequency = 82.41
    return round(string_frequency * 2**(fret/12), 2)

