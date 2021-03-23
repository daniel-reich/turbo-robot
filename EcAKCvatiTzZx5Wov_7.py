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

def string(n: float):
  if int(n) == n:
    return str(int(n))
  else:
    return str(n)
​
def resistor_code(col: list):
​
  dm_code = {
      "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
      "blue": 6, "violet": 7, "gray": 8, "white": 9, "gold": -1, "silver": -2
  }
  tl_code = {
      "brown": '1', "red": '2', "green": '0.5', "blue": '0.25', "violet": '0.1', 
      "gray": '0.05', "gold": '5', "silver": '10'
  }
  tcr_code = {
      "brown": '100', "red": '50', "orange": '15', "yellow": '25', "blue": '10', 
      "violet": '5'
  }
  if len(col) == 4:
    resistance = (dm_code[col[0]] * 10 + dm_code[col[1]]) * 10 ** dm_code[col[2]]
    tolerance = " +/-" + tl_code[col[3]] + "%" 
  else:
    resistance = (dm_code[col[0]] * 100 + dm_code[col[1]] * 10 + dm_code[col[2]]) * 10 ** dm_code[col[3]]
    tolerance = " +/-" + tl_code[col[4]] + "%" 
  if resistance // 10 ** 9:
    resistance = string(resistance / 10 ** 9) + "GOhm"
  elif resistance // 10 ** 6:
    resistance = string(resistance / (10 ** 6)) + "MOhm"
  elif resistance // 10 ** 3:
    resistance = string(resistance / 10 ** 3) + "kOhm"
  else:
    resistance = string(resistance) + "Ohm"
  
  if len(col) == 6:
    tcr = " " + tcr_code[col[5]] + "ppm/k"
  else:
    tcr = ""
​
  return resistance + tolerance + tcr

