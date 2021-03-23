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

def strip_url_params(*args):
  url = args[0]
  if len(args) == 2:
    params_to_strip = args[1]
  else:
    params_to_strip = []
  lst = url.split('?')
  if len(lst) == 1:
    return url
  else:
    params_string, dct, var = lst[1], {}, []
    items = params_string.split('&')
    for item in items:
      lst1 = item.split('=')
      dct[lst1[0]] = lst1[1]
      if lst1[0] not in params_to_strip and lst1[0] not in var:
        var.append(lst1[0])
    return lst[0] + "?" + "&".join([variable + "=" + dct[variable] for variable in var])

