"""


Traveling through Europe one needs to pay attention to how the license plate
in the given country is displayed. When crossing the border you need to park
on the shoulder, unscrew the plate, re-group the characters according to the
local regulations, attach it back and proceed with the journey.

Create a solution that can format the _dmv number_ into a plate number with
correct grouping. The function input consists of a string `s` and group length
`n`. The output has to be upper case characters and digits. The new groups are
made from right to left and connected by `-`. The original order of the _dmv
number_ is preserved.

### Examples

    license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"
    
    license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"
    
    license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"
    
    license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"

### Notes

N/A

"""

def license_plate(s, n):
  t=s.upper().split('-')
  t=''.join(t)[::-1]
  out=[]
  
  while len(t)>0:
    out.append(t[:n])
    t=t[n:]
  
  return '-'.join(out)[::-1]
