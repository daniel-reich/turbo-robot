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

def convertion(nombre):
   taille = len(str(int(nombre)))
   val = 0
   if taille >= 4 and taille <= 6 :
     if nombre % 1000 != 0:
          val = nombre /1000.0
     else:
        val = nombre // 1000
     string=str(val)+"kOhm"
     return string
   elif taille >=7 and taille <=  9 :
     if nombre % 1000000 !=0:
         val =nombre / 1000000.0
     else :
        val = nombre // 1000000
     string =str(val)+ "MOhm"
     return string
   elif taille >= 10:
     if nombre % 1000000000 !=0:
          val = nombre / 1000000000.0
     else:
        val = nombre // 1000000000
     string =str(val) +"GOhm"
     return string
   else:
     return str(nombre)+'Ohm'
def resistor_code(colors):
      dic ={'black':["0","0","0","0"],
"brown":["1","1","+/-1%","100ppm/k"],
"red" :["2","2","+/-2%","50ppm/k"],
"orange":["3","3","-","15ppm/k"],
"yellow":["4","4","-","25ppm/k"],
"green":["5","5","+/-0.5%", "0"],
"blue": ["6","6","+/-0.25%","10ppm/k"],
"violet":["7","7","+/-0.1%","5ppm/k"],
"gray": ["8","8","+/-0.05%","0"],
"white":["9","9","0","0"],
"gold": ["0", "-1", "+/-5%",  "0"],
"silver": ["0","-2","+/-10%","0"]}
      taille = len(colors)
      if taille == 4 :
           a = int(dic[colors[0]][1]+dic[colors[1]][1])
           b= 10**int(dic[colors[2]][1])
           nombre =a*b
           c=convertion(nombre)
           retour  = c + ' ' + dic[colors[3]][2]
           return  retour
      elif taille == 5:
          a = int(dic[colors[0]][1]+dic[colors[1]][1]+dic[colors[2]][1])
          b=10**int(dic[colors[3]][1])
          c=convertion(a*b)
          retour = c +" " + dic[colors[4]][2]
          return retour
      else :
         a = int(dic[colors[0]][1]+dic[colors[1]][1]+dic[colors[2]][1])
         b=10**int(dic[colors[3]][1])
         c=convertion(a*b)
         retour = c + " " +  dic[colors[4]][2] + " " + dic[colors[5]][3]
         return retour

