def choose_class_fun(class_):
    if class_ == "knight" or class_ == "Knight":
        class_char = "Knight"
        base_damage = 30
        stamina = 15
        patience = 35
        loyalty = 20
        strength = 20
        wisdom = 0
    elif class_ == "archer" or class_ == "Archer":
        class_char = "Archer"
        base_damage = 45
        stamina = 20
        patience = 10
        loyalty = 5
        strength = 25
        wisdom = 5
    elif class_ == "wizard" or class_ == "Wizard":
        class_char = "Wizard"
        base_damage = 15
        stamina = 25
        patience = 50
        strength = 5
        wisdom = 60
        loyalty = 65
    elif class_ == "troll" or class_ == "Troll":
        class_char = "Troll"
        base_damage = 60
        stamina = 15
        patience = 5
        strength = 70
        wisdom = 0
        loyalty = 10
    return class_char,base_damage,stamina,patience,strength,wisdom,loyalty