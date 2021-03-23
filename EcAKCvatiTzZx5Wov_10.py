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

import re
colorz = ["black","brown","red","orange","yellow","green","blue","violet","gray","white","gold","silver"]
tolerance = dict(zip(colorz,[None,1,2,None,None,0.5,0.25,0.1,0.05,None,5,10]))
tcr = dict(zip(colorz,([None,100,50,15,25,None,10,5,None,None,None,None])))
class Color:
  def __init__(self,color):
    self.color = color
    self.digit = colorz.index(color)
    self.tol = "+/-" + str(tolerance[self.color]) + "%"
    self.tc = str(tcr[self.color]) + "ppm/k"
  def magnitude(self):
    return 0.1 if self.color == "gold" else 0.01 if self.color == "silver" else pow(10,self.digit)
class Resistance:
  def __init__(self):
    self.label = ""
    self.n = None
  def update_info(self,n):
    if n < 1000:
      self.n = n
    elif n < 1000000:
      self.label = "k"
      self.n =  n/1000
    elif n < 1000000000:
      self.label = "M"
      self.n = n/1000000
    else:
      self.label = "G"
      self.n = n/1000000000
  def string(self):
    s = str(self.n)
    if s.endswith(".0"):
      s = s[:-2]
    elif s.endswith("0") and "." in s:
      s = re.sub(r'0+$','',s)
    return "{}{}Ohm".format(s,self.label)
def resistor_code(colors):
  bands = [Color(x) for x in colors]
  res = str(bands[0].digit) + str(bands[1].digit)
  if len(bands) > 4:
    res += str(bands[2].digit)
  res = int(res)
  def mag():
    return 2 if len(bands) == 4 else 3
  res *= bands[mag()].magnitude()
  def toler():
    return 3 if len(bands) == 4 else 4
  resistance = Resistance()
  resistance.update_info(res)
  s = "{} {}".format(resistance.string(),bands[toler()].tol)
  if len(bands) == 6:
    s += " " + bands[-1].tc
  return s

