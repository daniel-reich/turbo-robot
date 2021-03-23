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

def kix_code(addr):
​
  address = addr.split(',')
​
  second_part = address[1].split()
  third_part = address[2].split()
​
  post_code = third_part[:2]
  
  startn = None
  for n in reversed(range(0, len(second_part))):
    item = second_part[n]
    try:
      i = int(item)
      startn = n
      break
    except ValueError:
      if '-' in item:
        item = item.split('-')
        try:
          i = int(item[0])
          startn = n
          break
        except ValueError:
​
          continue
      else:
        continue#
  if startn == None:
    house_num = second_part[-1]
  else:
    house_num = 'X'.join(second_part[startn:]).replace('-','X')
​
  pc = ''
​
  for item in post_code:
    pc += item 
​
  tr = pc + house_num
​
  return tr.upper().replace('/', 'X')

