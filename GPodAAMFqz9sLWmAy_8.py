"""


Given a **two digit** number, return `True` if that number contains **one
even** and **one odd** digit.

### Examples

    one_odd_one_even(12) ➞ True
    
    one_odd_one_even(55) ➞ False
    
    one_odd_one_even(22) ➞ False

### Notes

N/A

"""

#edabit
#odd_even
​
def one_odd_one_even(num):
    num_string = str(num)
    int_1 = int(num_string[0])
    int_2 = int(num_string[-1])
    if (int_1 % 2 == 0 and int_2 % 2 != 0) or (int_1 % 2 != 0 and int_2 % 2 == 0):
        return True
    else:
        return False
​
def main():
    pass
​
if __name__ == "__main__":
    main()

