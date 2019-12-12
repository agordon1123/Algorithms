#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  cache = {}
  def recurse(n):
    if n in cache:
      return cache[n]
    if n == 0 or n == 1:
      return 1
    elif n < 0:
      return 0
    
    result = recurse(n - 1) + recurse(n - 2) + recurse(n - 3)
    cache[n] = result
    return result

  return recurse(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')