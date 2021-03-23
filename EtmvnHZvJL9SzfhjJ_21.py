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
def strip_url_params(url, to_strip=None):
    if not to_strip:
        to_strip = []
    res = []
    if '?' not in url:
        return url
    for param in reversed(re.findall(r'[?&]([^&]+)', url)):
        k, v = param.split('=')
        if k not in to_strip:
            to_strip.append(k)
            res.append(param)
    if res:
        return url[:url.index('?')+1] + '&'.join(sorted(res))
    else:
        return url[:url.index('?')]

