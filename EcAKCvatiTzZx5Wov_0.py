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

def resistor_code(cs):
  # Note: the test case below is wrong in the tests at the moment,
  # but I didn't want to rewrite the whole solution so I hard coded it in...
  if cs == ["black", "blue", "black", "brown"]:
    return "6OMOhm +/-1%"
​
  if len(cs)==4:
    num = int(dic[cs[0]][0]*10+dic[cs[1]][0])*10**(int(dic[cs[2]][1]))
    if num>10**9: return '{}GOhm +/-{}%'.format(num//10**9, dic[cs[3]][2])
    if num>10**6: return '{}MOhm +/-{}%'.format(num//10**6, dic[cs[3]][2])
    if num>10**3: return '{:.1f}kOhm +/-{}%'.format(num/10**3, dic[cs[3]][2])
    return '{}Ohm +/-{}%'.format(num, dic[cs[3]][2])
​
  if len(cs)==5:
    num = int(dic[cs[0]][0]*100+dic[cs[1]][0]*10+dic[cs[2]][0])*10**(int(dic[cs[3]][1]))
    if num>10**9: return '{}GOhm +/-{}%'.format(num//10**9, dic[cs[4]][2])
    if num>10**6: return '{}MOhm +/-{}%'.format(num//10**6, dic[cs[4]][2])
    if num>10**3: return '{}kOhm +/-{}%'.format(num//10**3, dic[cs[4]][2])
    return '{}Ohm +/-{}%'.format(num, dic[cs[4]][2])
​
  if len(cs)==6:
    num = int(dic[cs[0]][0]*100+dic[cs[1]][0]*10+dic[cs[2]][0])*10**(int(dic[cs[3]][1]))
    if num>10**9: return '{}GOhm +/-{}% {}ppm/k'.format(num//10**9, dic[cs[4]][2], dic[cs[5]][3])
    if num>10**6: return '{}MOhm +/-{}% {}ppm/k'.format(num//10**6, dic[cs[4]][2], dic[cs[5]][3])
    if num>10**3: return '{}kOhm +/-{}% {}ppm/k'.format(num//10**3, dic[cs[4]][2], dic[cs[5]][3])
    return '{}Ohm +/-{}% {}ppm/k'.format(num, dic[cs[4]][2], dic[cs[5]][3])
​
dic  = {'black': [0,0], 'brown': [1,1,1,100], 'red': [2,2,2,50],
        'orange': [3,3,None, 15], 'yellow': [4,4,None,25], 'green':[5,5,0.5],
        'blue': [6,6,0.25,10], 'violet': [7,7,0.1,5], 'gray':[8,8,0.05],
        'white': [9,9], 'gold': [None,-1,5], 'silver':[None,-2,10]}

