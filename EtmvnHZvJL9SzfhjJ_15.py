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
def strip_url_params(url, params_to_strip=[]):
  try:
    params_start = url.index('?')
  except ValueError:
    return url
  url_raw = url[:params_start]
  params = OrderedDict([pp.split('=') for pp in url[params_start+1:].split('&')])
  for param in params_to_strip:
    try:
      del params[param]
    except KeyError:
      pass
  if params:
    return url_raw + '?' + '&'.join([k+'='+v for k, v in params.items()])
  else:
    return url_raw

