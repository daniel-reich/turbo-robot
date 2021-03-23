"""


 **Syncopation** means an emphasis on a weak beat of a bar of music; most
commonly, **beats 2 and 4** (and all other _even-numbered_ beats if
applicable).

`s` is a line of music, represented as a string, where hashtags `#` represent
emphasized beats. Create a function that returns if the line of music contains
**any** _syncopation_.

### Examples

    has_syncopation(".#.#.#.#") ➞ True
    # There are Hash signs in the second, fourth, sixth and
    # eighth positions of the string.
    
    has_syncopation("#.#...#.") ➞ False
    # There are no Hash signs in the second, fourth, sixth or
    # eighth positions of the string.
    
    has_syncopation("#.#.###.") ➞ True
    # There are Hash signs in the sixth positions of the string.

### Notes

All other unemphasized beats will be represented as a dot.

"""

def has_syncopation(s):
  return any(i%2 for i,v in enumerate(s) if v=="#")

