# Import all the other modules
import jokes
import addition
import happy

# Each element of the array is a dictionary
# Each dictionary contains a string that is show to the user and a function that is called if they pick it
# Cool thing here is you can add more options here and they will automatically show up the next time you run the program.
options = [
    {
        "string": "Tell me a joke",
        "function": jokes.tell_joke
    },

    {
        "string": "Let me add a couple numbers",
        "function": addition.add_nums
    },

    {
        "string": "Show me a happy face",
        "function": happy.print_happy_face
    },

    {
        "string": "Leave this place",
        "function": exit
    }
]
