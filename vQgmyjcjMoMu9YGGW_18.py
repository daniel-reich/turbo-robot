"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

def simplify(str_fraction):
    largest_devisor = 1
    fraction = str_fraction.split('/')
    for f in range(len(fraction)): fraction[f] = int(fraction[f])
    for devisor in range(1,fraction[0]+1):
        test = fraction[0]/devisor
        if(test == int(test)):  
            test = fraction[1]/devisor
            if(test == int(test)):  largest_devisor = devisor
    
    simp_fraction = []
    simp_fraction.append(int(fraction[0]/largest_devisor))
    simp_fraction.append(int(fraction[1]/largest_devisor))
​
    out_fraction = ""
    if(simp_fraction[1] == 1):
        out_fraction = out_fraction + str(simp_fraction[0])
    else:
        out_fraction = out_fraction + str(simp_fraction[0]) + "/" + str(simp_fraction[1])
    return(out_fraction)

