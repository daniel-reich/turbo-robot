"""


Create a function that takes in a list of integers and returns the number of
even or odd digits for each number, depending on the parameter.

### Examples

    count_digits([22, 53, 99, 61, 777, 8], "odd") ➞ [0, 2, 2, 1, 3, 0]
    
    count_digits([22, 53, 99, 61, 777, 8], "even") ➞ [2, 0, 0, 1, 0, 1]
    
    count_digits([54, 113, 89, 10], "odd") ➞ [1, 3, 1, 1]
    
    count_digits([54, 113, 89, 10], "even") ➞ [1, 0, 1, 1]

### Notes

N/A

"""

def count_digits(lst, t):
    lista = []
    listeven= []
    listodd = []
    nlisteven = []
    nlistodd = []
    for num in lst:
        lista.append(list(str(num)))
    for l in lista:
        listeven.append([1 for n in l if int(n) % 2 == 0])
        listodd.append([1 for n in l if int(n) % 2 == 1])
    for li in listeven:
        nlisteven.append(sum(li))
    for li in listodd:
        nlistodd.append(sum(li))
    if t == "even":
        return nlisteven
    return nlistodd

