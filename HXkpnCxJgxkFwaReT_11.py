"""


Given a function that accepts **unlimited** arguments, check and count how
many data types are in those arguments. Finally return the total in a list.

List order is:

    [int, str, bool, list, tuple, dictionary]

### Examples

    count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
    
    count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
    
    count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
    
    count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]

### Notes

If no arguments are given, return `[0, 0, 0, 0, 0, 0]`

"""

def count_datatypes(*args):
 x=[0,0,0,0,0,0]
 for i in args:
  if type(i)==int:
   x[0]=x[0]+1
  elif type(i)==str:
   x[1]=x[1]+1
  elif type(i)==bool:
   x[2]=x[2]+1
  elif type(i)==list:
   x[3]=x[3]+1
  elif type(i)==tuple:
   x[4]=x[4]+1
  elif type(i)==dict:
   x[5]=x[5]+1
 return x

