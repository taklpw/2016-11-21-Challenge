# Author: Kelly Lynch
# Date: 2016-11-24
# Description: Learning Python, doing Reddit challenges at https://www.reddit.com/r/dailyprogrammer/
# Challenge: https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

# Function to create an array of user inputs of colours in order in which they are cut.


def getinput():
    # Variable Declarations
    validinputs = ['white', 'red', 'black', 'orange', 'green', 'purple', 'q']
    goodvalue = 0
    colourlist = []
    arrayindex = 0
    keeplooping = 1

    # Instructions to user
    print "Enter colours in the order of cut"
    print "Enter Colour or 'q' to stop"

    # Infinite Loop
    while keeplooping:
        # Get Input and test to see if it's valid, if it is add it to the array, if not notify the user
        colourlist.append(raw_input())
        for validInput in validinputs:
            if colourlist[arrayindex] == validInput:
                goodvalue = 1
                break
            else:
                goodvalue = 0

        if goodvalue == 1:
            # If 'q' is entered remove 'q' from array and exit user input
            if colourlist[arrayindex] == 'q':
                keeplooping = 0
                colourlist.pop()
            # Get ready for the next input
            arrayindex += 1
        else:
            # Alert user and remove invalid entry from the list
            print "Not a valid input"
            colourlist.pop()

    # Display the entered list of colours to the user for verification
    print "Your colours are the following (in order):"
    for colour in colourlist:
        if colour != 'q':
            print colour

    return colourlist


# Function to determine if the bomb is sucessfully disarmed or exploded.
# TODO: Determine if colour list is valid or not
def disarm(passedcolours):
    print "boom"
    print "disarmed"


disarm(getinput())
