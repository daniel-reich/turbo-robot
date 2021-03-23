"""


Write a function that returns the **position** of the **second occurrence** of
"zip" in a string, or **-1** if it does not occur at least twice. Your code
should be general enough to pass every possible case where "zip" can occur in
a string.

### Examples

    find_zip("all zip files are zipped") ➞ 18
    
    find_zip("all zip files are compressed") ➞ -1

### Notes

Uppercase "Zip" is not the same as lowercase "zip".

"""

def find_zip(txt):
  if txt.count("zip") ==1:
    return -1
  for i in range(len(txt)-1,0, -1):
    if txt[i] =='p' and txt[i-1] =='i' and txt[i-2] =='z':
      return i-2

