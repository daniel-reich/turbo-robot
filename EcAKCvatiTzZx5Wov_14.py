"""


A resistor is a common electrical component found in every electronic circuit.
Usually a resistor has a color-based code (as painted bands over it) to
decipher through a table.

Color| Digits| Magnitude| Tolerance| T.C.R.  
---|---|---|---|---  
Black| 0| 0| -| -  
Brown| 1| 1| +/-1%| 100ppm/k  
Red| 2| 2| +/-2%| 50ppm/k  
Orange| 3| 3| -| 15ppm/k  
Yellow| 4| 4| -| 25ppm/k  
Green| 5| 5| +/-0.5%| -  
Blue| 6| 6| +/-0.25%| 10ppm/k  
Violet| 7| 7| +/-0.1%| 5ppm/k  
Gray| 8| 8| +/-0.05%| -  
White| 9| 9| -| -  
Gold| -| -1| +/-5%| -  
Silver| -| -2| +/-10%| -  
  
Starting from the left assign a number to each coloured band:

  *  **4 bands resistor:**
    * 1st and 2nd color: digits from column 1.
    * 3rd color: 10 elevated to the digit of column 2.
    * 4th color: tolerance from column 3.
  *  **5 bands resistor:**
    * 1st, 2nd and 3rd color: digits from column 1.
    * 4th color: 10 elevated to the digit of column 2.
    * 5th color: tolerance from column 3.
  *  **6 bands resistor:**
    * From 1st to 5th: as above.
    * 6th color: coefficient from column 4.

Then, when numbers have replaced colors:

  *  **Resistance** is equal to the number resulting by the union of digits from column 1 multiplied for the magnitude calculated from column 2: is measured in Ohms (symbol: **Ω** ). When Ohms are in the thousands order the notation is **kΩ** ( _kiloOhms_ ), in the millions order the notation is **MΩ** ( _MegaOhms_ ), in the billions order the notation is **GΩ** ( _GigaOhms_ ).
  *  **Tolerance** and **TCR** (temperature coefficient of resistance, only for 6-banded resistors) are the results of columns 3 and 4.

Given a list of colors you must return the resistor resistance, tolerance and
(eventually) the TCR as a string (with identifiers separated by spaces between
them).

### Examples

    resistor_code(["red", "yellow", "blue", "green"]) ➞ "24MOhm +/-0.5%"
    # red + yellow = 24; blue = 10^6, green = +/-0.5%
    # resistance * magnitude = 24000000 (24M)
    
    resistor_code(["white", "black", "white", "blue", "gold"]) ➞ "909MOhm+/-5%"
    # white + black + white = 909
    
    resistor_code(["black", "white", "black", "orange", "red", "yellow"]) ➞ "90kOhm +/-2% 25ppm/k"
    # black + white + black = 090 = 90; orange = 10^3
    # resistance * magnitude = 90000 (90k)

### Notes

  * For more info about resistors and their color codes check the **Resources** tab.
  * All given lists are valid, no exceptions to handle.

"""

from collections import namedtuple
ColorData = namedtuple('ColorData', ['digits', 'power', 'tolerance', 'tcr'])
​
colors = {
    'black' : ColorData( 0    ,  0, None      , None       ),
    'brown' : ColorData( 1    ,  1, '+/-1%'   , '100ppm/k' ),
    'red'   : ColorData( 2    ,  2, '+/-2%'   , '50ppm/k'  ),
    'orange': ColorData( 3    ,  3, None      , '15ppm/k'  ),
    'yellow': ColorData( 4    ,  4, None      , '25ppm/k'  ),
    'green' : ColorData( 5    ,  5, '+/-0.5%' , None       ),
    'blue'  : ColorData( 6    ,  6, '+/-0.25%', '10ppm/k'  ),
    'violet': ColorData( 7    ,  7, '+/-0.1%' , '5ppm/k'   ),
    'gray'  : ColorData( 8    ,  8, '+/-0.05%', None       ),
    'white' : ColorData( 9    ,  9, None      , None       ),
    'gold'  : ColorData( None , -1, '+/-5%'   , None       ),
    'silver': ColorData( None , -2, '+/-10%'  , None       ),
}
def combine_values(seq):
  codes, total = (d.digits for d in seq), 0
  for v in codes:
    total = total * 10 + v
  return total
​
def format_resistance(val):
  prefixes = ['Ohm', 'kOhm', 'MOhm', 'GOhm' ]
  if val % 1:
    return "{:g}Ohm".format(val)
  else:
    pIdx = 0
    while val >= 1000:
      val /= 1000
      pIdx += 1
    return "{:g}{:s}".format(val, prefixes[pIdx])
​
def resistor_code(seq):
  seq = [colors[elem] for elem in seq]
  digits, seq = (seq[:2], seq[2:]) if len(seq) < 5 else (seq[:3], seq[3:])
  digits = combine_values(digits)
  res = digits * (10 ** seq[0].power)
  res = format_resistance(res)
  tol = seq[1].tolerance
  tcr = seq[2].tcr if len(seq) > 2 else None
  return res + ' ' + tol + (' ' + tcr if tcr else '')

