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
  
  class Circuit:
    class Resistor:
      
      def __init__(self, volt):
        self.v = volt
    
    def __init__(self, resistors):
      self.raw = resistors
      self.resistors = []
      
      for r in self.raw:
        self.resistors.append(Circuit.Resistor(r))
    
    def in_series(self):
      return round(sum([r.v for r in self.resistors]),2)
    
    def in_parrallel(self):
      try:
        return round(1/(sum([(1/r.v) for r in self.resistors])), 2)
      except ZeroDivisionError:
        return 0
  
  circuit = Circuit(resistors)
  
  series = circuit.in_series()
  parrallel = circuit.in_parrallel()
  
  return [parrallel, series]

