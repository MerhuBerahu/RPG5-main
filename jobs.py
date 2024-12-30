from utilities import *

#TODO:
# list stats for each job

class Job:

    def __init__(self, name, description, hp, mp,spell_list,ability_list):
        self.name = name
        self.description = description
        self.hp = hp
        self.mp = mp
        self.spell_list = spell_list
        self.ability_list = ability_list



whm = Job("White Mage", "Healer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])
blm = Job("Black Mage", "Elemental damage dealer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])
rdm = Job("Red Mage", "Elemental damage dealer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])
war = Job("Warrior", "Elemental damage dealer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])
thf = Job("Thief", "Elemental damage dealer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])
mnk = Job("Monk", "Elemental damage dealer", 7, 8,["cure", "Dia"],["Dual Wield","Run"])

job_list = [whm, blm, rdm, war, thf, mnk]   

def select_job(mainjob=None):
    for index, job in enumerate(job_list, start=1):
        if mainjob is None or job != mainjob: # if passing in a main job, exclude it from the list
            print(f"{index}. {job.name}")
            print(job.description + "\n")
    # Get and validate user choice  
    selected_index = get_valid_choice(job_list)
    selected_choice = job_list[selected_index - 1]  # minus 1 to get actual index position
    return selected_choice

"""
def select_mainjob():
    print("What Main Job are you?")
    # Display numbered choices
    for index, i in enumerate(job_list, start=1):
        print(f"{index}. {i.name}")    
    # Get and validate user choice
    selected_index = get_valid_choice(job_list)  
    selected_choice = job_list[selected_index - 1] # minus 1 to get actual index position
    return selected_choice


def select_supportjob(mainjob):
    print("What Support Job are you?")
    # Display numbered choices, excluding the main job
    valid_jobs = [job for job in job_list if job != mainjob]
    for index, i in enumerate(valid_jobs, start=1):
        print(f"{index}. {i.name}")
    # Get and validate user choice
    selected_index = get_valid_choice(valid_jobs)
    selected_choice = valid_jobs[selected_index - 1]  # minus 1 to get actual index position
    return selected_choice

"""