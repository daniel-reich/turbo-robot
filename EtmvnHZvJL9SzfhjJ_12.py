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
from collections import OrderedDict
def strip_url_params(url: str, params_to_strip=None) -> str:
    params_in_url = re.sub(r'(.+\?)', '', url)
    if params_in_url == url:
        return url
    dict_for_it = {}
    for param in params_in_url.split('&'):
        dict_for_it[param[0]] = param[2]
    sorted_dict = OrderedDict(sorted(dict_for_it.items(), key=lambda t: t[0]))
    if params_to_strip is None:
        return 'https://edabit.com?' + '&'.join(letter + "=" + number for letter, number in sorted_dict.items())
    else:
        for key in list(sorted_dict.keys()):
            if key in params_to_strip:
                sorted_dict.pop(key)
        return 'https://edabit.com?' + '&'.join(letter + "=" + number for letter, number in sorted_dict.items())

