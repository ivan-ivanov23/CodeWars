def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return str(names[0] + ' likes this')
    elif len(names) == 2:
        return str(names[0] + ' and ' + names[1] + ' like this')
    elif len(names) == 3:
        return str(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    else:
        num = str(len(names) - 2)
        return str(names[0] + ', ' + names[1] + ' and ' + num + ' others like this')
    

# Test the function
print(likes([])) # no one likes this
print(likes(['Peter'])) # Peter likes this
print(likes(['Peter', 'John'])) # Peter and John like this
print(likes(['Peter', 'John', 'James'])) # Peter, John and James like this
print(likes(['Peter', 'John', 'James', 'Luke'])) # Peter, John and 2 others like this