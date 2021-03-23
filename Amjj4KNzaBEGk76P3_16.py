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

def chemical_reactions(C,H,O):
  greater = max(H//2,O)
  if greater == H//2:
    H2O = O
    c_H = H-O*2
    c_O = 0
  else:
    H2O = H//2
    c_H = 0
    c_O = O - H//2
  grea = max(c_O//2,C)
  if grea == c_O//2:
    CO2 = C
    c_C = 0
  else:
    CO2 = c_O//2
    c_C = C - c_O//2
  gre = max(c_H//4,c_C)
  if gre == c_H//4:
    CH4 = c_C
  else:
    CH4 = c_H//4
  return list((H2O,CO2,CH4))

