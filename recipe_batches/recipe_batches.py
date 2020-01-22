#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # keep a count of the number of times a recipe is made
    count = 0
    # get a list of the key names
    x = list()

    for i in ingredients:
        x.append(i)
    # as long as there are the same numbers of ingredients left as in the recipe

    while len(x) == len(ingredients) and len(x) == len(recipe):
        # subtract each item in the recipe from the ingredients
        for i in recipe:
            # if the result is less than 0, remove the item from the dictionary
            if ingredients[i] - recipe[i] < 0:
                del ingredients[i]
                return count
        # else add 1 to the count
            else:
                ingredients[i] -= recipe[i]
        count += 1
       # if this is last item in loop add 1 to the count
    # if not return count
    return count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
