"""


You will be given a string consisting of a list of integers and their
relationships to their neighboring integers. For instance:

    "-15<-10<=0=0<5"

Test to see that all the relationships between the integers in the string are
true. If they are, return `True`. If they are not, return `False`.

### Examples

    validate_relationships("5>-1<0=0<-5>5=5") ➞ False
    # This is False because 0 is not less than -5.
    
    validate_relationships("-15<-10<=0=0<5") ➞ True
    
    validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
    # This is False because 0 is not equal to 807.

### Notes

  * This is a modifcation of Helen Yu's "Correct Signs" challenge.
  * As the examples above show, there could be negative numbers in the string.
  * The numbers will only be separated by: `=, <, >, >=, <=`
  * Tests will not contain any spaces.

"""

def validate_relationships(txt):
    idx = 1
    while idx < len(txt) - 1:
        if (txt[idx] == '=' and txt[idx - 1].isdigit()
                and (txt[idx + 1].isdigit() or txt[idx + 1] == '-')):
            txt = txt[: idx] + '==' + txt[idx + 1:]
            idx += 1
        idx += 1
    return eval(txt)

