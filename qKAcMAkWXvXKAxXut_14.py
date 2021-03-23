"""


Lets assume for the purposes of this challenge that for every _layer of
fabric_ you wear when it's cold outside (coats, cardigans, etc), the
temperature increases by a _tenth of the total_.

Given `n` number of layers and a given temperature, return the temperature
inside of all those warm fuzzy layers. Round to the nearest _tenth_ of a
degree.

    calc_bundled_temp(2, "10*C") ➞ "12.1*C"
    # 10 * 1.1 = 11
    # 11 * 1.1 = 12.1

### Examples

    calc_bundled_temp(1, "2*C") ➞ "2.2*C"
    
    calc_bundled_temp(4, "6*C") ➞ "8.8*C"
    
    calc_bundled_temp(20, "4*C") ➞ "26.9*C"

### Notes

  * The temperature will be given in celsius and as a string.
  * Note that the degrees sign is given as an asterisk.

"""

#edabit
#bundle up
​
def calc_bundled_temp(n, temperature):
    lst = temperature.split('*')
    temp = int(lst[0])
    for i in range(1,n+1):
        temp += (0.1*temp)
    return '%s*C'%round(temp, 1)
​
def main():
    pass
​
if __name__ == "__main__":
    main()

