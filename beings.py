#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with the Base being Class that players, NPC's
and enemies inherit from
"""

import random
from races import *


class Character:

    def __init__(self, race, sex,name, level, mainjob, supportjob,gold,inventory):
        self.race = race
        self.sex = sex
        self.name = name
        self.level = level
        self.mainjob = mainjob
        self.supportjob = supportjob
        self.gold = gold
        self.inventory = inventory


class Player(Character):

    def __init__(self, race, sex, name,  level, mainjob, supportjob,gold,inventory,currentexp,exptnl):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        self.currentexp = currentexp
        self.exptnl = exptnl
    
    def gain_experience(self, amount):
            print(f"{self.name} gains {amount} experience points!")
            self.currentexp += amount
            self.check_level_up()    

    def check_level_up(self):
        while self.currentexp >= self.exptnl:
            self.currentexp -= self.exptnl
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exptnl = int(self.exptnl * 1.5)  # Increase threshold
        print(f"{self.name} leveled up to Level {self.level}!")
        print(f"Next level requires {self.exptnl} currentexp points.")

    def __str__(self):
        return (f"Player: {self.name}, Level: {self.level}, "
                f"currentexp: {self.currentexp}/{self.exptnl}")


class Enemy(Character):
    
    def __init__(self, race, sex, name,level, mainjob, supportjob,gold, inventory= None):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def loot(self):           
        choices = []
        for item, weight in self.inventory:
            choices.extend( [item]*weight )
        return random.choice(choices)    
    
    def EnemyGenerator(race):
        name = race_name_random(random.choice(race))
        print(name)
        return name

class NPC(Character):

    def __init__(self, race, sex, name,  level, mainjob, supportjob,gold,inventory,quests,merchant = None):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        self.quests = quests
        self.merchant = merchant

race = random.choice(npc_races)
#Enemy.EnemyGenerator()

### TESTING ###




"""
player = Player('orc', 'M', 'Balinor', 1, None, None, 10, "staff", 100, 300)
print(player.name)
print(f"Level {player.level}")
print(f"Current Exp: {player.currentexp}")
print(f"TNL: {player.exptnl}")

player.gain_experience(50)
print(player.name)
print(f"Level {player.level}")
print(f"Current Exp: {player.currentexp}")
print(f"TNL: {player.exptnl}")

player.gain_experience(80)
print(player.name)
print(f"Level {player.level}")
print(f"Current Exp: {player.currentexp}")
print(f"TNL: {player.exptnl}")

player.gain_experience(200)
print(player.name)
print(f"Level {player.level}")
print(f"Current Exp: {player.currentexp}")
print(f"TNL: {player.exptnl}")
"""