"""


Create a function that determines how many number pairs are there embedded in
a space-separated string. The first numeric value in the space-separated
string represents the count of the numbers, thus, excluded in the pairings.

### Examples

    number_pairs("7 1 2 1 2 1 3 2") ➞ 2
    # (1, 1), (2, 2)
    
    number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
    # (10, 10), (20, 20), (10, 10)
    
    number_pairs("4 2 3 4 1") ➞ 0
    # although two 4's are present but
    # the first one is discounted

### Notes

Always take into consideration the first number in the string is not part of
the pairing, thus, the count. It may not seem so useful as most people see it,
but it's mathematically significant if you deal with **set operations**.

"""

def number_pairs(txt):
    #Eliminate the first number
    #I take the string from the first space detected
    txt = txt[ str.find(txt, ' ') + 1 : ]
    
    #Spliting the str into numbers ex:("10", "10", "20", "10")
    my_elements = str.split(txt, ' ')
    
    #Transforme into a set to eliminate the double elements
    #Then retransforme it into list
    my_keys = my_elements
    my_keys = set(my_keys)
    my_keys = sorted(list(my_keys))
    
    #Counting every elements
    my_values = []
    for x in my_keys:
        list.append(my_values, list.count(my_elements, x))
​
    #Building y dictionnary (element : how many)
    #ex: {"10":2, "20":5}
    my_dictionnary = {}
    for x in range(len(my_keys)):
        my_dictionnary[my_keys[x]] = my_values[x]
    
    #Counting the numbers of pairs
    num_of_pairs = 0
    for x in my_dictionnary.values():
        num_of_pairs += int(x/2)
    
    return num_of_pairs

