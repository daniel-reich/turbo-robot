"""


Create a function that takes a string containing both name and number of
animals and plants that may or may not be found in Chitwan National Park. The
function should return a list of tuples where first element in the tuple is
animal name and second element in the tuple is number of that particular
animal that is found in Chitwan National Park.

### Animals Present in Chitwan National Park

    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

### Examples

    fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
    # Mango not present in animal list.
    
    fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
    # Apples not present in animal list.

### Notes

  * Input contains name and number of both animals and plants.
  * If there is no match, return an empty list.

"""

def fauna_number(txt):
    #iterate through list <animals> and check if animal exists in list <txt>
    #if animal exists, store animal in list <exists>
    #sort list <exists> based on order of appearance in string <txt>
    #for each animal in exists
    #get starting index of animal in string
    #iterate through the string backwards from index - 2 until not digit
    #add 1 to start and end to adjust
    #store animal and number in tuple and append to list <result>
​
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    result = []
    exists = []
    for animal in animals:
        if animal in txt:
            exists.append(animal)
    exists.sort(key=txt.index)
    for animal in exists:
        end = txt.index(animal) - 2
        start = end
        while txt[start].isdigit():
            start -= 1
        result.append((animal, txt[start + 1: end + 1]))
    return result

