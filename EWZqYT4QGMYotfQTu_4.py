"""


Tap code is a way to communicate messages via a series of taps (or knocks) for
each letter in the message. Letters are arranged in a 5x5 _polybius square_ ,
with the letter "K" being moved to the space with "C".

       1  2  3  4  5
    1  A  B C\K D  E
    2  F  G  H  I  J
    3  L  M  N  O  P
    4  Q  R  S  T  U
    5  V  W  X  Y  Z

Each letter is translated by tapping out the _row_ and _column_ number that
the letter appears in, leaving a short pause in-between. If we use "." for
each tap, and a single space to denote the pause:

    text = "break"
    
    "B" = (1, 2) = ". .."
    "R" = (4, 2) = ".... .."
    "E" = (1, 5) = ". ....."
    "A" = (1, 1) = ". ."
    "K" = (1, 3) = ". ..."

Another space is added between the groups of taps for each letter to give the
final code:

    "break" = ". .. .... .. . ..... . . . ..."

Write a function that returns the tap code if given a word, or returns the
translated word (in lower case) if given the tap code.

### Examples

    tap_code("break") ➞ ". .. .... .. . ..... . . . ..."
    
    tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"

### Notes

For more information on tap code, please see the resources section. The code
was widely used in WW2 as a way for prisoners to communicate.

"""

def tap_code(text):
  txt = text
  def l8rs_to_taps(l8rs):
​
    l8r_block = [['A', 'B', 'C', 'D', 'E'], 'F G H I J'.split(), 'L M N O P'.split(), 'Q R S T U'.split(), 'V W X Y Z'.split()]
​
    taps = []
​
    for l8r in l8rs:
      l8r = l8r.upper()
      if l8r == 'K':
        l8r = 'C'
      
      rownum = None
      colnum = None
​
      for n in range(0, len(l8r_block)):
        row = l8r_block[n]
        for num in range(0, 5):
          item = row[num]
          if item == l8r:
            rownum = n + 1
            colnum = num + 1
            break
      
      rowtap = ''
      coltap = ''
​
      for n in range(0, rownum):
        rowtap += '.'
      for n in range(0, colnum):
        coltap += '.'
      
      tap = rowtap + ' ' + coltap
​
      taps.append(tap)
    
    tr = ' '.join(taps)
​
    return tr
  def taps_to_l8rs(taps):
   
    taps = taps.split()
    
    idents = []
​
    for n in range(0, len(taps), 2):
      rowtapitem = taps[n]
      coltapitem = taps[n + 1]
​
      rownum = rowtapitem.count('.') - 1
      colnum = coltapitem.count('.') - 1 
​
      ident = '{r} {c}'.format(r = rownum, c = colnum)
​
      idents.append(ident)
    
    l8r_block = [['A', 'B', 'C', 'D', 'E'], 'F G H I J'.split(), 'L M N O P'.split(), 'Q R S T U'.split(), 'V W X Y Z'.split()]
​
    l8rs = []
​
    for ident in idents:
​
      i = ident.split()
      rowid = int(i[0])
      colid = int(i[1])
​
      l8r = l8r_block[rowid][colid]
​
      l8rs.append(l8r)
​
    return ''.join(l8rs).lower()
​
  tr = None
​
  if '.' in txt:
    tr = taps_to_l8rs(txt)
  else:
    tr = l8rs_to_taps(txt)
​
  return tr

