import sqlite3

class Spell:
    def __init__(self, name, description, effect, effect_amount, mp_cost, cooldown, cast_time, modifier, modifier_amount, element_affinity, whm, blm, rdm, war):
        self.name = name
        self.description = description
        self.effect = effect
        self.effect_amount = effect_amount
        self.mp_cost = mp_cost
        self.cooldown = cooldown
        self.cast_time = cast_time
        self.modifier = modifier
        self.modifier_amount = modifier_amount
        self.element_affinity = element_affinity
        self.whm = whm
        self.blm = blm
        self.rdm = rdm
        self.war = war

    def __str__(self):
        return f"Spell: {self.name}, Effect: {self.effect} ({self.effect_amount})"

def fetch_spells_from_database(database_path):
    spells = []
    try:
        # Connect to the database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Query the spells table
        cursor.execute("SELECT * FROM spells")
        rows = cursor.fetchall()

        # Column names for reference
        columns = [column[0] for column in cursor.description]

        # Map rows to Spell instances
        for row in rows:
            spell_data = dict(zip(columns, row))
            spell = Spell(
                name=spell_data['name'],
                description=spell_data['description'],
                effect=spell_data['effect'],
                effect_amount=spell_data['effect_amount'],
                mp_cost=spell_data['mp_cost'],
                cooldown=spell_data['cooldown'],
                cast_time=spell_data['cast_time'],
                modifier=spell_data['modifier'],
                modifier_amount=spell_data['modifier_amount'],
                element_affinity=spell_data['element_affinity'],
                whm=spell_data['whm'],
                blm=spell_data['blm'],
                rdm=spell_data['rdm'],
                war=spell_data['war']
            )
            spells.append(spell)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()

    return spells

# Example usage
database_path = "database.db"
spells = fetch_spells_from_database(database_path)


### TESTING ###
"""
#print all spells
for spell in spells:
    print(spell)

#print(spells[0].description)

#print spell for whm at job level
job = "whm"
level = 1

for spell in spells:
    if getattr(spell, job) <= level:
        print(spell)



#print healing spells
for spell in spells:
    if getattr(spell, "effect") == "healing":
        print(spell)


print(spells[0].description)
for spell in spells:
    print(spell.description)

"""
