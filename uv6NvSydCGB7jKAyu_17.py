"""


Hermione has come up with a precise formula for determining whether or not a
phrase was ssspoken by a parssseltongue ( _a reference from the Harry Potter
universe; the language of ssserpents and those who can converse with them_ ).

Each word in a sssentence must contain either:

  1. Two or more consecutive instances of the letter "s" (i.e. must be together `ss..`), or...
  2. Zero instances of the letter "s" by itself.

### Examples

    is_parsel_tongue("Sshe ssselects to eat that apple. ") ➞ True
    
    is_parsel_tongue("She ssselects to eat that apple. ") ➞ False
    # "She" only contains one "s".
    
    is_parsel_tongue("Beatrice samples lemonade") ➞ False
    # While "samples" has 2 instances of "s", they are not together.
    
    is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly.") ➞ True

### Notes

N/A

"""

#At least 2 instances of the letter "s" (must be together ss), or      
#Zero instances of the letter "s".
def is_parsel_tongue(sentence):
    sentence = sentence.lower().strip()
    s_list = sentence.split(" ")
    for i in s_list:
        if i.count("s") != 0 and i.count("s") < 2:
            print(s_list)
            return False
        if i.count("s") >= 2:
            if i[i.index("s")] == "s" and i[i.index("s")+1] == "s":
                return True
            else:
                return False
                
    return True

