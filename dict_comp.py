names_and_ages = [
    ("Sarah", 22), 
    ("jorge", 50), 
    ("sam", 38),
    ("frank", 27),
    ("bob", 39),
    ("sandy", 46),
    ("shawn", 16),
]
​
# transfer the above list into a dictionary whose keys are the names 
# and values are the ages 
​
d = {}
# with a for loop
# taking advantage of Python's automatic destructuring of tuples 
for name, age in names_and_ages:
    # assign the name as a key to our dict with the age as value 
    d[name] = age
​
d = {name: age for name, age in names_and_ages}
​
print(d)