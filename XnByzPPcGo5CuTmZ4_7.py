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
    import re
    l2 = addr.upper().split(', ')
    l3 = [l2[2].split(), l2[1].split()]
    l3[0].pop(-1)
    l3[1].pop(0)
    
    l4 = [l3[1][-1]]
    if not re.search('[0-9]', l3[1][-1]) and len(l3) > 1:
        l4 = [l3[1][-2], l3[1][-1]]
    s_out = ''.join(l3[0][:2])
    if l4[0].isnumeric():
        s_out += l4[0]
    else:
        s_out += re.sub('[^0-9,^A-Z,^a-z]', 'X', l4[0])
    for i in range(1, len(l4)):
        if l4[i].isnumeric():
            s_out += l4[i]
        else:
            s_out += 'X' + l4[i]
    return s_out

