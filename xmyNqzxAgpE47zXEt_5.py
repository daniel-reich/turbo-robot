"""


A word is alphabetically sorted if all of the letters in it are in consecutive
alphabetical order. Some examples of alphabetically sorted words: _abhors_ (
_a_ is before _b_ , _b_ is before _h_ , _h_ is before _o_ , etc.), _ghost_ ,
_accent_ , _hoop_.

Create a function that takes in a sentence as input and returns `True` if
there is **at least one** alphabetically sorted word inside that has a
**minimum length of 3**.

### Examples

    is_alphabetically_sorted("Paula has a French accent.") ➞ True
    # "accent" is alphabetically sorted.
    
    is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
    # "biopsy" is alphabetically sorted.
    
    is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
    # Although "by" is alphabetically sorted, it is only 2 letters long.

### Notes

  * Do not count words with 2 or fewer characters.
  * Ignore punctuation (periods, commas, etc).

"""

def is_alphabetically_sorted(sentence):
    sentence = sentence.replace(".","")
    sentence = sentence.lower()
    my_str = "paula"
    my_list = []
    sorted_list = []
    string = ""
    lst = []
    for i in range (0,len(sentence)):
        lst = sentence.split()
        for j in range (0,len(lst)):
            string = lst[j]
            my_list = []
            sorted_list = []
            for k in range (0,len(string)):
                my_list.append(string[k])
            for l in range (0,len(my_list)):
                sorted_list.append(my_list[l])
            sorted_list.sort()
            #print(my_list)
            #print(sorted_list)
            if (sorted_list == my_list and len(my_list) > 2):
                return True
    return False
        
​
print(is_alphabetically_sorted("Paula has a French accent."))

