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

from collections import OrderedDict 
​
def extract_params(param):
  key_value = param.split("=")
  return (key_value[0], key_value[1])
​
def strip_url_params(url, params_to_strip=[]):
  parts = url.split('?')
  if len(parts) == 1:
    return url
  url = parts[0]
  parameters = parts[1]
  params_map = OrderedDict(map(extract_params, parameters.split("&")))
  params_string = ["=".join([key, val]) for (key, val) in params_map.items() if key not in params_to_strip]
  return url + "?" + "&".join(params_string)

