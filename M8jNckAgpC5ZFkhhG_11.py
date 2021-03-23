"""


Create a function that finds the reverse complement of a ribonucleic acid
(RNA) strand. The RNA will be represented as a string containing only the
characters "A", "C", "G" and "U". Since RNA can only (canonically) allow
pairings of A/U and G/C, the complement of an RNA would be as follows:

Original| Complement  
---|---  
"AAA"| "UUU"  
"UUU"| "AAA"  
"GGG"| "CCC"  
"CCC"| "GGG"  
  
Your function should find the complement on the right **AND** also reverse the
resulting string.

### Examples

    reverse_complement("GUGU") ➞ "ACAC"
    
    reverse_complement("UCUCG") ➞ "CGAGA"
    
    reverse_complement("CAGGU") ➞ "ACCUG"

### Notes

You can assume all input seqeuences will be valid.

"""

def reverse_complement(input_sequence):
  revStr = ""
  for i in range(len(input_sequence)):
    if input_sequence[i] == "A":
      revStr = "U" + revStr
    elif input_sequence[i] == "U":
      revStr = "A" + revStr
    elif input_sequence[i] == "C":
      revStr = "G" + revStr
    else:
      revStr = "C" + revStr
  return revStr

