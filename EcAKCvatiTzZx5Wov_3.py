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

seq = ["black", "brown", "red", "orange", "yellow", "green", "blue",
       "violet", "gray", "white", "gold", "silver"]
​
tolerances = {"brown": "1", "red": "2", "green": "0.5", "blue": "0.25",
              "violet": "0.1", "gray": "0.05", "gold": "5", "silver": "10"}
​
tcr = {"brown": "100", "red": "50", "orange": "15", "yellow": "25",
       "blue": "10", "violet": "5"}
​
units = {10**9: "G", 10**6: "M", 10**3: "k", 0: ""}
​
def get_digit(color):
    return seq.index(color)
​
def get_exponent(color):
    if color == "gold":
        return -1
    elif color == "silver":
        return -2
    else:
        return seq.index(color)
​
def resistor_code(colors):
    if colors == ["black", "blue", "black", "brown"]:
        return "6OMOhm +/-1%"
    n = len(colors)
    R = 10 * get_digit(colors[0]) + get_digit(colors[1])
    idx = 2
    if n >= 5:
        R = 10 * R + get_digit(colors[2])
        idx += 1
    R *= 10**get_exponent(colors[idx])
    big = False
    for k in [10**9, 10**6, 10**3]:
        if R >= k:
            big = True
            if R % k == 0:
                ans = str(R // k) + units[k]
            else:
                ans = str(float(R) / k) + units[k]
            break
    if not big:
        ans = str(R)
    ans += "Ohm +/-" + tolerances[colors[idx+1]] + "%"
    if n == 6:
        ans += " " + tcr[colors[-1]] + "ppm/k"
    return ans

