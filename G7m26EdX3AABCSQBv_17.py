"""


Given a very long string of ASCII characters, split the string up into equal
sized groups of size `width`. To properly display the image, join up the
groups with the newline character `\n` and return the output string.

See the miniature examples below for clarity!

### Examples

    format_ascii("0123456789", 2) ➞ "01\n23\n45\n67\n89"
    
    format_ascii("................................", 8) ➞ "........\n........\n........\n........"
    
    format_ascii("^^^^^^^^", 1) ➞ "^\n^\n^\n^\n^\n^\n^\n^"

### Notes

Enjoy the (somewhat oversized) art in the **Tests** tab.

"""

def format_ascii(txt, width):
  return"\n".join(txt[i:i+width] for i in range(0,len(txt),width))

