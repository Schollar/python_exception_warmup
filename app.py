# TODO Please make me safe! There are so many places where I can fail.
# import the choices from choices.py
import choices

# Function for running the function associated with the user choice


def run_choice(index):
    choices.options[index]['function']()


# Print a nice little welcome message
print("Wecome friend, to a world of command line python wonder!")
print("Marvel at my creations allowing you to do spectacular things.")
print("First, you must choose your own adventure.")

# Go through all choices and show each choice string to the user
for i in range(len(choices.options)):
    print(f"Option {i+1}: {choices.options[i]['string']}")

# Show the user options until the user decides to choose the exit option
try:
    while(True):
        # Ask for the user input, assume it's an integer
        user_input = int(
            input("Please select the number you would like to choose: "))
    # Call the run_choice function with the users choice - 1 (because arrays count from 0)
        run_choice(user_input - 1)
except IndexError:
    print('You must choose a number from the list!')
except ValueError:
    print('Input must be a number!')
except:
    print('Something went wrong, you must input a number')
