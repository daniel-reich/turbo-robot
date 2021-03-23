"""


Given two strings `s` and `t`, create a function to determine if they are
isomorphic. Two strings are isomorphic if the characters in `s` can be
replaced to get `t`. All occurrences of a character must be replaced with
another character while preserving the order of characters. No two characters
may map to the same character but a character may map to itself.

### Examples

    is_isomorphic("egg", "add") ➞ True
    
    is_isomorphic("aba", "baa") ➞ False
    
    is_isomorphic("paper", "title") ➞ True

### Notes

N/A

"""

def is_isomorphic(s, t):
    s.lower();t.lower();
    alphabet={};values=[];
    for i in range(len(s)):
        # if the character in string s does not point to anything yet, and the character in string t is not pointed by anything,
        #create a mapping from s[i] to t[i] 
        if(s[i] not in alphabet):
            if(t[i] not in values):
                alphabet.update({s[i]:t[i]});
                values.append(t[i]);
            else:
                return False;            # if the character in string s point to a character in t that has been pointed, return false
        elif(alphabet[s[i]] != t[i]):
            return False;                # if there is already a mapping from s[i], but not to t[i],this means that two strings are not isomorphic
        
    #print(alphabet)
    return True;

