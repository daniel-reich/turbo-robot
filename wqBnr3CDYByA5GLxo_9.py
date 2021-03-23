"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

def unravel(txt):
    open_bracket, close_bracket = [], []
    for i in range(len(txt)):
        if txt[i] == '[':
            open_bracket.append(i)
        elif txt[i] == ']':
            close_bracket.append(i)
    sub_strings = []
    for o, c in zip(open_bracket, close_bracket):
        sub_strings.append(txt[o: c + 1])
    for i in range(len(sub_strings)):
        txt = txt.replace(sub_strings[i], '{}')
        sub_strings[i] = sub_strings[i].replace('[', "['")\
            .replace(']', "']").replace('|', "','")
    format_str, for_str = '', ''
    for i in range(len(sub_strings)):
        format_str += 's' + str(i) + ', '
        for_str += ' for ' + 's' + str(i) + ' in ' + sub_strings[i]
    return sorted(eval('["' + txt + '".format(' + format_str[: -2]
                  + ')' + for_str + ']'))

