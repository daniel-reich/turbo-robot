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

def resistor_code(colors):
    d = {'black': {'digit': 0, 'mag': 0}, 
         'brown': {'digit': 1, 'mag': 1, 'tol': '+/-1%', 'tcr': ' 100ppm/k'}, 
         'red': {'digit': 2, 'mag': 2, 'tol': '+/-2%', 'tcr': ' 50ppm/k'}, 
         'orange': {'digit': 3, 'mag': 3, 'tcr': ' 15ppm/k'}, 
         'yellow': {'digit': 4, 'mag': 4, 'tcr': ' 25ppm/k'}, 
         'green': {'digit': 5, 'mag': 5, 'tol': '+/-0.5%'}, 
         'blue': {'digit': 6, 'mag': 6, 'tol': '+/-0.25%', 'tcr': ' 10ppm/k'}, 
         'violet': {'digit': 7, 'mag': 7, 'tol': '+/-0.1%', 'tcr': ' 5ppm/k'}, 
         'gray': {'digit': 8, 'mag': 8, 'tol': '+/-0.05%'}, 
         'white': {'digit': 9, 'mag': 9}, 
         'gold': {'mag': -1, 'tol': '+/-5%'}, 
         'silver': {'mag': -2, 'tol': '+/-10%'}}
​
    coeff = d[colors.pop()]['tcr'] if len(colors) == 6 else ''
    res = int(''.join(str(d[col]['digit']) for col in colors[:-2])) * 10**d[colors[-2]]['mag']
    
    if res >= 10**9:
        res = str(res/10**9) + 'G'
    elif res >= 10**6:
        res = str(res/10**6) + 'M'
    elif res >= 10**3:
        res = str(res/10**3) + 'k'
    else:
        res = str(res)
        
    return '{}Ohm {}'.format(res.replace('.0', ''), d[colors.pop()]['tol']) + coeff

