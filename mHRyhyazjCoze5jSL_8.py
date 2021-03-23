"""


Write a function to replace all instances of character `c1` with character
`c2` and vice versa.

### Examples

    double_swap("aabbccc", "a", "b") ➞ "bbaaccc"
    
    double_swap("random w#rds writt&n h&r&", "#", "&")
    ➞ "random w&rds writt#n h#r#"
    
    double_swap("128 895 556 788 999", "8", "9")
    ➞ "129 985 556 799 888"

### Notes

Both characters will show up at least once in the string.

"""

def double_swap(string,chr1,chr2):
    new_string = ""
    for char in string:
        if char == chr1:
            new_string = new_string + chr2
        elif char == chr2:
            new_string = new_string + chr1
        else:
            new_string = new_string + char
    return new_string

