"""


Create a function that takes an integer and returns it as an **ordinal
number**. An Ordinal Number is a number that tells the position of something
in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

### Examples

    return_end_of_number(553) ➞ "553-RD"
    
    return_end_of_number(34) ➞ "34-TH"
    
    return_end_of_number(1231) ➞ "1231-ST"
    
    return_end_of_number(22) ➞ "22-ND"
    
    return_end_of_number(412) ➞ "412-TH"

### Notes

Check the **Resources** tab for more info on _ordinal numbers_.

"""

suffix = {'1': '-ST', '2': '-ND', '3': '-RD'}
def return_end_of_number(num):
    str_num = str(num)
    if len(str_num) > 1 and str_num[-2] == '1' or str_num[-1] not in suffix:
        return '{}-TH'.format(str_num)
    return '{}{}'.format(str_num, suffix[str_num[-1]])

