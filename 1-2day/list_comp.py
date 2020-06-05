def double(x):
    return x * 2
​
lis = [10, 11, 12, 13, 14]
​
# List Comprehensions 
doubled = [double(x) for x in lis]
​
# List comprehension to copy the elements of lis 
# and populate another list with them 
copy_of_lis = [x for x in lis]
​
# List comprehension that only copies the even elements
# of lis and populates another list with them 
evens_of_lis = [x for x in lis if x % 2 == 0]
​
# List comprehension format
# [ 
#   `return statement of action for each element`,
#   `the loop part to access each element`,
#   `optional criteria to filter out elements`,
# ]
​
# translate into a normal for loop 
evens_of_lis = []
# loop through each element of lis
for x in lis:
    # check if the element is even 
    if x % 2 == 0:
        # if it is, append it to the evens_of_lis 
        evens_of_lis.append(x)
​
# The loop part where we're accessing "outside"
# The initial part says how we want to treat that element 
# The fact that spelled this out between brackets means we 
# want all these elements in a list 
​
print(evens_of_lis)