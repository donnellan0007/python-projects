import random


def game():
    damage = 0
    strength = 0
    char_class = ""
    loyalty = 0
    wisdom = 0
    stamina = 0
    health = 0
    weapon_dmg = 0
    opponent = ""
    opponent_weapon = ""
    opponent_health = 0
    

    message = input("Choose your class: [Knight, Wizard, Archer, Troll]: ")
    if message == "knight" or message == "Knight":
        strength = 30
        health = 45
        char_class = "Knight"
        loyalty = 15
        wisdom = 5
        stamina = 25
        weapon_dmg = 45
        weapons = ['Sword',]
    elif message == "wizard" or message == "Wizard":
        strength = 5
        char_class = "Wizard"
        health = 30
        loyalty = 50
        wisdom = 65
        stamina = 15
        weapon_dmg = 20
        weapons = ['Magic',]
    elif message == "archer" or message == "Archer":
        strength = 10
        health = 35
        char_class = "Archer"
        loyalty = 5
        wisdom = 0
        stamina = 35
        weapon_dmg = 55
        weapons = ['Bow',]
    elif message == "troll" or message == "Troll":
        strength = 70
        health = 50
        char_class = "Troll"
        loyalty = 10
        wisdom = 0
        stamina = 10
        weapon_dmg = 60
        weapons = ['Hands',]
    # print(f"Strength: {strength} | Character Class {char_class} | Loyalty {loyalty} | Wisdom {wisdom} | Weapon Damage {weapon_dmg}")

    print("Welcome to the game. You will play now. Also, for story purposes, the troll and archer are on one team, and the knight and wizard are on the other")
    print()
    if char_class is "Troll" or char_class is "Archer":
        print("You are walking in the forest when you see something up ahead of you. It is very faint, but there is a glow. You don't know what it is. \n You have 2 options. Do you run straight towards the light, or sneak up on it? \n")
        message = input("Run or Sneak? ")
        if message == "Run" or message == "run":
            print("You decide the best option is to confront the light. You start running towards it. It gets brighter the more you come towards it. \n It becomes apparent someone is holding a stick, with a lantern atop of it. \n There is no going back, you have to face the light. What weapon are you going to have prepared in case an altercation takes place?")
            message = input("Hands: ")
            if message == "Hands" or message == "hands":
                print(f"You get your fists ready. You are approaching the light. But alas, you now have a stamina bar. And guess what, you only have {stamina}% left. And because you're a {char_class}, you don't have much to being with")
                print(f"Do you want to continue running? Or do you want to walk the rest of the way? ")
                message = input("Run or Walk? ")
                if message == "Run" or message == "run":
                    stamina -= 6
                    print(f"Stats: \n Stamina: {stamina} \n Health: {health} \n You are within 10 metres of the building. Of course, it cost you stamina. You now have {stamina}% left. \n But luckily for you, you are able to see the figure. It is a wizard. He is holding a staff in his hand, and on top of the staff is a glowing light. Now fight him!")
                else:
                    stamina -= 2
                    print(f"Stats: \n Stamina: {stamina} \n Health: {health} \n There is a wizard in front of you. Yep, believe it or not, there is. Which sucks I guess. He's just standing there. Waving his wand around like an autistic kid who thinks he has a wand. He is saying some things which are quite gibberish, almost in a foreign language. You have your {weapons} out.")
                    message = input("Attack or Stay")
                    if message == "Attack" or message == "attack":
                        health -= 15
                        print(f"Stats: \n Stamina: {stamina} \n Health: {health} \n You lay into him with your {weapons}. The wizard starts screeching and fires his wand back at you, giving you a taste of medicine. Your health is now down to {health}%. You have to do something. ")



game()
