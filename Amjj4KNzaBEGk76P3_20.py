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

def chemical_reactions(c, h, o):
  h2o = min(h // 2, o)
  co2 = min(c, (o - h2o) // 2)
  ch4 = min(c - co2, (h - h2o * 2) // 4)
  return [h2o, co2, ch4]
