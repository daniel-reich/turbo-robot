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
  if url.find('?') == -1:
    return url
  param_string = url[url.find('?')+1:]
  params = {}
  while len(param_string) > 0:
    eq = param_string.find('=')
    amp = param_string.find('&')
    key = param_string[:eq]
    if amp == -1:
      value = param_string[eq+1:]
      param_string = ''
    else:
      value = param_string[eq+1:amp]
      param_string = param_string[amp+1:]
    params[key] = value
  for item in params_to_strip:
    params.pop(item, None)
  new_url = url[:url.find('?')+1]
  for key in sorted(params):
    new_url += (key + '=' + params[key] + '&')
  return new_url[:-1]

