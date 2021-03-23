"""


In The Netherlands we have PostNL, the postal company. They use KixCodes, a
fast way to deliver letters and packages that can be scanned during the
process.

![Kix Code](https://edabit-challenges.s3.amazonaws.com/KIX-code-van-
PostNL_tcm10-8633.gif)

The code is a combination of: "Postal code", "House/box/call number" and
"House appendage / suffix"

If there is a character between the house number and the suffix, we need to
replace that with an X. Eventually, the code will be printed in the KixCode
font.

### Examples

    kix_code("PostNL, Postbus 30250, 2500 GG 's Gravenhage") ➞ "2500GG30250"
    
    kix_code("Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk") ➞ "1657KA11X1"
    
    kix_code("Dijk, Antwoordnummer 80430, 2130 VA Hoofddorp") ➞ "2130VA80430"

### Notes

  * Your function will get an address line (string) separated by comma's.
  * The input format will always be the same.
  * Watch out for the different suffixes!

"""

import re
​
def kix_code(addr):
  data = re.search(r'''
          (\d+\w)         # House
          (?:[ -/](\w{,2}))?,\s # Suffix
          (\d{4})\s       # Postal code p.1
          (\w{2})         # Postal code p.2
          ''', addr, re.X)
          
  house, suf, postal, code = map(lambda x: str(x).upper(), data.groups(0))
  return postal + code + house + ('', 'X' + suf)[suf != '0']

