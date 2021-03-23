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

def strip_url_params(url, params_to_strip=[]):
  fields = url.split('?')
  addr = fields[0]
  s = addr
  if len(fields) <= 1:
    return s
  s += '?'  
  field = fields[1].split('&')
  d = dict()
  l = []
  for f in field:
    tokens = f.split('=')
    if tokens[0] not in params_to_strip:
      if tokens[0] not in l:
        l.append(tokens[0])
      d[tokens[0]] = tokens[1]  
  for i in range(len(l)):
    key = l[i]
    s += key + '=' + d[key]
    if i < len(l) - 1:
      s += '&'
  return s

