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

class Resistor:
​
  d = {'black': {'Digits': 0, 'Mag': 0, 'Tol': None, 'TCR': None},  'brown': {'Digits': 1, 'Mag': 1, 'Tol': .01, 'TCR': 100},  'red': {'Digits': 2, 'Mag': 2, 'Tol': .02, 'TCR': 50},  'orange': {'Digits': 3, 'Mag': 3, 'Tol': None, 'TCR': 15},  'yellow': {'Digits': 4, 'Mag': 4, 'Tol': None, 'TCR': 25},  'green': {'Digits': 5, 'Mag': 5, 'Tol': .005, 'TCR': None},  'blue': {'Digits': 6, 'Mag': 6, 'Tol': .0025, 'TCR': 10},  'violet': {'Digits': 7, 'Mag': 7, 'Tol': .001, 'TCR': 5},  'gray': {'Digits': 8, 'Mag': 8, 'Tol': .0005, 'TCR': None},  'white': {'Digits': 9, 'Mag': 9, 'Tol': None, 'TCR': None},  'gold': {'Digits': None, 'Mag': -1, 'Tol': .05, 'TCR': None},  'silver': {'Digits': None, 'Mag': -2, 'Tol': .1, 'TCR': None}}
​
  band4 = lambda b: '{} +/-{}%'.format(float(''.join([str(Resistor.d[color]['Digits']) for color in [b[0], b[1]]])) * (10 ** Resistor.d[b[2]]['Mag']), Resistor.d[b[3]]['Tol'] * 100) 
  band5 = lambda b: '{} +/-{}%'.format(float(''.join(str(Resistor.d[color]['Digits']) for color in [b[0], b[1], b[2]])) * (10 ** Resistor.d[b[3]]['Mag']), Resistor.d[b[4]]['Tol'] * 100)
  band6 = lambda b: '{} +/-{}% {}ppm/k'.format(float(''.join(str(Resistor.d[color]['Digits']) for color in [b[0], b[1], b[2]])) * (10 ** Resistor.d[b[3]]['Mag']), Resistor.d[b[4]]['Tol'] * 100, Resistor.d[b[5]]['TCR'])
​
  def ohmify(string):
    ohms = float(string.split()[0])
#    print(ohms, ohms / 1000000 == ohms // 1000000)
​
    end = 'Ohm'
    if ohms < 1000:
      ohms = round(ohms / 1, 1) if ohms // 1 != ohms / 1 else int(ohms)
    elif 1000 <= ohms < 1000000:
      ohms = round(ohms / 1000, 1) if ohms // 1000 != ohms / 1000 else int(ohms // 1000)
      end = 'k' + end
    elif 1000000 <= ohms < 1000000000:
      ohms = round(ohms / 1000000, 1) if ohms // 1000000 != ohms / 1000000 else int(ohms // 1000000)
      end = 'M' + end
    else:
      ohms = round(ohms / 1000000000, 1)if ohms // 1000000000 != ohms / 1000000000 else int(ohms // 1000000000)
      end = 'G' + end
    
    return ' '.join(['{}{}'.format(ohms, end)] + string.split()[1:])
​
  def percentify(string):
    percent = string.split()[1].replace('+/-', '').replace('%', '')
    if percent[-1] != '0' or '.' not in percent:
      return string
    else:
      return string.replace(string.split()[1], '+/-{}%'.format(int(float(percent))))
​
​
  def __init__(self, raw):
​
    self.first_band = raw[0]
    self.second_band = raw[1]
    self.third_band = raw[2]
    self.fourth_band = raw[3]
    
    if len(raw) >= 5:
      self.fifth_band = raw[4]
    else:
      self.fifth_band = None
    
    if len(raw) == 6:
      self.sixth_band = raw[5]
    else:
      self.sixth_band = None
    
    self.num_of_bands = len(raw)
  
  def __str__(self):
​
    if self.num_of_bands == 4:
      raw = Resistor.band4([self.first_band, self.second_band, self.third_band, self.fourth_band])
    elif self.num_of_bands == 5:
      raw = Resistor.band5([self.first_band, self.second_band, self.third_band, self.fourth_band, self.fifth_band])
    else:
      raw = Resistor.band6([self.first_band, self.second_band, self.third_band, self.fourth_band, self.fifth_band, self.sixth_band])
    
    return Resistor.percentify(Resistor.ohmify(raw))
​
resistor_code = lambda colors: str(Resistor(colors))

