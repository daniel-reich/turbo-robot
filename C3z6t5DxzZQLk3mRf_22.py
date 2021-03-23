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

properFreq = [329.63,246.94,196.00,146.83,110.00,82.41]
​
def tune(lst):
  pointer = 0
  finalarray = []
  while pointer <6:
    theResult=""
    if lst[pointer] == 0:
      theResult = " - "
    else:
      answer = lst[pointer]/properFreq[pointer]
      theResult=""
      if answer >1.03:
        theResult = "+<<"
      elif answer >1.005:
        theResult = "+<"
      elif answer > 0.995:
        theResult = "OK"
      elif answer > 0.98:
        theResult = ">+"
      elif answer <= 0.98:
        theResult = ">>+"
    finalarray.append(theResult)
    pointer+=1
  return finalarray

