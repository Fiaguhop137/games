#Setup(varibles, functions, ect.)
#Imports
import random
import math
#Functions
def ask(question, valid_answers):
    answer=input(question).strip().lower()
    answer_map={word.lower(): word for word in valid_answers}
    while answer not in answer_map:
        answer=input(f"Invalid entry. Please answer with {' or '.join(valid_answers)}. ").strip().lower()
    return answer_map[answer]
def update_cooldowns(player_cooldowns):
    #Call this at the start of every turn
    for move in player_cooldowns:
        if player_cooldowns[move]>0:
            player_cooldowns[move]-=1
def use_attack(move_name, player_cooldowns):
    #Triggers the attack and sets the cooldown.
    if player_cooldowns[move_name]==0:
        print(f"You used {move_name}! ")
        # Set the cooldown from attack data
        player_cooldowns[move_name]=attacks[move_name]["cooldown"]
        return True
    else:
        print(f"{move_name} is still on cooldown for {player_cooldowns[move_name]} turns. Try again later. ")
        return False
def get_damage(move_name, attacker_p, defender_p):
    base_dmg = attacks[move_name]["damage"]
    multiplier = atk_mods[attacker_p][defender_p]/def_mods[defender_p][attacker_p]
    return round(base_dmg * multiplier, 2)

#Variables, Lists, Contants, and Dictionaries
power_definitions={
    "Fire":"the power of flames and heat. You are able to control and manipulate flames, creating powerful attacks and defenses. You are also immune to fire and heat, allowing you to withstand extreme temperatures. You deal more damage to metal by melting it, but less to earth because it is not flammable. You have more defense towards wood since you can't put out fire by adding fuel, but less protection from water because water can extinguish fire.", 
    "Metal":"the power of strength and durability. You are able to control and manipulate metallic substanced, creating powerful weapons and armor. You are also immune to metal-based attacks such as bullets and blades, allowing you to withstand physical damage. You deal more damage to wood by cutting it, but less to water because water can cause rust. You have more defense towards earth since you are heavier than it, but less protection from fire because fire can melt metal.", 
    "Wood":"the power of growth and nature. You are able to control and manipulate plant life, creating powerful tools and structures. You are also immune to wood-based attacks, allowing you to withstand natural disasters. You deal more damage to earth since tree roots break up, penetrate, and bind soil together, but less to fire since you can't put out fire by adding fuel. You have more defense towards water because you drink water, but less protection from metal because metal can cut wood.", 
    "Earth":"the power of stability and protection. You are able to control and manipulate dirt, stone, and other earth materials, creating powerful barriers and fortifications. You are also immune to earth-based attacks, allowing you to withstand seismic activity. You deal more damage to water by soaking it up, but less to metal because metal is too durable. You have more defense towards fire you are non flammable, but less protection from wood because tree roots break up, penetrate, and bind soil together.", 
    "Water":"the power of fluidity and adaptability. You are able to control and manipulate water and ice, creating powerful waves and currents. You are also immune to water-based attacks, allowing you to withstand flooding. You deal more damage to fire by extinguishing it, but less to wood because wood can absorb water. You have more defense towards metal because it sinks in you, but less protection from earth because earth can absorb the water.", 
    "Light":"the power of illumination and vision. You are able to control and manipulate radiant energy, creating powerful beams and illusions. You are also immune to light-based attacks, allowing you to withstand bright environments. You deal more damage to dark by dispelling it, but take more damage from it as well since it obscures your vision.", 
    "Dark":"the power of negation and mystery. You are able to control and manipulate the absence of light and the shadows themself, creating powerful voids and illusions. You are also immune to dark-based attacks, allowing you to withstand eerie environments. You deal more damage to light by absorbing it, but take more damage to it as well because it blots out your shadows.", 
    "Space":"the power of dimensions and travel. You are able to control and manipulate the fabric of space, creating powerful portals and levitations. You are also immune to space-based attacks, allowing you to withstand vacuum and teleportation. You deal more damage to time by disrupting it, but take more damage from it as well since it is not in the 3 dimensions you exist in.", 
    "Time":"the power of past, present, and future. You are able to control and manipulate the flow of time, creating powerful time loops and see the future. You are also immune to time-based attacks, allowing you to withstand temporal anomalies. You deal more damage to space by disrupting it, but take more damage from it as well since it is not in your domain."}
powers={"First Powers":["Fire","Metal","Wood","Earth","Water"],"Second Powers": ["Light", "Dark"],"Third Powers": ["Space", "Time"]}
player_stats={"Health":100,"First Power":None,"Second Power":None,"Third Power":None}
strong=math.sqrt(2)
weak=1/math.sqrt(2)
atk_mods={
    "Fire":{"Fire":1,"Metal":strong,"Wood":1,"Earth":weak,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Metal":{"Fire":1,"Metal":1,"Wood":strong,"Earth":1,"Water":weak,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Wood":{"Fire":weak,"Metal":1,"Wood":1,"Earth":strong,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Earth":{"Fire":1,"Metal":weak,"Wood":1,"Earth":1,"Water":strong,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Water":{"Fire":strong,"Metal":1,"Wood":weak,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Light":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":strong,"Space":1,"Time":1,},
    "Dark":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":strong,"Dark":1,"Space":1,"Time":1,},
    "Space":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":strong,},
    "Time":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":strong,"Time":1,}
}
def_mods={
    "Fire":{"Fire":1,"Metal":1,"Wood":strong,"Earth":1,"Water":weak,"Light":1,"Dark":1,"Space":1,"Time":1},
    "Metal":{"Fire":weak,"Metal":1,"Wood":1,"Earth":strong,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Wood":{"Fire":1,"Metal":weak,"Wood":1,"Earth":1,"Water":strong,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Earth":{"Fire":strong,"Metal":1,"Wood":weak,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Water":{"Fire":1,"Metal":strong,"Wood":1,"Earth":weak,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":1,},
    "Light":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":weak,"Space":1,"Time":1,},
    "Dark":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":weak,"Dark":1,"Space":1,"Time":1,},
    "Space":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":1,"Time":weak,},
    "Time":{"Fire":1,"Metal":1,"Wood":1,"Earth":1,"Water":1,"Light":1,"Dark":1,"Space":weak,"Time":1,}
}
attacks={
        "Flame Burst":{"damage":10,"aoe":False,"cooldown":1,"type":"Fire"}, #There must be at least one attack without a cooldown for each power, otherwise the player could end up without any attacks not on cooldown and be unable to do anything.
        "Fireball":{"damage":12,"aoe":False,"cooldown":2,"type":"Fire"}, #Here I have two attacks, each with a cooldown of 2, meaning you can rotate them and always have one available. This is a pretty interesting gimmick I think
        "Heat Wave":{"damage":17,"aoe":True,"cooldown":2,"type":"Fire"}, #I want at least one aoe attack for each power, but not all of them should be aoe because that would make the game too easy.
        "Iron Spike":{"damage":10,"aoe":False,"cooldown":1,"type":"Metal"},
        "Shard Spray":{"damage":15,"aoe":True,"cooldown":4,"type":"Metal"},
        "Knife Storm":{"damage":15,"aoe":True,"cooldown":4,"type":"Metal"},
        "Vine Whip":{"damage":10,"aoe":False,"cooldown":1,"type":"Wood"},
        "Leaf Storm":{"damage":15,"aoe":True,"cooldown":4,"type":"Wood"},
        "Splinter":{"damage":5,"aoe":False,"cooldown":2,"type":"Wood"}, #somehow add bleed like effect later
        "Pebble Shot":{"damage":10,"aoe":False,"cooldown":1,"type":"Earth"},
        "Tremor":{"damage":15,"aoe":True,"cooldown":4,"type":"Earth"},
        "Boulder Crush":{"damage":20,"aoe":False,"cooldown":5,"type":"Earth"},
        "Water Jet":{"damage":10,"aoe":False,"cooldown":1,"type":"Water"},
        "Tidal Wave":{"damage":15,"aoe":True,"cooldown":4,"type":"Water"},
        "Flood":{"damage":20,"aoe":True,"cooldown":5,"type":"Water"},
        "Light Beam":{"damage":10,"aoe":False,"cooldown":1,"type":"Light"},
        "Solar Flare":{"damage":15,"aoe":True,"cooldown":4,"type":"Light"},
        "Radiant Burst":{"damage":12,"aoe":False,"cooldown":3,"type":"Light"},
        "Photon Bolt":{"damage":20,"aoe":False,"cooldown":5,"type":"Light"},
        "Void Strike":{"damage":10,"aoe":False,"cooldown":1,"type":"Dark"},
        "Shadow Flux":{"damage":17,"aoe":True,"cooldown":4,"type":"Dark"},
        "Nightmare":{"damage":20,"aoe":True,"cooldown":5,"type":"Dark"},
        "Eclipse":{"damage":25,"aoe":False,"cooldown":6,"type":"Dark"},
        "Space Rift":{"damage":10,"aoe":False,"cooldown":1,"type":"Space"},
        "Gravity Well":{"damage":15,"aoe":True,"cooldown":4,"type":"Space"},
        "Wormhole":{"damage":20,"aoe":False,"cooldown":5,"type":"Space"},
        "Singularity":{"damage":25,"aoe":True,"cooldown":6,"type":"Space"},
        "Galactic Strike":{"damage":17,"aoe":False,"cooldown":3,"type":"Space"},
        "Chronic Chakram":{"damage":10,"aoe":False,"cooldown":1,"type":"Time"},
        "Temporal Loop":{"damage":20,"aoe":False,"cooldown":5,"type":"Time"},
        "Time Bomb":{"damage":25,"aoe":True,"cooldown":6,"type":"Time"},
        "Fortune":{"damage":13,"aoe":False,"cooldown":3,"type":"Time"},
        "Destiny":{"damage":16,"aoe":False,"cooldown":3,"type":"Time"}, 
}
player_cooldowns={"Flame Burst":0, "Fireball":0, "Heat Wave":0, "Iron Spike":0, "Shard Spray":0, "Knife Storm":0, "Vine Whip":0, "Leaf Storm":0, "Splinter":0, "Pebble Shot":0, "Tremor":0, "Boulder Crush":0, "Water Jet":0, "Tidal Wave":0, "Flood":0, "Light Beam":0, "Solar Flare":0, "Radiant Burst":0, "Photon Bolt":0, "Void Strike":0, "Shadow Flux":0, "Nightmare":0, "Eclipse":0, "Space Rift":0, "Gravity Well":0, "Wormhole":0, "Singularity":0,"Supernova":0,"Chronic Chakram":0,"Temporal Loop":0,"Time Bomb":0,"Fortune":0,"Destiny":0}
#Classes
class Enemy:
    def __init__(self,name,first_power,second_power,third_power,health=100):
        self.name=name
        self.health=health
        self.powers={"First Power":first_power,"Second Power":second_power,"Third Power":third_power}
        self.knowledge={"First Power":None,"Second Power":None,"Third Power":None}
        self.cooldowns={name:0 for name in attacks}
    def is_alive(self):
        return self.health>0
#Begin
choice=ask("Would you like random(input 'rolled') or choose(input: 'choose') your powers? ", ["rolled", "choose"])
if("rolled" in choice):
    player_stats["First Power"]=random.choice(powers["First Powers"])
    player_stats["Second Power"]=random.choice(powers["Second Powers"])
    player_stats["Third Power"]=random.choice(powers["Third Powers"])
    know_more=ask(f"Your powers are: {player_stats['First Power']}, {player_stats['Second Power']}, and {player_stats['Third Power']}. \nWould you like to know more about your powers? (yes or no) ", ["yes", "no"])
    if know_more == "yes":
        print(f"{player_stats['First Power']} is {power_definitions[player_stats['First Power']]} \n\n{player_stats['Second Power']} is {power_definitions[player_stats['Second Power']]} \n\n{player_stats['Third Power']} is {power_definitions[player_stats['Third Power']]} \n")
elif("choose" in choice):
    player_stats['First Power']=ask(f"First, choose your first power. It can be either Fire, Metal, Wood, Earth, or Water. Each of these powers has its own strengths and weaknesses. If you'd like to know more about any of them, just ask!(tell me more) ", ["Fire","Metal","Wood","Earth","Water","tell me more"])
    if player_stats['First Power'] == "tell me more":
        for power in powers["First Powers"]:
            print(f"{power} is {power_definitions[power]}. \n")
        player_stats['First Power']=ask("Now, choose your first power. It can be either Fire, Metal, Wood, Earth, or Water. ", powers["First Powers"])
    player_stats['Second Power']=ask(f"Next, choose your second power. It can be either Light or Dark. If you'd like to know more about either of them, just ask!(tell me more) ", ["Light", "Dark", "tell me more"])
    if player_stats['Second Power'] == "tell me more":
        for power in powers["Second Powers"]:
            print(f"{power} is {power_definitions[power]}. \n")
        player_stats['Second Power']=ask("Now, choose your second power. It can be either Light or Dark. ", powers["Second Powers"])
    player_stats['Third Power']=ask(f"Finally, choose your third power. It can be either Space or Time. If you'd like to know more about either of them, just ask!(tell me more) ", ["Space", "Time", "tell me more"])
    if player_stats['Third Power'] == "tell me more":
        for power in powers["Third Powers"]:
            print(f"{power} is {power_definitions[power]}. \n")
        player_stats['Third Power']=ask("Now, choose your third power. It can be either Space or Time. ", powers["Third Powers"])
    print(f"Your powers are: {player_stats['First Power']}, {player_stats['Second Power']}, and {player_stats['Third Power']}.")
test_enemy=Enemy(name="Test Dummy",first_power=random.choice(powers["First Powers"]),second_power=random.choice(powers["Second Powers"]),third_power=random.choice(powers["Third Powers"]))
print(f"\n--- BATTLE START: {test_enemy.name} ---")
while player_stats["Health"]>0 and test_enemy.is_alive():
    update_cooldowns(player_cooldowns)
    my_powers=[player_stats["First Power"],player_stats["Second Power"],player_stats["Third Power"]]
    valid_moves=[name for name, data in attacks.items() if data["type"] in my_powers]
    print(f"\nYour HP: {player_stats['Health']} | {test_enemy.name} HP: {test_enemy.health}")
    move_choice = ask(f"Choose your attack({valid_moves}): ", valid_moves)
    print(f"Active Cooldowns: { {k:v for k,v in player_cooldowns.items() if v>0} }")
    if use_attack(move_choice,player_cooldowns):
        move_type=attacks[move_choice]["type"]
        if move_type == player_stats["First Power"]: enemy_p = test_enemy.powers["First Power"]
        elif move_type == player_stats["Second Power"]: enemy_p = test_enemy.powers["Second Power"]
        else: enemy_p = test_enemy.powers["Third Power"]
        dmg = get_damage(move_choice, move_type, enemy_p)
        test_enemy.health-=dmg
        print(f"You dealt {dmg} damage!")
    else:
        continue
    if not test_enemy.is_alive():
        break    
    enemy_move_type = test_enemy.powers["First Power"]
    enemy_dmg = 10 # Simple flat damage for the dummy
    player_stats["Health"] -= enemy_dmg
    print(f"{test_enemy.name} hits you for {enemy_dmg} damage!")
if player_stats["Health"]>0:
    print("\nYou won!")
else:
    print("\nYou were defeated...")