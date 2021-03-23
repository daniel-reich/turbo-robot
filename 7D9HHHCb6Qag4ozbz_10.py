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
  if txt.count("zip")>1:
    a=txt.find("zip")
    b=txt.find("zip",a+1)
    return b
  else: return -1
