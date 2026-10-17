import random
BASIC_POWERS=["fire","metal","wood","earth","water"]
ALIGNMENTS=["light","dark"]
COSMIC_POWERS=["space","time"]
POWER_DEFINITIONS={
    "fire":"the power of flames and heat. You are able to control and manipulate flames, creating powerful attacks and defenses. You are also immune to fire and heat, allowing you to withstand extreme temperatures. You deal more damage to metal by melting it, but less to earth because it is not flammable. You have more defense towards wood since you can't put out fire by adding fuel, but less protection from water because water can extinguish fire.",
    "metal":"the power of strength and durability. You are able to control and manipulate metallic substanced, creating powerful weapons and armor. You are also immune to metal-based attacks such as bullets and blades, allowing you to withstand physical damage. You deal more damage to wood by cutting it, but less to water because water can cause rust. You have more defense towards earth since you are heavier than it, but less protection from fire because fire can melt metal.",
    "wood":"the power of growth and nature. You are able to control and manipulate plant life, creating powerful tools and structures. You are also immune to wood-based attacks, allowing you to withstand natural disasters. You deal more damage to earth since tree roots break up, penetrate, and bind soil together, but less to fire since you can't put out fire by adding fuel. You have more defense towards water because you drink water, but less protection from metal because metal can cut wood.",
    "earth":"the power of stability and protection. You are able to control and manipulate dirt, stone, and other earth materials, creating powerful barriers and fortifications. You are also immune to earth-based attacks, allowing you to withstand seismic activity. You deal more damage to water by soaking it up, but less to metal because metal is too durable. You have more defense towards fire you are non flammable, but less protection from wood because tree roots break up, penetrate, and bind soil together.",
    "water":"the power of fluidity and adaptability. You are able to control and manipulate water and ice, creating powerful waves and currents. You are also immune to water-based attacks, allowing you to withstand flooding. You deal more damage to fire by extinguishing it, but less to wood because wood can absorb water. You have more defense towards metal because it sinks in you, but less protection from earth because earth can absorb the water.",
    "light":"the power of illumination and vision. You are able to control and manipulate radiant energy, creating powerful beams and illusions. You are also immune to light-based attacks, allowing you to withstand bright environments. You deal more damage to dark by dispelling it, but take more damage from it as well since it obscures your vision.",
    "dark":"the power of negation and mystery. You are able to control and manipulate the absence of light and the shadows themself, creating powerful voids and illusions. You are also immune to dark-based attacks, allowing you to withstand eerie environments. You deal more damage to light by absorbing it, but take more damage to it as well because it blots out your shadows.",
    "space":"the power of dimensions and travel. You are able to control and manipulate the fabric of space, creating powerful portals and levitations. You are also immune to space-based attacks, allowing you to withstand vacuum and teleportation. You deal more damage to time by disrupting it, but take more damage from it as well since it is not in the 3 dimensions you exist in.",
    "time":"the power of past, present, and future. You are able to control and manipulate the flow of time, creating powerful time loops and see the future. You are also immune to time-based attacks, allowing you to withstand temporal anomalies. You deal more damage to space by disrupting it, but take more damage from it as well since it is not in your domain."}
MOVES={
    "flame_burst":{"name":"Flame Burst","damage":10,"cooldown":1,"type":"fire","level":"basic"},
    "fireball":{"name":"Fireball","damage":13,"cooldown":2,"type":"fire","level":"basic"},
    "heat_wave":{"name":"Heat Wave","damage":17,"cooldown":2,"type":"fire","level":"basic"},
    "iron_spike":{"name":"Iron Spike","damage":10,"cooldown":1,"type":"metal","level":"basic"},
    "shard_spray":{"name":"Shard Spray","damage":15,"cooldown":4,"type":"metal","level":"basic"},
    "knife_storm":{"name":"Knife Storm","damage":15,"cooldown":4,"type":"metal","level":"basic"},
    "splinter":{"name":"Splinter","damage":10,"cooldown":1,"type":"wood","level":"basic"},
    "vine_whip":{"name":"Vine Whip","damage":12,"cooldown":2,"type":"wood","level":"basic"},
    "leaf_storm":{"name":"Leaf Storm","damage":15,"cooldown":3,"type":"wood","level":"basic"},
    "pebble_shot":{"name":"Pebble Shot","damage":10,"cooldown":1,"type":"earth","level":"basic"},
    "tremor":{"name":"Tremor","damage":15,"cooldown":2,"type":"earth","level":"basic"},
    "boulder_crush":{"name":"Boulder Crush","damage":20,"cooldown":5,"type":"earth","level":"basic"},
    "water_jet":{"name":"Water Jet","damage":10,"cooldown":1,"type":"water","level":"basic"},
    "tidal_wave":{"name":"Tidal Wave","damage":15,"cooldown":2,"type":"water","level":"basic"},
    "flood":{"name":"Flood","damage":20,"cooldown":5,"type":"water","level":"basic"},
    "light_beam":{"name":"Light Beam","damage":10,"cooldown":1,"type":"light","level":"alignment"},
    "solar_flare":{"name":"Solar Flare","damage":15,"cooldown":4,"type":"light","level":"alignment"},
    "radiant_burst":{"name":"Radiant Burst","damage":12,"cooldown":3,"type":"light","level":"alignment"},
    "photon_bolt":{"name":"Photon Bolt","damage":20,"cooldown":5,"type":"light","level":"alignment"},
    "void_strike":{"name":"Void Strike","damage":10,"cooldown":1,"type":"dark","level":"alignment"},
    "shadow_flux":{"name":"Shadow Flux","damage":12,"cooldown":3,"type":"dark","level":"alignment"},
    "nightmare":{"name":"Nightmare","damage":15,"cooldown":4,"type":"dark","level":"alignment"},
    "eclipse":{"name":"Eclipse","damage":20,"cooldown":6,"type":"dark","level":"alignment"},
    "space_rift":{"name":"Space Rift","damage":10,"cooldown":1,"type":"space","level":"cosmic"},
    "gravity_well":{"name":"Gravity Well","damage":15,"cooldown":4,"type":"space","level":"cosmic"},
    "space_wormhole":{"name":"Spatial Wormhole","damage":20,"cooldown":5,"type":"space","level":"cosmic"},
    "singularity":{"name":"Singularity","damage":25,"cooldown":6,"type":"space","level":"cosmic"},
    "galactic_strike":{"name":"Galactic Strike","damage":17,"cooldown":3,"type":"space","level":"cosmic"},
    "chronic_chakram":{"name":"Chronic Chakram","damage":10,"cooldown":1,"type":"time","level":"cosmic"},
    "temporal_loop":{"name":"Temporal Loop","damage":19,"cooldown":3,"type":"time","level":"cosmic"},
    "time_wormhole":{"name":"Temporal Wormhole","damage":20,"cooldown":5,"type":"time","level":"cosmic"},
    "fortune":{"name":"Fortune","damage":13,"cooldown":3,"type":"time","level":"cosmic"},
    "destiny":{"name":"Destiny","damage":16,"cooldown":3,"type":"time","level":"cosmic"}
}
def user_input(prompt,valid_options=None):
    user_is_stupid=True
    while user_is_stupid:
        try:
            response=input(f"{prompt} ({', '.join(valid_options[:-1])} or {valid_options[-1]}) ").strip() if valid_options else input(f"{prompt} ").strip()
            if valid_options and response not in valid_options:
                print(f"Invalid input. Please choose {', '.join(valid_options[:-1])} or {valid_options[-1]}.")
                continue
            user_is_stupid=False
            return response
        except Exception as e:
            print(f"Invalid input. Please try again. ({e})")
class stats:
    def __init__(self,attack,speed,defense,health):
        self.attack=attack
        self.speed=speed
        self.defense=defense
        self.health=health
class powers:
    def __init__(self,basic,alignment,cosmic):
        self.basic=basic
        self.alignment=alignment
        self.cosmic=cosmic
class player:
    def __init__(self):
        self.name=user_input("What would you like to name your character?")
        rand=user_input("Would you like to randomize your character's stats and powers?",["yes","no"]).lower()
        if rand=="yes":
            basic=random.choice(BASIC_POWERS*2+["nexus"])
            alignment=random.choice(ALIGNMENTS*4+["objectivity"])
            cosmic=random.choice(COSMIC_POWERS*5+["axiom"])
        else:
            basic=user_input("What would you like your character's basic power to be?",BASIC_POWERS).lower()
            alignment=user_input("What would you like your character's alignment to be?",ALIGNMENTS).lower()
            cosmic=user_input("What would you like your character's cosmic power to be?",COSMIC_POWERS).lower()
        self.stats=stats(10,20,10,100)
        self.powers=powers(basic,alignment,cosmic)
        self.known_moves=["flame_burst"if basic=="fire"else"iron_spike"if basic=="metal"else"splinter"if basic=="wood"else"pebble_shot"if basic=="earth"else"water_jet"]
        self.cooldown_times={}
        self.pets=[]
        self.rare_traits=((self.powers.basic=="nexus")+(self.powers.alignment=="objectivity")+(self.powers.cosmic=="axiom"))
class enemy:
    def __init__(self,name,stats,enemy_powers):
        self.name=name
        self.stats=stats
        self.powers=enemy_powers
        self.memory=powers("","","")
        self.known_moves=[]
        self.cooldown_times={}
def attack(attacker,attackee,move_used):
    attacker.cooldown_times[move_used]=MOVES[move_used]["cooldown"]
    attackee.stats.health-=get_damage(attacker,attackee,move_used)
def get_damage(attacker,attackee,move_used):
    return MOVES[move_used]["damage"]*(attacker.stats.attack/attackee.stats.defense)
def battle_loop(player,enemy,turn):
    if turn==0:
        action="see moves"
        while action=="see moves":    
            action=user_input(f"You have {player.stats.attack} ATK, {player.stats.defense} DFN, {player.stats.speed} SPD, and {player.stats.health} HLT \nWhat would you like to do?",["use move","see moves"])
            if action=="use move":
                available_moves=[move for move in player.known_moves if move not in player.cooldown_times]
                move_lookup={MOVES[move]["name"]: move for move in available_moves}
                move_to_use=user_input("What move would you like to use?",list(move_lookup))
                attack(player,enemy,move_lookup[move_to_use])
            elif action=="see moves":
                print("You can use the following moves: ")
                for move in player.known_moves[:-1]:
                    print(f"{MOVES[move]['name']}: {MOVES[move]['damage']} damage, {MOVES[move]['cooldown']} cooldown")
                print(f"{MOVES[player.known_moves[-1]]['name']}: {MOVES[player.known_moves[-1]]['damage']} damage, {MOVES[player.known_moves[-1]]['cooldown']} cooldown")
    else:
        available_moves=[move for move in enemy.known_moves if move not in enemy.cooldown_times]
        chosen_move=max(available_moves,key=lambda move:get_damage(enemy,player,move))
        attack(enemy,player,chosen_move)
    for move in list(player.cooldown_times):
        player.cooldown_times[move]-=1
        if player.cooldown_times[move]<=0:
            del player.cooldown_times[move]
    for move in list(enemy.cooldown_times):
        enemy.cooldown_times[move]-=1
        if enemy.cooldown_times[move]<=0:
            del enemy.cooldown_times[move]
    return 0 if turn==1 else 1
print("Welcome to the game! You are a player in a world of magic and adventure. You will be able to choose your character's stats and powers, and then embark on a journey to defeat the evil forces that threaten the land.")
player=player()
print(f"""{player.name} has been created with the following stats: 
Attack: {player.stats.attack} 
Speed: {player.stats.speed} 
Defense: {player.stats.defense} 
Health: {player.stats.health} 
{'You are a Nexus!' if player.powers.basic=='nexus' else f'Your Basic Power: {player.powers.basic}'} 
{'You are an Objective!' if player.powers.alignment=='objectivity' else f'Your Alignment: {player.powers.alignment}'} 
{'You are an Axiom!' if player.powers.cosmic=='axiom' else f'Your Cosmic Power: {player.powers.cosmic}'}""")
if player.rare_traits==0:
    print(f"{player.powers.basic.title()} is the {POWER_DEFINITIONS[player.powers.basic]}")
    print(f"{player.powers.alignment.title()} is the {POWER_DEFINITIONS[player.powers.alignment]}")
    print(f"{player.powers.cosmic.title()} is the {POWER_DEFINITIONS[player.powers.cosmic]}")
elif player.rare_traits==1:
    if player.powers.basic=='nexus':
        print("As a Nexus, you have the ability to control all elements and have access to powerful abilities. Use your powers wisely to defeat your enemies and protect the land ")
        print(f"{player.powers.alignment.title()} is the {POWER_DEFINITIONS[player.powers.alignment]}")
        print(f"{player.powers.cosmic.title()} is the {POWER_DEFINITIONS[player.powers.cosmic]}")
    if player.powers.alignment=='objectivity':
        print(f"{player.powers.basic.title()} is the {POWER_DEFINITIONS[player.powers.basic]}")
        print("As an Objective, you have the ability to balance the forces of light and dark and see the true nature of things. Use your powers wisely to maintain harmony in the land ")
        print(f"{player.powers.cosmic.title()} is the {POWER_DEFINITIONS[player.powers.cosmic]}")
    if player.powers.cosmic=='axiom':
        print(f"{player.powers.basic.title()} is the {POWER_DEFINITIONS[player.powers.basic]}")
        print(f"{player.powers.alignment.title()} is the {POWER_DEFINITIONS[player.powers.alignment]}")
        print("As an Axiom, you have the ability to manipulate space and time and have access to powerful abilities. Use your powers wisely to achieve your goals and explore the universe ")
elif player.rare_traits==2:
    if player.powers.basic=='nexus':
        if player.powers.alignment=='objectivity':
            print("As an Objective Nexus, you have the ability to control all elements and balance the forces of light and dark. Use your powers wisely to restore harmony in the land and defeat your enemies ")
            print(f"{player.powers.cosmic.title()} is the {POWER_DEFINITIONS[player.powers.cosmic]}")
        if player.powers.cosmic=='axiom':
            print("As a Nexus, you have the ability to control all elements and have access to powerful abilities. Use your powers wisely to defeat your enemies and protect the land ")
            print(f"{player.powers.alignment.title()} is the {POWER_DEFINITIONS[player.powers.alignment]}")
            print("As an Axiom, you have the ability to manipulate space and time and have access to powerful abilities. Use your powers wisely to achieve your goals and explore the universe ")
    else:
        # If they have 2 rare traits, but not the Nexus trait, we can assume they have the other two rare traits
        print(f"{player.powers.basic.title()} is the {POWER_DEFINITIONS[player.powers.basic]}")
        print("As an Axiomatic Objective, you have the ability to manipulate space and time and balance the forces of light and dark. Use your powers wisely to restore harmony to the land and achieve your goals ")
elif player.rare_traits==3:
    print("Legend has it that one in a thousand people are Axiomatic Objective Nexum, and you are one of them! You have the ability to control all elements, manipulate space and time, and balance the forces of light and dark. Use your powers wisely to restore harmony to the land and achieve your goals ")
print("You are now ready to embark on your journey. Good luck, and may the forces of magic be with you!")
print("first enemy encounter testing an shi")
bob=enemy("Bob",stats(5,10,5,100),powers(random.choice(BASIC_POWERS),random.choice(ALIGNMENTS),random.choice(COSMIC_POWERS)))
bob.known_moves=[move for move,data in MOVES.items()if data["type"] in [bob.powers.basic,bob.powers.alignment,bob.powers.cosmic] and random.choice([True,False])]
if bob.known_moves==[]:bob.known_moves=[move for move,data in MOVES.items()if data["type"] in [bob.powers.basic,bob.powers.alignment,bob.powers.cosmic]]
turn=0
while player.stats.health>0 and bob.stats.health>0:
    turn=battle_loop(player,bob,turn)