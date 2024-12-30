class Ability:

    def __init__(self, name, description, level, effect, effect_amount,tp_cost,cooldown, cast_time, modifier, modifier_amount, element_affinity):
        self.name = name
        self.description = description
        self.level = level
        self.effect  = effect
        self.effect_amount = effect_amount
        self.tp_cost = tp_cost
        self.cooldown = cooldown
        self.cast_time =cast_time
        self.modifier = modifier
        self.modifier_amount = modifier_amount
        self.element_affinity = element_affinity