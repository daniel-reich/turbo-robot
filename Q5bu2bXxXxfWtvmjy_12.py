"""


Given a string of letters in the English alphabet, return the letter that's
missing from the string. The missing letter will make the string be in
alphabetical order (from A to Z).

If there are no missing letters in the string, return `"No Missing Letter"`.

### Examples

    missing_letter("abdefg") ➞ "c"
    
    missing_letter("mnopqs") ➞ "r"
    
    missing_letter("tuvxyz") ➞ "w"
    
    missing_letter("ghijklmno") ➞ "No Missing Letter"

### Notes

The given string will never have more than one missing letter.

"""

def missing_letter(txt):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    first = alphabets.index(txt[0])
    last = alphabets.index(txt[-1])
    main = set(alphabets[first: last+1])
    txt = set(txt)
    final = "".join(list(main - txt))
    if final:
        return final
    else:
        return "No Missing Letter"

