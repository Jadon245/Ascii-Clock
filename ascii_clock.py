# Define placeholder variables; this makes it easier to visualize the giant dictionary and plug in repetetive values
# They intentionally look similar to the variables; they make it readable
S = ' '
X = 'X'
A = 'A'
M = 'M'
P = 'P'


            ### GOAL 1 ###
## Input and validate format for time ##
# Ask for a time and test if it is valid syntax; assume invalid until it past tests
start = input('Enter the time: ')
valid = False

# Test to make sure input is in military time
while not valid:
    
    # Split by ':' to test left and right side easier; if no colon, it tests as invalid and prompts retry
    if ':' in start:
        y = start.split(':')
        hour = y[0]
        minute = y[1]
        
        # Make sure both sides are numbers and set them as integers for later
        if hour.isdigit() and minute.isdigit():
            hour = int(hour)
            minute = int(minute)

            # Make sure both sides are within the specified range of a clock
            if 24 > hour >= 0 and 60 > minute >= 0:
                valid = True

    # If conditions are not meant, reprompt the user
    if not valid:
        start = input('The entered value was formatted incorrectly, please entter a correct time: ')






            ### GOAL 2 ###
## Input and validate format for format ##

# Ask user for a time format
clock = input('Choose the clock type (12 or 24): ')
valid = False

# Check if input syntax was correct and reprompt if not
while not valid:

    # Ensure it's a number and adjust attribute if so
    if clock.isdigit():

        # Apply specific attributes for military time
        if int(clock) == 24:
            valid = True
            military = True

        # Apply specific attributes for non military time
        elif int(clock) == 12:
            valid = True
            military = False

    # Remprompt user if not valid; must use separate if statement to not repeat reprompt
    if not valid:
        clock = input('Incorrect value, please try again: ')





            ### GOAL 3 ###
## Convert time to a readable format ##


# Start by converting minute since it has no special rules
minute = ' : ' + str(minute//10) + S + str(minute%10)

# Adjust for military time and determine status (am or pm)
# military time has no special format
if military:
    pass

# Identify edge cases and fix
elif hour == 0:
    hour = 12
    minute += ' A M'

elif hour == 12:
    minute += ' P M'

# Apply formatting for PM
elif hour > 12:
    hour -=12
    minute += ' P M'

# Apply formatting for AM; no adjustment to hour needed since it is already less than 12
else:
    minute += ' A M'

# Determine if 2 digits and concatenate
if hour >= 10:
    hour = str(hour//10) + S + str(hour%10)
else:
    hour = str(hour)

# Combine everything into one variable: this will be the instructions for the ascii art
time = hour + minute





            ### GOAL 4 ###
## Input and validate preferred character ##


# Ask for preferred character
preferred = input('Enter your preferred character: ')

# Define allowed characters
AllowedCharacters = list('abcdeghkmnopqrsuvwxyz@$&*=')

# validate input for character; reprompt if not in list
while preferred not in AllowedCharacters and preferred != '':
    preferred = input('Character not permitted! Try again: ')





                    ### GOAL 5 ###
## Identify symbol and create ascii art dictionary ##

# Start off by creating a dictionary which defines each character as an ascii art
# The values will specifically feature plaeholder 'X' values and blank space 'S'
# We can use logic to replace 'X' with the intended placeholder (number or preferred)
# Rows and columns can be represented as indexes of lists and sublists
# We can use this fact to go character by character and build the first row
# By doing this, we also get the option to replace 'X' with the intended placeholder


# Define dictionaries for all digits, A, P, and ':'
# Use this syntax so its easier to see visually
Ascii = {
    '0' :
        [
            X+X+X,
            X+S+X,
            X+S+X,
            X+S+X,
            X+X+X
        ],
    '1' :
        [
            S+X+S,
            X+X+S,
            S+X+S,
            S+X+S,
            X+X+X
        ],
    '2' :
        [
            X+X+X,
            S+S+X,
            X+X+X,
            X+S+S,
            X+X+X
        ],
    '3' :
        [
            X+X+X,
            S+S+X,
            X+X+X,
            S+S+X,
            X+X+X
        ],
    '4' :
        [
            X+S+X,
            X+S+X,
            X+X+X,
            S+S+X,
            S+S+X
        ],
    '5' :
        [
            X+X+X,
            X+S+S,
            X+X+X,
            S+S+X,
            X+X+X
        ],
    '6' :
        [
            X+X+X,
            X+S+S,
            X+X+X,
            X+S+X,
            X+X+X
        ],
    '7' :
        [
            X+X+X,
            S+S+X,
            S+S+X,
            S+S+X,
            S+S+X
        ],
    '8' :
        [
            X+X+X,
            X+S+X,
            X+X+X,
            X+S+X,
            X+X+X
        ],
    '9' :
        [
            X+X+X,
            X+S+X,
            X+X+X,
            S+S+X,
            X+X+X
        ],
    ':' :
        [
            S,
            ':',
            S,
            ':',
            S
        ],
    'A' :
        [
            S+A+S,
            A+S+A,
            A+A+A,
            A+S+A,
            A+S+A
        ],
    'P' :
        [
            P+P+P,
            P+S+P,
            P+P+P,
            P+S+S,
            P+S+S
        ],
    'M' :
        [
            M+S+S+S+M,
            M+M+S+M+M,
            M+S+M+S+M,
            M+S+S+S+M,
            M+S+S+S+M
        ],
    ' ' :
        [
            S,
            S,
            S,
            S,
            S
        ]
}


print()
row = ''

# Use converted time to go line by line and print each line -- dictionary values on the same line
# There are only 5 rows of characters in the ascii art, so use for i in range(5)
for i in range(5):

    # Make sure that it cycles through every ascii character; each character in time variable
    for j in time:


        # If preferred is blank, define the placeholder as that number
        if preferred == '':
            placeholder = j
        
        # If preferred is not blank, define the placeholder as preferred
        else:
            placeholder = preferred
        
        # Enter the list for that dictionary
        # Enter the sublist for the column
        # Replace all instances of 'X' with intended character
        row += Ascii[j][i].replace('X',placeholder)

    # After full row is built, print the row and resest variable for next Row
    print(row)
    row = ''
