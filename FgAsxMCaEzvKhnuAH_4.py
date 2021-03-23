"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

def str_split_num(string):
    left = 0
    right = 0
    result = []
    while right < len(string):
        if right < len(string) - 1:
            if not string[left].isdigit():
                left += 1
                right += 1
            elif string[left].isdigit() and string[right].isdigit():
                right += 1
            elif string[left].isdigit() and not string[right].isdigit():
                if left - 1 >=0 and string[left-1] != "-":
                   result.append(int(string[left:right]))
                elif left - 1 >=0 and string[left-1] == "-":
                    result.append(int(string[left:right]) * -1)
                elif left - 1 < 0:
                    result.append(int(string[left:right]))
                left = right
        elif right == len(string) - 1:
            if not string[left].isdigit() and string[right].isdigit():
                if string[left] == "-":
                    result.append(int(string[right]) *-1)
                elif string[left] != "-":
                    result.append(int(string[right]))
                break
            elif string[left].isdigit() and not string[right].isdigit():
                if left -1 >= 0 and string[left-1] != "-":
                    result.append(int(string[left:right]))
                if left - 1 >= 0 and string[left - 1] == "-":
                    result.append(int(string[left:right]) * -1)
                if left - 1 < 0:
                    result.append(int(string[left:right]))
                break
            elif string[left].isdigit() and string[right].isdigit():
                if left - 1 >= 0 and string[left - 1] != "-":
                   result.append(int(string[left:right + 1]))
                elif left - 1 >= 0 and string[left - 1] == "-":
                    result.append(int(string[left:right + 1])*-1)
                elif left - 1 < 0:
                    result.append(int(string[left:right + 1]))
                break
            elif not string[left].isdigit() and not string[right].isdigit():
                break
    return result
​
def deep_sum(lst):
    sum_lst = 0
    if all(type(item) != list for item in lst):
        for item in lst:
            sum_lst += sum(str_split_num(item))
        return sum_lst
    for item in lst:
        if type(item) == list:
            sum_lst += deep_sum(item)
        elif type(item) != list:
           sum_lst += sum(str_split_num(item))
    return sum_lst

