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
  new=addr.split(",")
  new2=new[2].split(" ")
  new3=new[1].split(" ")
  if new3[len(new3)-1].isalpha():
    new4=" ".join(new3[len(new3)-2:])
  else:
    new4="".join(new3[-1])
  result=""
  result+=new2[1]
  result+=new2[2]
  for letter in new4:
    if letter.isdigit():
      result+=letter
    elif letter.isalpha():
      result+=letter.upper()
    else:
      result+="X"
  return result

