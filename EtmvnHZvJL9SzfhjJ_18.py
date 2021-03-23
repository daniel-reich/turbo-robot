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
def strip_url_params(url, params_to_strip = []):
    # Disassemble url
    url_parts = re.split('\?', url)
    params_dict = {}
    new_url_parts = [url_parts[0]]
​
    # Extract all unique params
    if len(url_parts) > 1:
        params = re.split('&', url_parts[1])
        for s in params:
            param_parts = re.split('=', s)
            params_dict[param_parts[0]] = param_parts[1]
​
    # Remove params_to_strip from the map
    for param in params_to_strip:
        params_dict.pop(param, None) 
​
    if len(params_dict.keys()) > 0: new_url_parts.append('?')
​
    # Re-assemble url
    for key in sorted(params_dict.keys()):
        new_url_parts.append(key + '=' + params_dict[key])
        
    # Put a &-character in-between the params
    for i in range(2, len(new_url_parts) - 1):
        new_url_parts[i] += '&'
​
    return ''.join(new_url_parts)

