"""


Create a function that takes a string and returns **dashes** on both sides of
every vowel ( _a e i o u_ ).

### Examples

    dashed("Edabit") ➞ "-E-d-a-b-i-t"
    
    dashed("Carpe Diem") ➞ "C-a-rp-e- D-i--e-m"
    
    dashed("Fight for your right to party!") ➞ "F-i-ght f-o-r y-o--u-r r-i-ght t-o- p-a-rty!"

### Notes

  * A string can contain uppercase and lowercase vowels.
  *  **Y** is not considered a vowel.

"""

def dashed(txt):
    
    for i,element in enumerate(txt):
        
        if(i==0):
            if (element =="a" or element =="e" or element =="i" or element=="o" or element=="u"
                or element=="A" or element =="E" or element=="I" or element=="O" or element=="U"):
                text2 = "-"+element+"-"
            else:
                text2 = element
        else:
                if (element =="a" or element =="e" or element =="i" or element=="o" or element=="u"
                or element=="A" or element =="E" or element=="I" or element=="O" or element=="U"):
                    text2 = text2+"-"+element+"-"
                else:
                    text2 = text2+element
    
    print(text2)
    return(text2)

