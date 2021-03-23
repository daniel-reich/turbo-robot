"""


Create a function that takes a string representing a fraction, and return a
string representing that input as a mixed number.

  * Mixed numbers are of the form `1 2/3` — note the space between the whole number portion and the fraction portion.
  * Resulting fractions should be fully reduced (see example #2).
  * If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
  * If a result is only fractional with no whole number, return only the fractional portion (see example #4).
  * If a result is negative, the whole number should carry the negative sign. If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).

### Examples

    mixed_number("5/4") ➞ "1 1/4"
    
    mixed_number("6/4") ➞ "1 1/2"
    
    mixed_number("8/4") ➞ "2"
    
    mixed_number("4/6") ➞ "2/3"
    
    mixed_number("-1/4") ➞ "-1/4"
    
    mixed_number("-5/4") ➞ "-1 1/4"
    
    mixed_number("-8/4") ➞ "-2"

### Notes

All provided inputs will be formatted similarly, negative numbers will be
provided in the numerator portion only, and all inputs will contain no spaces,
invalid characters, or zero denominators.

"""

import math
​
def mixed_number(frac):
  
  ############################################################
  #   PRECURSORY STEP
  #   Making Sure frac is String
  ############################################################
    
  Text = str(frac) 
​
  ############################################################
  #   PART A
  #   Establishing if Minus Sign will be required
  ############################################################
​
  Status = frac[0]
​
  if (Status == "-"):
    Part_A = "-"
​
  else:
    Part_A = ""    
​
  ############################################################
  #   PART B
  #   Establishing if Fraction is Above One
  ############################################################
​
  # Finding Location of Slash    
    
  Slash = Text.rindex("/")
  After = Slash + 1
​
  # Extracting Text Either Side of Slash
  Upper = Text[:Slash]
  Lower = Text[After:]
​
  # Converting Upper and Lower to Numbers
  Top = abs(int(Upper))
  Bottom = int(Lower)
​
  Value = Top/Bottom
  Whole = math.floor(Value)
  
  Remainder = Top % Bottom
  
  if (Value == 0):
    Part_B = "0"
  elif (Whole == 0):
    Part_B = ""
  elif (Whole > 0) and (Remainder > 0):
    Part_B = str(Whole) + " "
  else:
    Part_B = str(Whole)
​
  ############################################################
  #   PARTS C AND D
  #   Establishing if Fraction is Above One
  ############################################################
​
  # Simplifying Fraction Alongside Whole Number
  
  Remainder = Top % Bottom
  Factor_Count = 1
  Highest_Common = 1
​
  while (Factor_Count <= Remainder):
    
    if (Remainder % Factor_Count == 0) and (Bottom % Factor_Count == 0):
      Highest_Common = int(Factor_Count)
      Factor_Count += 1
    else:
      Factor_Count += 1
​
  Top /= Highest_Common
  Bottom /= Highest_Common
​
  Remainder = Top % Bottom
​
  if (Remainder == 0):
    Part_C = ""
    Part_D = ""
   
  else:
    Part_C = str(int(Remainder))
    Part_D = str(int(Bottom))
​
  ############################################################
  #   BUILDING SENTENCE
  ############################################################
​
  if (Part_C == "") and (Part_D == ""):
    Sentence = Part_A + Part_B
    return Sentence
    
  else:
    Sentence = Part_A + Part_B + Part_C + "/" + Part_D
    return Sentence

