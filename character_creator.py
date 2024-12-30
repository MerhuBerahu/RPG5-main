from beings import *
from races import *
from utilities import *
from jobs import *


# TODO: 



def choose_name():
    name = input("Hello adventurer, what is your name? ")
    return name


def choose_gender():
    gender_choices = ['Male', "Female"]
    print("Which gender are you?")
    # Display numbered choices
    for index, i in enumerate(gender_choices, start=1): # start at 1 instead of index 0, real start
        print(f"{index}. {i}")    
    # Get and validate user choice
    selected_index = get_valid_choice(gender_choices)
    selected_choice = gender_choices[selected_index - 1] # minus 1 to get actual index position
    return selected_choice
    

player = Player(choose_race(), choose_gender(), choose_name(), 1, None, None, 10, "staff", 100, 300)
player.mainjob = select_job()
player.supportjob = select_job(player.mainjob)

print(player.name)
print(player.mainjob.name)
print(player.supportjob.name)



