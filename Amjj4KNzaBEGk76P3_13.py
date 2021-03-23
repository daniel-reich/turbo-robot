"""


 **Mubashir** was testing how atoms can react in their ionic state during
nuclear fusion. He observed that atoms can introduce different elements with
Hydrogen at high temperatures and inside a pressurized chamber. During his
experiment, elements started precipitating inside the chamber. Help him find
the total number of molecules of Water **H2O** , Carbon Dioxide **CO2** and
Methane **CH4** generated during this process.

Given the number of atoms of `carbon`, `hydrogen` and `oxygen`, calculate the
**molecules** in the following order:

    1. Hydrogen reacts with Oxygen = H2O
    2. Carbon reacts with Oxygen   = CO2
    3. Carbon reacts with Hydrogen = CH4

### Examples

    chemical_reactions(45, 11, 100) ➞ [5, 45, 0]
    # 10 atoms of hydrogen + 5 atoms of oxygen = 5 molecules of H2O
    # 45 atoms of carbon + 90 atoms of oxygen = 45 molecules of CO2
    # 1 hydrogen atom + 0 carbon atoms = 0 molecules of CH4
    
    chemical_reactions(113, 0, 52) ➞ [0, 26, 0]
    
    chemical_reactions(939, 3, 694) ➞ [1, 346, 0]

### Notes

N/A

"""

class H2O:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(hydrogen, oxygen):
    if hydrogen < 2 or oxygen < 1:
      return False
    else:
      hydrogen -= 2
      oxygen -= 1
      
      return H2O(['H', 'H', 'O']), hydrogen, oxygen
class CO2:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(carbon, oxygen):
    if carbon < 1 or oxygen < 2:
      return False
    else:
      carbon -= 1
      oxygen -= 2
      
      return CO2(['C', 'C', 'O']), carbon, oxygen
class CH4:
  
  def __init__(self, chemicals = []):
    self.chemicals = chemicals
  
  def generate(carbon, hydrogen):
    if carbon < 1 or hydrogen < 4:
      return False
    else:
      carbon -= 1
      hydrogen -= 4
      
      return CH4(['C', 'H', 'H', 'H', 'H']), carbon, hydrogen
​
def chemical_reactions(carbon, hydrogen, oxygen):
  
  water = []
  carbon_dioxide = []
  methane = []
  
  water_possible = True
  carbon_dioxide_possible = True
  methane_possible = True
  
  while water_possible == True:
    wp = H2O.generate(hydrogen, oxygen)
    print(hydrogen, oxygen)
    if wp == False:
      water_possible = False
    else:
      water.append(wp[0])
      hydrogen = wp[1]
      oxygen = wp[2]
  
  while carbon_dioxide_possible == True:
    cdp = CO2.generate(carbon, oxygen)
    if cdp == False:
      carbon_dioxide_possible = False
    else:
      carbon_dioxide.append(cdp[0])
      carbon = cdp[1]
      oxygen = cdp[2]
  
  while methane_possible == True:
    mp = CH4.generate(carbon, hydrogen)
    if mp == False:
      methane_possible = False
    else:
      methane.append(mp[0])
      carbon = mp[1]
      hydrogen = mp[2]
  
  return [len(water), len(carbon_dioxide), len(methane)]

