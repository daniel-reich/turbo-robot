"""


Create a function that takes the volume of a cube and returns the length of
the cube's main diagonal, rounded to two decimal places.

### Examples

    cube_diagonal(8) ➞ 3.46
    
    cube_diagonal(343) ➞ 12.12
    
    cube_diagonal(1157.625) ➞ 18.19

#### Notes

Use the `sqrt` function in the math module.

"""

def cube_diagonal(vol):
  return round(vol**(1/3) * 3**.5, 2)

