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

def strip_url_params(url, params_to_strip = []):
  if url.count("?") < 1:
    return url
  params = url.split("?")[1].split("&")
  returnparams = {}
  returnkeys = []
  for param in params:
    key, value = param.split("=")
    if key in params_to_strip:
      continue
    if key in returnkeys:
      returnparams[key] = value
    else:
      returnkeys.append(key)
      returnparams[key] = value
  returnurl = url.split("?")[0] + "?"
  for key in returnkeys:
    returnurl += key + "=" + returnparams[key] + "&"
  returnurl = returnurl[:-1]
  return returnurl

