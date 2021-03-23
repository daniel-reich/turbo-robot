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
def strip_url_params(url, *params_to_strip):
  d = {}
  for i in [x.split('=') for x in re.findall("[a-z]=[0-9]", url)]:
    d[i[0]] = i[1] #url to dict
​
  if params_to_strip: #delete params
    [d.pop(i) for i in params_to_strip[0] if i in d]
​
  s = ''.join(sorted(['{}={}&'.format(i, d[i]) for i in d]))
  if s and s[-1] == '&': s = s[:-1] #from dict to url
​
  return re.sub('[a-z]=[0-9].*', s, url) #change url

