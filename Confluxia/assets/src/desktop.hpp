#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <array>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <random>
#include <chrono>
#include <thread>
#include "../data/lore.hpp"
#include "../data/modifiers.hpp"
#include "../data/moves.hpp"
#include "../data/pets.hpp"
#include "../data/status_effects.hpp"
using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::unordered_map;
using std::find;
namespace desktop{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::bernoulli_distribution coin_flip(0.5);
    const vector<string> basic_powers={"fire","metal","wood","earth","water"};
    const vector<string> alignments={"light","dark"};
    const vector<string> cosmic_powers={"space","time"};
    const std::array<string,5> rarities={"common","uncommon","rare","epic","legendary"};
    struct move{
        string name;
        int damage;
        int cooldown;
        string type;
        string level;
    };
    struct pet{
        string name;
        string type;
        string rarity;
        string buffed_stat;
        string move;
        string description;
    };
    unordered_map<string,move> load_moves() {
        unordered_map<string,move> result;
        for(const auto& data:confluxed_assets::moves){result.emplace(string(data.id),move{string(data.name),data.damage,data.cooldown,string(data.type),string(data.level)});}
        return(result);
    }
    unordered_map<string,pet> load_pets() {
        unordered_map<string,pet> result;
        for(const auto& data:confluxed_assets::pets){result.emplace(string(data.id),pet{string(data.name),string(data.type),string(data.rarity),string(data.buffed_stat),string(data.move),string(data.description)});}
        return(result);
    }
    unordered_map<string,string> load_lore() {
        unordered_map<string,string> result;
        for(const auto& data:confluxed_assets::lore){result.emplace(string(data.id),string(data.text));}
        return(result);
    }
    unordered_map<string,vector<string>> load_modifiers() {
        unordered_map<string,vector<string>> result;
        for(const auto& data:confluxed_assets::modifiers){result[string(data.id)]=vector<string>(data.targets.begin(),data.targets.end());}
        return(result);
    }
    const unordered_map<string,move>moves=load_moves();
    const unordered_map<string,pet>pets=load_pets();
    const unordered_map<string,string>lore_defs=load_lore();
    const unordered_map<string,vector<string>> modifiers=load_modifiers();
    void print(string text){
        for(size_t i=0,len=text.size();i<len;++i){
            cout<<text[i]<<std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(3)); //for testing, changed to 3ms. change back to 30 when done
        }
    }
    string input(string prompt,vector<string>valid_options={},bool options=true){
        vector<string> printed_options=valid_options;
        while(true){
            string response;
            print(prompt);
            print(" ");
            if(!valid_options.empty()){
                if(printed_options==vector<string>{"y/n"}){
                    valid_options={"yes","no","y","n"};
                }
                if(options){
                    print("(");
                    for(size_t i=0;i<printed_options.size()-1;i++){
                        print(printed_options[i]);
                        if(i<printed_options.size()-2){print(", ");}
                    }
                    if(printed_options.size()>1){print(" or ");}
                    print(printed_options.back()+") ");
                }
            }
            std::getline(cin,response);
            string response_lower=response;
            std::transform(response_lower.begin(),response_lower.end(),response_lower.begin(),[](unsigned char c){return std::tolower(c);});
            if(!valid_options.empty()){
                bool valid=false;
                for(const auto& option:valid_options){
                    string option_lower=option;
                    std::transform(option_lower.begin(),option_lower.end(),option_lower.begin(),[](unsigned char c){return std::tolower(c);});
                    if(response_lower==option_lower){
                        valid=true;
                        response=option;
                        break;
                    }
                }
                if(!valid){
                    print("Invalid input. Please choose a valid option. \n");
                }else{
                    if(valid_options==vector<string>{"yes","no","y","n"}){
                        if(response_lower=="y"){response="yes";}
                        else if(response_lower=="n"){response="no";}
                    }
                    return(response);
                }
            }else{
                if(valid_options==vector<string>{"yes","no","y","n"}){
                    if(response_lower=="y"){response="yes";}
                    else if(response_lower=="n"){response="no";}
                }
                return(response);
            }
        }
    }
    struct stat_block{
        int speed;
        int attack;
        int defense;
        int health;
        int max_health;
    };
    struct power_construct{
        string basic;
        string alignment;
        string cosmic;
    };
    struct enemy{
        string name;
        stat_block stats;
        int bar;
        power_construct powers;
        vector<string> known_moves;
        vector<string> pets;
        unordered_map<string,int>cooldown_times={};
        power_construct memory;
    };
    struct player{
        string name;
        int rare_traits=0;
        unordered_map<string,int>cooldown_times={};
        vector<string> known_moves;
        vector<string> pets;
        stat_block stats{10,10,10,100,100};
        int bar=0;
        power_construct powers;
        player(){
            name=input("What would you like to name your character?");
            print("Welcome, "+name+"! Let's get started. \n");
            bool randomize=input("Would you like to randomize your character's stats and powers?",{"y/n"})=="yes";
            if(randomize){
                vector<string> basic_options={"fire","metal","wood","earth","water","fire","metal","wood","earth","water","nexus"};
                std::uniform_int_distribution<size_t> basic_dist(0,basic_options.size()-1);
                powers.basic=basic_options[basic_dist(gen)];
                vector<string> alignment_options={"light","light","light","light","dark","dark","dark","dark","objectivity"};
                std::uniform_int_distribution<size_t> alignment_dist(0,alignment_options.size()-1);
                powers.alignment=alignment_options[alignment_dist(gen)];
                vector<string> cosmic_options={"space","space","space","space","space","time","time","time","time","time","axiom"};
                std::uniform_int_distribution<size_t> cosmic_dist(0,cosmic_options.size()-1);
                powers.cosmic=cosmic_options[cosmic_dist(gen)];
            }else{
                powers.basic=input("What would you like your character's basic power to be?",basic_powers);
                powers.alignment=input("What would you like your character's alignment to be?",alignments);
                powers.cosmic=input("What would you like your character's cosmic power to be?",cosmic_powers);
            }
            std::vector<std::string> basic_starter_moves={"flame_burst", "iron_spike", "splinter", "pebble_shot", "water_jet"};
            auto basic_it=find(basic_powers.begin(),basic_powers.end(),powers.basic);
            size_t index=basic_it-basic_powers.begin();
            if(index<basic_starter_moves.size()){known_moves.push_back(basic_starter_moves[index]);} 
            else{known_moves.insert(known_moves.end(),basic_starter_moves.begin(),basic_starter_moves.end());}
            std::vector<std::string> alignment_starter_moves={"light_beam", "void_strike"};
            auto alignment_it=find(alignments.begin(),alignments.end(),powers.alignment);
            index=alignment_it-alignments.begin();
            if(index<alignment_starter_moves.size()){known_moves.push_back(alignment_starter_moves[index]);} 
            else{known_moves.insert(known_moves.end(),alignment_starter_moves.begin(),alignment_starter_moves.end());}
            std::vector<std::string> cosmic_starter_moves={"space_rift", "chronic_chakram"};
            auto cosmic_it=find(cosmic_powers.begin(),cosmic_powers.end(),powers.cosmic);
            index=cosmic_it-cosmic_powers.begin();
            if(index<cosmic_starter_moves.size()){known_moves.push_back(cosmic_starter_moves[index]);} 
            else{known_moves.insert(known_moves.end(),cosmic_starter_moves.begin(),cosmic_starter_moves.end());}
            if(powers.basic=="nexus"){rare_traits++;}
            if(powers.alignment=="objectivity"){rare_traits++;}
            if(powers.cosmic=="axiom"){rare_traits++;}
        }
    };
    string get_lore(const player&player){
        string lore="";
        string basic_power_upper=player.powers.basic;
        basic_power_upper[0]=static_cast<char>(std::toupper(static_cast<unsigned char>(basic_power_upper[0])));
        string alignment_power_upper=player.powers.alignment;
        alignment_power_upper[0]=static_cast<char>(std::toupper(static_cast<unsigned char>(alignment_power_upper[0])));
        string cosmic_power_upper=player.powers.cosmic;
        cosmic_power_upper[0]=static_cast<char>(std::toupper(static_cast<unsigned char>(cosmic_power_upper[0])));
        if(player.rare_traits==0){
            lore+="You have the power of "+player.powers.basic+". "+basic_power_upper+" is "+lore_defs.at(player.powers.basic)+" \n";
            lore+="You have the power of "+player.powers.alignment+". "+alignment_power_upper+" is "+lore_defs.at(player.powers.alignment)+" \n";
            lore+="You have the power of "+player.powers.cosmic+". "+cosmic_power_upper+" is "+lore_defs.at(player.powers.cosmic)+" ";
        }else if(player.rare_traits==1){
            if(player.powers.basic=="nexus"){
                lore+="You are the Nexus. "+lore_defs.at("nexus")+"\n";
                lore+="You have the power of "+player.powers.alignment+". "+alignment_power_upper+" is "+lore_defs.at(player.powers.alignment)+" \n";
                lore+="You have the power of "+player.powers.cosmic+". "+cosmic_power_upper+" is "+lore_defs.at(player.powers.cosmic)+" ";
            }
            else if(player.powers.alignment=="objectivity"){
                lore+="You have the power of "+player.powers.basic+". "+basic_power_upper+" is "+lore_defs.at(player.powers.basic)+" \n";
                lore+="You are the Objective. "+lore_defs.at("objectivity")+"\n";
                lore+="You have the power of "+player.powers.cosmic+". "+cosmic_power_upper+" is "+lore_defs.at(player.powers.cosmic)+" ";
        }
            else{
                lore+="You have the power of "+player.powers.basic+". "+basic_power_upper+" is "+lore_defs.at(player.powers.basic)+" \n";
                lore+="You have the power of "+player.powers.alignment+". "+alignment_power_upper+" is "+lore_defs.at(player.powers.alignment)+" \n";
                lore+="You are the Axiom. "+lore_defs.at("axiom");
            }
        }else if(player.rare_traits==2){
            if(player.powers.basic=="nexus"){
                if(player.powers.alignment=="objectivity"){
                    lore+="You are the Nexus of Objectivity. "+lore_defs.at("nexus_objectivity")+"\n";
                    lore+="You have the power of "+player.powers.cosmic+". "+cosmic_power_upper+" is "+lore_defs.at(player.powers.cosmic)+" ";
                }else{
                    lore+="You have the power of "+player.powers.alignment+". "+alignment_power_upper+" is "+lore_defs.at(player.powers.alignment)+" \n";
                    lore+="You are the Nexus of Axiom. "+lore_defs.at("nexus_axiom");
                }
            }else{
                lore+="You have the power of "+player.powers.basic+". "+basic_power_upper+" is "+lore_defs.at(player.powers.basic)+" \n";
                lore+="You are the Axiom of Objectivity. "+lore_defs.at("objectivity_axiom");
            }
        }else{lore+=lore_defs.at("absolute");}
        return lore;
    }
    int get_damage(const bool apply_cooldown,unordered_map<string,int>& attacker_cooldown_times,const stat_block& attacker_stats,const stat_block& attackee_stats,const power_construct& attackee_types,string attacking_move){
        const string attack_type=moves.at(attacking_move).type;
        string defender_type;
        if(find(basic_powers.begin(),basic_powers.end(),attack_type)!=basic_powers.end()){defender_type=attackee_types.basic;}
        else if(find(alignments.begin(),alignments.end(),attack_type)!=alignments.end()){defender_type=attackee_types.alignment;}
        else if(find(cosmic_powers.begin(),cosmic_powers.end(),attack_type)!=cosmic_powers.end()){defender_type=attackee_types.cosmic;}
        else{defender_type="";}
        int damage_multipliernum=1;
        int damage_multiplierden=1;
        int lvlmod;
        if(moves.at(attacking_move).level=="basic"){lvlmod=2;}
        else if(moves.at(attacking_move).level=="alignment"){lvlmod=3;}
        else if(moves.at(attacking_move).level=="cosmic"){lvlmod=4;}
        else{throw(std::invalid_argument("No move level found"));}
        if(find(modifiers.at(attack_type).begin(),modifiers.at(attack_type).end(),defender_type)!=modifiers.at(attack_type).end()){damage_multipliernum=lvlmod;}
        else if(find(modifiers.at(defender_type).begin(),modifiers.at(defender_type).end(),attack_type)!=modifiers.at(defender_type).end()){damage_multiplierden=lvlmod;}
        if(apply_cooldown){attacker_cooldown_times[attacking_move]=moves.at(attacking_move).cooldown;}
        return(static_cast<int>(std::round(static_cast<double>(moves.at(attacking_move).damage)*static_cast<double>(attacker_stats.attack)/static_cast<double>(attackee_stats.defense)*static_cast<double>(damage_multipliernum)/static_cast<double>(damage_multiplierden))));
    }
    bool battle_loop(player& player,enemy& enemy,bool favor){
        int bar=std::max(player.stats.speed,enemy.stats.speed)+1;
        bool turn;
        vector<string> available_moves;
        player.bar+=player.stats.speed;
        enemy.bar+=enemy.stats.speed;
        bool dbar=false;
        while(player.bar>=bar&&enemy.bar>=bar){
            player.bar-=bar;
            enemy.bar-=bar;
            dbar=true;
        }
        if(dbar){
            if (player.bar>=enemy.bar){turn=true;}
            else{turn=false;}
        }else{
            if(player.bar>=bar){turn=true;}
            else if(enemy.bar>=bar){turn=false;}
            else{
                if(player.stats.speed>enemy.stats.speed){turn=true;}
                else if(player.stats.speed<enemy.stats.speed){turn=false;}
                else{turn=favor;}
            }
        }
        favor=!turn;
        if(turn){
            player.bar-=bar;
            available_moves.clear();
            for(size_t i=0;i<player.known_moves.size();++i){if(player.cooldown_times.find(player.known_moves[i])==player.cooldown_times.end()){available_moves.push_back(player.known_moves[i]);}}
            print("You can use the following moves: \n");
            for(size_t i=0;i<available_moves.size();++i){
                string cooldown;
                if(moves.at(available_moves[i]).cooldown==1){cooldown="no";}
                else{cooldown=std::to_string(moves.at(available_moves[i]).cooldown-1)+"-turn";}
                print(moves.at(available_moves[i]).name+": "+std::to_string(moves.at(available_moves[i]).damage)+" damage, "+cooldown+" cooldown \n");
            }
            unordered_map<string,string> move_lookup;
            for(const auto& move_id:available_moves){move_lookup[moves.at(move_id).name]=move_id;}
            vector<string> available_move_names;
            for(const auto& pair:move_lookup){available_move_names.push_back(pair.first);}
            string move_to_use=input("What move would you like to use?",{available_move_names},false);
            string move_to_use_id=move_lookup[move_to_use];
            int damage=get_damage(true,player.cooldown_times,player.stats,enemy.stats,enemy.powers,move_to_use_id);
            enemy.stats.health-=damage;
            if(moves.at(move_to_use_id).level=="basic"){
                if(enemy.memory.basic!=moves.at(move_to_use_id).type&&enemy.memory.basic!="nexus"){
                    if(enemy.memory.basic==""){enemy.memory.basic=moves.at(move_to_use_id).type;}
                    else{enemy.memory.basic="nexus";}
                }
            }else if(moves.at(move_to_use_id).level=="alignment"){
                if(enemy.memory.alignment!=moves.at(move_to_use_id).type&&enemy.memory.alignment!="objectivity"){
                    if(enemy.memory.alignment==""){enemy.memory.alignment=moves.at(move_to_use_id).type;}
                    else{enemy.memory.alignment="objectivity";}
                }
            }else if(moves.at(move_to_use_id).level=="cosmic"){
                if(enemy.memory.cosmic!=moves.at(move_to_use_id).type&&enemy.memory.cosmic!="axiom"){
                    if(enemy.memory.cosmic==""){enemy.memory.cosmic=moves.at(move_to_use_id).type;}
                    else{enemy.memory.cosmic="axiom";}
                }
            }
            print("You used "+moves.at(move_to_use_id).name+" and dealt "+std::to_string(damage)+" damage to "+enemy.name+"! \n");
            for(auto it=player.cooldown_times.begin();it!=player.cooldown_times.end();){
                it->second--;
                if(it->second<=0){it=player.cooldown_times.erase(it);}
                else{it++;}
            }
        }else{
            enemy.bar-=bar;
            for(size_t i=0;i<enemy.known_moves.size();++i){if(enemy.cooldown_times.find(enemy.known_moves[i])==enemy.cooldown_times.end()){available_moves.push_back(enemy.known_moves[i]);}}
            string best_move;
            if(!available_moves.empty()){
                best_move=available_moves[0];
            }
            int best_damage=0;
            for(const auto& move_id:available_moves){
                int damage=get_damage(false,enemy.cooldown_times,enemy.stats,player.stats,enemy.memory,move_id);
                if(damage>best_damage){
                    best_damage=damage;
                    best_move=move_id;
                }
            }
            const int actual_damage=get_damage(true,enemy.cooldown_times,enemy.stats,player.stats,player.powers,best_move);
            const int expected_damage=get_damage(false,enemy.cooldown_times,enemy.stats,player.stats,enemy.memory,best_move);
            player.stats.health-=actual_damage;
            print(enemy.name+" used "+moves.at(best_move).name+" and dealt "+std::to_string(actual_damage)+" damage to you! \n"+"You have "+std::to_string(player.stats.health)+" health remaining. \n");
            if(actual_damage!=expected_damage){
                if(moves.at(best_move).level=="basic"){enemy.memory.basic=player.powers.basic;}
                else if(moves.at(best_move).level=="alignment"){enemy.memory.alignment=player.powers.alignment;}
                else if(moves.at(best_move).level=="cosmic"){enemy.memory.cosmic=player.powers.cosmic;}
            }
            for(auto it=enemy.cooldown_times.begin();it!=enemy.cooldown_times.end();){
                it->second--;
                if(it->second<=0){it=enemy.cooldown_times.erase(it);}
                else{it++;}
            }
        }
        return favor;
    }
    string hp_print(int player_health,int enemy_health,string enemy_name){
        if(enemy_health<=0){return("You have defeated "+enemy_name+"! \n");}
        else if(player_health<=0){return("You have been defeated by "+enemy_name+". \n");}
        else{
            if(static_cast<double>(enemy_health-player_health)/player_health>0.0){
                return(enemy_name+" has "+std::to_string(static_cast<int>(std::round((static_cast<double>(enemy_health-player_health)/player_health)*10000)/100))+"% more health than you. \n");
            }else if(static_cast<double>(enemy_health-player_health)/player_health<0.0){
                return(enemy_name+" has "+std::to_string(static_cast<int>(0-std::round((static_cast<double>(enemy_health-player_health)/player_health)*10000)/100))+"% less health than you. \n");
            }else{
                return(enemy_name+" has the same health as you. \n");
            }
        }
    }
    void stat_change(stat_block& stats,string stat,int change){
        if(stat=="speed"){stats.speed+=change;}
        else if(stat=="attack"){stats.attack+=change;}
        else if(stat=="defense"){stats.defense+=change;}
        else if(stat=="health"){stats.max_health+=change;stats.health=stats.max_health;}
        else{throw(std::invalid_argument("No stat found"));}
    }
    void run(){
        print("Welcome to the game! You are a player in a world of magic and adventure. You will be able to choose your character's stats and powers, and then embark on a journey to defeat the evil forces that threaten the land. \n");
        player player;
        print(player.name+" has been created with the following stats: \n");
        print("Attack: "+std::to_string(player.stats.attack)+" \n");
        print("Speed: "+std::to_string(player.stats.speed)+" \n");
        print("Defense: "+std::to_string(player.stats.defense)+" \n");
        print("Max Health: "+std::to_string(player.stats.max_health)+" \n");
        print(get_lore(player)+"\n");
        print("You are now ready to embark on your journey. Good luck, and may the forces of magic be with you! \n");
        enemy bob{"bob",{10,10,10,100,100},0,{},{},{},{},{}};
        std::uniform_int_distribution<size_t> basic_dist(0,basic_powers.size()-1);
        bob.powers.basic=basic_powers[basic_dist(gen)];
        std::uniform_int_distribution<size_t> alignment_dist(0,alignments.size()-1);
        bob.powers.alignment=alignments[alignment_dist(gen)];
        std::uniform_int_distribution<size_t> cosmic_dist(0,cosmic_powers.size()-1);
        bob.powers.cosmic=cosmic_powers[cosmic_dist(gen)];
        for(const auto& [id,val]:moves){
            if(val.type==bob.powers.basic||val.type==bob.powers.alignment||val.type==bob.powers.cosmic){
                if(coin_flip(gen)){
                    bob.known_moves.push_back(id);
                }
            }
        }
        if(bob.known_moves.empty()){
            for(const auto& [id,val]:moves){
                if(val.type==bob.powers.basic||val.type==bob.powers.alignment||val.type==bob.powers.cosmic){
                    bob.known_moves.push_back(id);
                }
            }
        }
        bool win=false;
        while(!win){
            if(input("Would you like to check out the pets?",{"y/n"})=="yes"){
                std::bernoulli_distribution same_type(0.1);
                const bool option_1_same_type=same_type(gen);
                const bool option_2_same_type=same_type(gen);
                const bool option_3_same_type=same_type(gen);
                vector<string> option_1_options;
                vector<string> option_2_options;
                vector<string> option_3_options;
                for(const auto& pet:pets){
                    if((pet.second.type==player.powers.basic)||((player.powers.basic=="nexus"||option_1_same_type)&&find(basic_powers.begin(),basic_powers.end(),pet.second.type)!=basic_powers.end())){
                        for(size_t i=0;i<std::distance(find(rarities.begin(),rarities.end(),pet.second.rarity),rarities.end())+1;++i){
                            option_1_options.push_back(pet.first);
                        }
                    }
                }
                for(const auto& pet:pets){
                    if((pet.second.type==player.powers.alignment)||((player.powers.alignment=="objectivity"||option_2_same_type)&&find(alignments.begin(),alignments.end(),pet.second.type)!=alignments.end())){
                        for(size_t i=0;i<std::distance(find(rarities.begin(),rarities.end(),pet.second.rarity),rarities.end())+1;++i){
                            option_2_options.push_back(pet.first);
                        }
                    }
                }
                for(const auto& pet:pets){
                    if((pet.second.type==player.powers.cosmic)||((player.powers.cosmic=="axiom"||option_3_same_type)&&find(cosmic_powers.begin(),cosmic_powers.end(),pet.second.type)!=cosmic_powers.end())){
                        for(size_t i=0;i<std::distance(find(rarities.begin(),rarities.end(),pet.second.rarity),rarities.end())+1;++i){
                            option_3_options.push_back(pet.first);
                        }
                    }
                }
                if(option_1_options.empty()||option_2_options.empty()||option_3_options.empty()){throw std::runtime_error("No valid pets found for one or more power types.");}
                std::uniform_int_distribution<size_t> option_1_dist(0,option_1_options.size()-1);
                std::uniform_int_distribution<size_t> option_2_dist(0,option_2_options.size()-1);
                std::uniform_int_distribution<size_t> option_3_dist(0,option_3_options.size()-1);
                const string option_1_id=option_1_options[option_1_dist(gen)];
                const string option_2_id=option_2_options[option_2_dist(gen)];
                const string option_3_id=option_3_options[option_3_dist(gen)];
                pet option_1=pets.at(option_1_id);
                pet option_2=pets.at(option_2_id);
                pet option_3=pets.at(option_3_id);
                print("You come across a few pets on your journey. \n");
                print("A "+option_1.rarity+" "+option_1.type+" "+option_1.description+" "+option_1.name+" has the move "+moves.at(option_1.move).name+"\n");
                print("A "+option_2.rarity+" "+option_2.type+" "+option_2.description+" "+option_2.name+" has the move "+moves.at(option_2.move).name+"\n");
                print("A "+option_3.rarity+" "+option_3.type+" "+option_3.description+" "+option_3.name+" has the move "+moves.at(option_3.move).name+"\n");
                const string choice=input("Which pet would you like to add to your collection?",{option_1.name,option_2.name,option_3.name,"none"});
                if(choice==option_1.name){
                    player.pets.push_back(option_1_id);
                    stat_change(player.stats,option_1.buffed_stat,10);
                    player.known_moves.push_back(option_1.move);
                    print(option_1.name+" has been added to your collection! \n");
                }else if(choice==option_2.name){
                    player.pets.push_back(option_2_id);
                    stat_change(player.stats,option_2.buffed_stat,10);
                    player.known_moves.push_back(option_2.move);
                    print(option_2.name+" has been added to your collection! \n");
                }else if(choice==option_3.name){
                    player.pets.push_back(option_3_id);
                    stat_change(player.stats,option_3.buffed_stat,10);
                    player.known_moves.push_back(option_3.move);
                    print(option_3.name+" has been added to your collection! \n");
                }else{
                    print("You decided not to add any pets to your collection. \n");
                }
            }else{
                print("You decided not to add any pets to your collection. \n");
            }
            print("You have encountered "+bob.name+"! Prepare for battle!\nYou have "+std::to_string(player.stats.speed)+" SPD, "+std::to_string(player.stats.attack)+" ATK, "+std::to_string(player.stats.defense)+" DFN, "+std::to_string(player.stats.health)+" HLT\n");
            bool favor=coin_flip(gen);
            while(player.stats.health>0&&bob.stats.health>0){
                favor=battle_loop(player,bob,favor);
                print(hp_print(player.stats.health,bob.stats.health,bob.name));
            }
            if(player.stats.health>0){print("Congratulations! You have won the battle! \n");win=true;}
            else{print("You have lost the battle. ");}
            player.stats.health=player.stats.max_health;
            bob.stats.health=bob.stats.max_health;
            player.cooldown_times.clear();
            bob.cooldown_times.clear();
        }
    }
}