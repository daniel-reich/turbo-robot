"""


Create a function that takes a URL (string), removes duplicate query
parameters and parameters specified within the 2nd argument (which will be an
_optional_ list).

### Examples

    strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"
    
    strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"
    
    strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"

### Notes

  * The 2nd argument `params_to_strip` is optional.
  * `params_to_strip` can contain multiple params.
  * If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).

"""

import re
​
​
def remove_dups(lst):
    already_used = []
    filtered_list = []
    for i in range(len(lst)-1, -1, -1):
        if lst[i][0] not in already_used:
            filtered_list.append(lst[i])
            already_used.append(lst[i][0])
    return list(sorted(filtered_list, key=lambda a: a[0]))
​
​
def strip_url_params(txt, strip_parameter=None):
    pattern = re.compile(r"(https://edabit.com)\??(.*)")
    match = re.search(pattern, txt)
    if match.group(2) == '':
        return match.group(1)
    a = [param.split('=') for param in match.group(2).split("&")]
    if strip_parameter:
        b = [element for element in remove_dups(a) if element[0] not in strip_parameter]
        if b == []:
            return match.group(1)
    else:
        b = remove_dups(a)
    return match.group(1) + "?" + '&'.join(['='.join(element) for element in b])

