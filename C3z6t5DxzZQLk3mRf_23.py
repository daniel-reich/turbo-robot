"""


Create a function that takes guitar strings as an array of frequencies,
starting at the first string (High E) and ending in the sixth string (Low E).

The function must return the display of a tuner for each string, in the same
order, as an array.

You can find the frequencies of the strings on the Wikipedia page (check the
**Resources** tab).

  * The guitar strings are played 1st to 6th, High E to Low E.
  * If the guitar string matches, return `"OK"` for that guitar string.
  * If it's too low, return `">+"` for 1 or 2 percent off (the arrow means, tune up).
  * Return `">>+"` if it's way off. For more than 3 percent.
  * If it's too high, return `"+<"` for 1 or 2 percent, and `"+<<"` for more, (tune down).
  * Check the rounded percentages.
  * If `0` is given, the guitar string isn't played, return `" - "`.

### Examples

    tune([0, 246.94, 0, 0, 0, 80]) ➞ [" - ", "OK", " - ", " - ", " - ", ">>+"]
    
    tune([329, 246, 195, 146, 111, 82]) ➞ ["OK", "OK", ">+", ">+", "+<", "OK"]
    
    tune([329.63, 246.94, 196, 146.83, 110, 82.41]) ➞ ["OK", "OK", "OK", "OK", "OK", "OK"]

### Notes

Items in the list will always be numbers.

"""

def tune(lst):
    freq = [329.63, 246.94, 196, 146.83, 110, 82.41]
    res = []
    for x in range(len(lst)):
        if lst[x] == 0:
            res.append(' - ')
            continue
        diff = round((freq[x]) - lst[x] )/ lst[x] * 100
        if .5 >= diff >= -.5:
            res.append('OK')
        elif -0.5 > diff > -2.5:
            res.append('+<')
        elif diff <= -2.5:
            res.append('+<<')
        elif 0.5 < diff < 2.5:
            res.append('>+')
        elif diff >= 2.5:
            res.append('>>+')
    return res

