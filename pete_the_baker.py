def cakes(recipe, available):
    # list to keep the amount of cakes that can be made with
    # every ingredient available
    result_avail = []
    # Here the <= is subset
    if recipe.keys() <= available.keys():
        for key, value in recipe.items():
            # Int divide the available ingredient by the 
            # required one to find for how many cakes you can use it
            for_cake = available[key] // value
            # add this value to the list
            result_avail.append(for_cake)
        # find the limiting factor, i.e., how many cakes you can make
        return min(result_avail)
    
    return 0

# Test the function
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})) # 2
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'milk': 200})) # 0
