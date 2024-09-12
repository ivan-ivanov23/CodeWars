"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. 
Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, 
otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! 
So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
"""

# Opposite directions
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dir_reduc(plan):
    new_plan = []
    for d in plan:
        # If the new plan is not empty and the last direction in the new plan 
        # is the opposite of the current direction,
        # remove the last direction from the new plan
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        
        else:
            # Otherwise, add the current direction to the new plan
            new_plan.append(d)
    return new_plan

# Test
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # Expected: ['WEST']
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])) # Expected: ['NORTH', 'WEST', 'SOUTH', 'EAST']