"""
Implementing RPSLS for Practice Project
"""

def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

    
print(name_to_number("rock"))		# output - 0
print(name_to_number("Spock"))		# output - 1
print(name_to_number("paper"))		# output - 2
print(name_to_number("lizard"))		# output - 3
print(name_to_number("scissors"))	# output - 4