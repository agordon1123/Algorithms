#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  total = []

  if len(ingredients) < len(recipe):
    return 0

  for i in recipe:
    if math.floor((ingredients[i] / recipe[i])) == 0:
      total.append(0)
    else:
      total.append(math.floor((ingredients[i] / recipe[i])))

  if 0 in total:
    return 0
  else:
    return min(total)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))