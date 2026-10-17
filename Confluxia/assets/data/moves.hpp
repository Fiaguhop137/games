#pragma once
#include <string_view>
#include <vector>
namespace confluxed_assets{
    struct move_data{
        std::string_view id;
        std::string_view name;
        int damage;
        int cooldown;
        std::string_view type;
        std::string_view level;
    };
    const std::vector<move_data> moves={
        {"flame_burst","Flame Burst",10,1,"fire","basic"},
        {"fireball","Fireball",13,2,"fire","basic"},
        {"heat_wave","Heat Wave",17,2,"fire","basic"},
        {"iron_spike","Iron Spike",10,1,"metal","basic"},
        {"shard_spray","Shard Spray",15,4,"metal","basic"},
        {"knife_storm","Knife Storm",15,4,"metal","basic"},
        {"splinter","Splinter",10,1,"wood","basic"},
        {"vine_whip","Vine Whip",12,2,"wood","basic"},
        {"leaf_storm","Leaf Storm",15,3,"wood","basic"},
        {"pebble_shot","Pebble Shot",10,1,"earth","basic"},
        {"tremor","Tremor",15,2,"earth","basic"},
        {"boulder_crush","Boulder Crush",20,5,"earth","basic"},
        {"water_jet","Water Jet",10,1,"water","basic"},
        {"tidal_wave","Tidal Wave",15,2,"water","basic"},
        {"flood","Flood",20,5,"water","basic"},
        {"light_beam","Light Beam",10,1,"light","alignment"},
        {"solar_flare","Solar Flare",15,4,"light","alignment"},
        {"radiant_burst","Radiant Burst",12,3,"light","alignment"},
        {"photon_bolt","Photon Bolt",20,5,"light","alignment"},
        {"void_strike","Void Strike",10,1,"dark","alignment"},
        {"shadow_flux","Shadow Flux",12,3,"dark","alignment"},
        {"nightmare","Nightmare",15,4,"dark","alignment"},
        {"eclipse","Eclipse",20,6,"dark","alignment"},
        {"space_rift","Space Rift",10,1,"space","cosmic"},
        {"gravity_well","Gravity Well",15,4,"space","cosmic"},
        {"space_wormhole","Spatial Wormhole",20,5,"space","cosmic"},
        {"singularity","Singularity",25,6,"space","cosmic"},
        {"galactic_strike","Galactic Strike",17,3,"space","cosmic"},
        {"chronic_chakram","Chronic Chakram",10,1,"time","cosmic"},
        {"temporal_loop","Temporal Loop",19,3,"time","cosmic"},
        {"time_wormhole","Temporal Wormhole",20,5,"time","cosmic"},
        {"fortune","Fortune",13,3,"time","cosmic"},
        {"destiny","Destiny",16,3,"time","cosmic"},
    };
}