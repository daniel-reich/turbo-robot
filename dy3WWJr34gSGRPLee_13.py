"""


Create a function that creates a box based on dimension `n`.

### Examples

    make_box(5) ➞ [
      "#####",
      "#   #",
      "#   #",
      "#   #",
      "#####"
    ]
    
    make_box(3) ➞ [
      "###",
      "# #",
      "###"
    ]
    
    make_box(2) ➞ [
      "##",
      "##"
    ]
    
    make_box(1) ➞ [
      "#"
    ]

### Notes

N/A

"""

def make_box(n):
    if n>=2:
        output=[]
        output.append('#'*n)
        mystring=''
        mystring=mystring+'#'+' '*(n-2)+'#'
        for i in range(n-2):
            output.append(mystring)
        output.append('#'*n)
        return output
    else: return ['#']

