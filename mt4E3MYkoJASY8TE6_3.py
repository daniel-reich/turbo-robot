"""


Given a keypad that has the following layout:

    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘

Your secret agent **Mubashir** has already given you a pincode. However, he
also said it's possible that each of the digits he saw could be another
adjacent digit (horizontally or vertically, but not diagonally).

Suppose the secret agent has given you the code: **46** :

    # Instead of the 4 it could also be 1, 5, or 7.
    # Instead of the 6 it could also be 3, 5, or 9.
    
    crack_pincode("46") ➞
    ["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]

Create a function that takes an argument of `pincode` informed by your secret
agent and returns a list of **all possible variations** of the pin codes.

### Examples

    crack_pincode("0") ➞ ["0", "8"]
    
    crack_pincode("2") ➞ ["1", "2", "3", "5"]
    
    crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]

### Notes

All pin codes must be strings, because of potentially leading `0`s.

"""

def combo_list_of_string(lst_of_strs):
    if len(lst_of_strs) == 0:
        return ['']
    result = []
    for i in range(0, len(lst_of_strs)):
        for j in range(len(lst_of_strs[i])):
            to_add_letter = lst_of_strs[i][j]
            remain_lst_of_strs = lst_of_strs[i + 1:]
            for string in combo_list_of_string(remain_lst_of_strs):
                if len(string) == len(lst_of_strs) - 1:
                    result.append(to_add_letter + string)
    return result
​
def crack_pincode(pincode):
    adj_dct = {"1": "124", "2": "1235", "3": "236", "4": "1475",
               "5": "24568", "6": "3569", "7": "478", "8": "57890",
               "9": "689", "0": "80"}
    if len(pincode) == 0:
        return []
    lst_of_strs = []
    for i in range(len(pincode)):
        lst_of_strs.append(list(adj_dct[pincode[i]]))
    print(lst_of_strs)
    return sorted(combo_list_of_string(lst_of_strs))

