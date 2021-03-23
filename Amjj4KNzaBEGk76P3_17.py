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

def chemical_reactions(carbon, hydrogen, oxygen):
  ## assign temp variables
  temp_hydrogen = hydrogen
  temp_oxygen = oxygen
  temp_carbon = carbon
  total_h20 = 0
  total_c02 = 0
  total_ch4 = 0
  while temp_hydrogen >= 2 and temp_oxygen >= 1:
    temp_hydrogen -= 2
    temp_oxygen -= 1
    total_h20 += 1
  while temp_carbon >= 1 and temp_oxygen >= 2:
    temp_oxygen -= 2
    temp_carbon -= 1
    total_c02 += 1
  while temp_carbon >= 1 and temp_hydrogen >= 4:
    temp_carbon -= 1
    temp_hydrogen -= 4
    total_ch4 += 1
  return [total_h20,total_c02,total_ch4]

