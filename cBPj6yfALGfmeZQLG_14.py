"""


Create a function that converts a string into a matrix of characters that can
be read vertically. Add spaces when characters are missing.

### Examples

    vertical_txt("Holy bananas") ➞ [
      ["H", "b"],
      ["o", "a"],
      ["l", "n"],
      ["y", "a"],
      [" ", "n"],
      [" ", "a"],
      [" ", "s"]
    ]
    
    vertical_txt("Hello fellas") ➞ [
      ["H", "f"],
      ["e", "e"],
      ["l", "l"],
      ["l", "l"],
      ["o", "a"],
      [" ", "s"]
    ]

### Notes

N/A

"""

def vertical_txt(txt):
  l = txt.split( " " )
  m = max( [ len( s ) for s in l ] )
  l = [ x + ( m - len( x ) ) * " " for x in l ]
  r = [ [ ] for i in range(m) ]
  for i in range( m ) :
    for x in l :
      r[ i ].append( x[ i ] )
  return r

