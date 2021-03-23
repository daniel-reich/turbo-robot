"""


Create a function that takes a list of `resistors` and calculates the output
of total resistance if the circuit is connected in **parallel** or in
**series**.

### Examples

    resistance_calculator([10, 20, 30, 40, 50]) ➞ [4.38, 150]
    
    resistance_calculator([25, 14, 65, 18]) ➞ [5.48, 122]
    
    resistance_calculator([10, 10]) ➞ [5, 20]
    
    resistance_calculator([0, 0, 0, 0]) ➞ [0, 0]
    
    resistance_calculator([1.1, 2.1, 3.2, 4.3, 5.4, 6.5]) ➞ [0.44, 22.6]

### Notes

  * Return parallel resistance as the first element and series resistance as second element of the list.
  * Round up the total resistance to two decimal places.

"""

def resistance_calculator(resistors):
  
  Top_Part_01 = 1
  Top_Part_02 = 0
  Bottom = 0
   
  Counter = 0
  Length = len(resistors)
  
  if (Length == 2):
        
    Parallel = (resistors[0] * resistors[1]) / (resistors[0] + resistors[1])
    Parallel = round(Parallel,2)
    Series = sum(resistors)
    Series = round(Series,2)
    
    Answer = []
    Answer.append(Parallel)
    Answer.append(Series)
  
    return Answer
  
​
  else:
    
    while (Counter < Length):
            
      Item = resistors[Counter]
            
      if (Item == 0):
        Value = 0
        Top_Part_02 += Value
        Bottom += Item
                        
      else:
        Value = 1 / Item
        Top_Part_02 += Value
        Bottom += Item      
            
      Counter += 1
            
    if (Top_Part_02 == 0):
      Parallel = 0
​
    else:
      Parallel = round(Top_Part_01 / Top_Part_02,2)
        
    Series = sum(resistors)
    Series = round(Series,2)
  
    Answer = []
    Answer.append(Parallel)
    Answer.append(Series)
  
    return Answer

