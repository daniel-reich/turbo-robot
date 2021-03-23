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

def strip_url_params(url, params_to_strip=None):
  if '?' not in url:
    return url
  q = url.index('?')
  mod = url[q+1:]
  param = mod.split('&')
  newparam = []
  for i in reversed(param):
    if not i[0] in [j[0] for j in newparam]:
      newparam.append(i)
  if params_to_strip:
    for i in params_to_strip:
      newparam = list(filter(lambda x:i not in x,newparam))
  return url[:q+1]+"&".join(sorted(newparam))

