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
import string
def strip_url_params(url, *params_to_strip):
  for alpha in string.ascii_lowercase:
    pattern = r"({}=)+".format(alpha)
    if len(re.findall(pattern, url)) > 1:
      m = re.search(pattern.format(alpha), url)
      url = url[:m.end()] + re.sub(pattern, "", url[m.end():])
      n = re.search(pattern.format(alpha), url)
      url = url[:n.end()] + url[-1] + url[n.end() + 1:]
      url = url[:-2]
  for param in params_to_strip:
    url = re.sub(r"&{}=[0-9]".format(param), "", url)
    url = re.sub(r"{}=[0-9]&".format(param), "", url)
    url = re.sub(r"{}=[0-9]".format(param), "", url)
  return url

