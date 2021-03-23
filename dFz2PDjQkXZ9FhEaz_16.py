"""


Create a function that accepts a list of two strings and checks if the letters
in the second string are present in the first string.

### Examples

    letter_check(["trances", "nectar"]) ➞ True
    
    letter_check(["compadres", "DRAPES"]) ➞ True
    
    letter_check(["parses", "parsecs"]) ➞ False

### Notes

  * Function should not be case sensitive (as indicated in the second example).
  * Both strings are presented as a single argument in the form of a list.
  *  **Bonus:** Solve this without RegEx.

"""

def letter_check(lst):
    for i in range (len(lst)):
        if i==1:
            STRING2 = lst[1]
            STRING1 = lst[0]
            for elem in STRING2:
                if elem not in STRING1 and elem not in STRING1.lower():
                    print('NO')
                    return False
    print("YES")
    return True

