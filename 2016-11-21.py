# Author: Kelly Lynch
# Date: 2016-11-24
# Description: Learning Python, doing Reddit challenges at https://www.reddit.com/r/dailyprogrammer/
# Challenge: https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

# Function to create an array of user inputs of colours in order in which they are cut.
def getInput():
    # Variable Declarations
    validInputs = ['white', 'red', 'black', 'orange', 'green', 'purple', 'q']
    inputValid = 0
    colourList = []
    arrayIndex = 0
    loops = 0
    keepLooping = 1

    # Instructions to user
    print "Enter colours in the order of cut"
    print "Enter Colour or 'q' to stop"

    # Infinite Loop
    while keepLooping:
        # Get Input and test to see if it's valid, if it is add it to the array, if not notify the user
        colourList.append(raw_input())
        for validInput in validInputs:
            if colourList[arrayIndex] == validInput:
                inputValid = 1
                break
            else:
                inputValid = 0

        if inputValid == 1:
            # If 'q' is entered remove 'q' from array and exit user input
            if colourList[arrayIndex] == 'q':
                keepLooping = 0
                colourList.pop()
            # Get ready for the next input
            arrayIndex += 1
        else:
            # Alert user and remove invalid entry from the list
            print "Not a valid input"
            colourList.pop()

    # Display the entered list of colours to the user for verification
    print "Your colours are the following (in order):"
    for colour in colourList:
        if colour != 'q':
            print colour

    return colourList


# Function to determine if the bomb is sucessfully disarmed or exploded.
# TODO: Determine if colour list is valid or not
def disarm(passedColours):
    print "boom"
    print "disarmed"

disarm(getInput())
