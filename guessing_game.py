# Guessing game 
​
# What does it do? 
# We'll write a program that plays a guessing game with a user 
# Would be useful to have the program print out the rules at the beginning 
# How does the user communicate to the program that the program didn't guess
# the right number? 
# We can have the user specify that the program's guess it too low, too high, 
# or equal 
# After the program makes a guess, it will wait on user input from the command line 
# Player types in "low", "high", or "equal"
# Program reads in that input and acts on it 
# If the player says the number is too low, then program knows it needs to guess higher
# and vice versa for if the number is too high 
# How does the program generate a guess? 
​
# What are the rules?
# The user will think of a number, the program has to guess it 
# Is there a range of possible numbers? Or can we allow any number? 
# Let's say the range is between 1 and 100 
​
# Printing out the rules 
print("Think of a number between 1 and 100, and I'll guess it.")
print("You have to tell me if my guess is less than, greater than, or equal to your number.")
​
# How does the game actually run? 
# Loop until the program exits 
# When does the program exit? 
# Either when the user terminates it, or when the program has successfully guessed
# the player's number
​
# variables to store the floor and ceiling of our range 
floor = 1
ceiling = 100
​
# boolean value to indicate whether the program guessed the number or not 
got_it = False 
​
# In the loop
while not got_it:
    # Game generates a guess between 1 and 100 
        # should it guess a totally random number between this range? 
        # should we have it guess a bit smarter
        # guess the halfway point between the range? 
        # we'll have it guess halfway between the range 
    # using a midpoint formula 
    # in Python, `//` that's floor division (always rounds down)
    guess = (floor + ceiling) // 2
​
    # print out the guess to the user 
    print(f"I'm guessing {guess}.")
​
    # wait for the user's input to tell the program if its guess was high, low, or equal
    # read in user's input 
    result = input("Is my guess less, greater, or equal to your number?")
​
    # format the result for ease 
    # lowercase the result 
    result = result.lower()
    # let's just grab the first letter of the input 
    result = result[0]
​
    # act according to the user's input 
​
    # if input == 'high'
    if result == 'h':
        # we need to guess lower for the next guess 
        # narrow the range accordingly 
        # set the "ceiling" of the range equal to guess - 1
        ceiling = guess - 1
​
    # if input == 'low'
    elif result == 'l':
        # we need to guess higher for the next guess 
        # narrow the range accordingly 
        # set the "floor" of the range to equal guess + 1
        floor = guess + 1
​
    # if input == 'equal'
    elif result == 'e':
        # print "I guessed your number!"
        print("I guessed your number!")
        # quit the game loop 
        got_it = True
​
    # if result isn't any of the above, then print an error message 
    else:
        print("I don't know what that means. Try again please.")
​
    # go on to the next loop iteration 
    # our range has been updated according to the user's input 
