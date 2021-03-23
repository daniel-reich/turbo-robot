"""


![Mexican Wave Simulator](https://s3.amazonaws.com/edabit-images/mex.gif)

 _The wave (known as a Mexican wave in the English-speaking world outside
North America) is an example of metachronal rhythm achieved in a packed
stadium when successive groups of spectators briefly stand, yell, and raise
their arms._

Create a function that takes a string and turns it into a Mexican Wave.

### Examples

    wave("edabit") ➞ ["Edabit", "eDabit", "edAbit", "edaBit", "edabIt", "edabiT"]
    
    wave("just do it") ➞ ["Just do it", "jUst do it", "juSt do it", "jusT do it", "just Do it", "just dO it", "just do It", "just do iT"]
    
    wave(" ") ➞ []

### Notes

  * All test cases will be lowercase strings.
  * Ignore spaces (they are considered empty seats).
  * An empty string should return an empty list.

"""

wave = lambda word: [word[:upper_letter_num] + word[upper_letter_num].upper() + word[upper_letter_num + 1:] for upper_letter_num in range(len(word)) if not word[upper_letter_num] == " " ]

