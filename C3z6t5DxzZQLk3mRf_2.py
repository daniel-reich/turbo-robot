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
    freq = [329.63,246.94,196.00,146.83,110.00,82.41]
    symb = ['+<<','+<','>+','>>+',' - ','OK']
    lst2 = []
    for i,x in enumerate(lst):
        dif = x - freq[i]
        if x != 0:
            y = round(abs(dif)/x,2)
        if x == 0:
            lst2.append(symb[-2])
        elif dif == 0:
            lst2.append(symb[-1])
        elif y < .01:
            lst2.append(symb[-1])
        elif y >= .03:
            if dif < 0:
                lst2.append(symb[3])
            else:
                lst2.append(symb[0])
        elif y < .03: 
            if dif > 0:
                lst2.append(symb[1])
            else:
                lst2.append(symb[2])
    return lst2

