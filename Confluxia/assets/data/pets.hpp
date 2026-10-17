#pragma once
#include <string_view>
namespace confluxed_assets{
    struct pet_data{
        std::string_view id;
        std::string_view name;
        std::string_view type;
        std::string_view rarity;
        std::string_view buffed_stat;
        std::string_view move;
        std::string_view description;
    };
    constexpr pet_data pets[]={
        {"flickerkit","Flickerkit","fire","common","speed","flame_burst","kitten made of flickering flames. It zooms around, leaving a trail of sparks in its wake."},
        {"emberpaw","Emberpaw","fire","uncommon","attack","fireball","rabbit whose glowing paws leave embers in every footprint. It's powerful hind legs leave a trail of burning pawprints."},
        {"plasmeow","Plasmeow","fire","rare","attack","heat_wave","lion, flame-maned and proud, that can turn an entire battlefield into a shimmering heat haze with its fiery breath."},
        {"ironpup","Ironpup","metal","common","defense","iron_spike","puppy with a body of polished iron. The mischievous little creature is nearly bulletproof, but its shiny coat is a bit of a giveaway."},
        {"shardhound","Shardhound","metal","uncommon","health","shard_spray","hound whose reflective coat sheds razor-sharp splinters. It will loyally protect its master, even if it means getting a few dents itself."},
        {"steelmaw","Steelmaw","metal","rare","attack","knife_storm","wolf forged of blades and steel. Its hulking frame is covered in jagged edges, and its jaws are a whirling storm of serrated knives."},
        {"spriglet","Spriglet","wood","common","health","splinter","dryad that leaves a trail of fresh green shoots. While shy at first, it will grow to trust its master and protect them with its own life force."},
        {"vinelash","Vinelash","wood","uncommon","defense","vine_whip","pet. This entity is only seen with the trail of foliage that follows its every step. It camouflages so well nobody truly knows what they look like."},
        {"verdantail","Verdantail","wood","rare","speed","leaf_storm","equine guardian, whose flowing mane is a whirling canopy of leaves. While plantlike and ancient in appearance, it can gallop at speeds that rival the wind."},
        {"pebblit","Pebblit","earth","common","health","pebble_shot","lamb that collects interesting stones in its fur pouch. Its round, soft, body, and gentle, generous nature make it a favorite among children and elderly."},
        {"quakeling","Quakeling","earth","uncommon","defense","tremor","ram whose every stomp makes the ground hum. Sure-footed and strong, its rock-hard hooves can withstand the most violent of earthquakes without faltering."},
        {"cragodon","Cragodon","earth","rare","attack","boulder_crush","crocodile strong enough to split a cliff with swing of its tail. Its Atlas-sized jaws can crush boulders with ease."},
        {"droplet","Droplet","water","common","defense","water_jet","fish that can dart through the air on a stream of water. This bubbly little creature is surprisingly resilient, and can survive in both water and air with ease."},
        {"surgefin","Surgefin","water","uncommon","speed","tidal_wave","dolphin whose swift fins carry the pull of the tide. It can leap from the water and ride the waves with ease, and is known to save drowning sailors."},
        {"leviathan","Leviathan","water","rare","health","flood","colossal deep-water serpent that follows the oldest ocean currents. It is said that the Leviathan can swallow entire ships whole, leaving only a trail of foam behind."},
        {"glimmerflap","Glimmerflap","light","common","speed","light_beam","chick that shines brightest when someone needs guidance. It's inquisitive nature leads it to quickly investigate curiosities."},
        {"solavis","Solavis","light","uncommon","attack","solar_flare","fox with a warm glow that chases shadows from the wilds. It is said that their very presence can banish unholy spirits."},
        {"luminar","Luminar","light","rare","speed","radiant_burst","winged guardian that scatters brilliant motes with every beat of its wings. Its form is most often seen as a beam of light with feathery angelic wings"},
        {"photonix","Photonix","light","epic","attack","photon_bolt","celestial bird that crosses the sky as a streak of living light. This radiant being is able to focus the sun's rays into a single, devastating beam of energy."},
        {"shadelet","Shadelet","dark","common","defense","void_strike","tiny feline shaped shadow with no feline casting it. A shadow cannot be injured, and this little creature is able to slip through the cracks of reality to do the same."},
        {"gloamclaw","Gloamclaw","dark","uncommon","speed","shadow_flux","silent panther that melts into darkness if you look too closely. Its able to travel near instantly from any shadow to any other."},
        {"dreadfur","Dreadfur","dark","rare","health","nightmare","velvet-furred leopard whose shed furs have been said to cure insomnia. It is said that the Dreadfur can slip into nightmares to comfort it's master."},
        {"umbrael","Umbrael","dark","epic","defense","eclipse","midnight tiger that gathers every nearby shadow beneath its unshattering obsidian claws to create a shadow blacker than the concept of darkness."},
        {"riftling","Riftling","space","common","speed","space_rift","creature with no definable shape that pops in and out of reality. This little curiousity appears to violate relativity."},
        {"orbiton","Orbiton","space","uncommon","health","gravity_well","floating, pure black orb surrounded by miniature floating worlds pulled from distant galaxies. It is said that the Orbiton can create a miniature black hole to swallow its enemies."},
        {"parsecwyrm","Parsecwyrm","space","rare","speed","space_wormhole","starlit wyrm, parsecs long, that coils through wormholes between faraway places. It has a sister, the Epochwyrm, that is said to coil around time itself."},
        {"singularis","Singularis","space","epic","health","singularity","dense, dark, winged creature with a tiny galaxy turning at its core. It looks almost like an unholy angel, with eyes of black holes and a halo of supernovae."},
        {"galaxar","Galaxar","space","legendary","defense","galactic_strike","cosmic dragon whose constellation-marked hide holds the light of vanished stars. It is said that the hide of a Galaxar is strong enough to hold back the force of a dying star."},
        {"ticktail","Ticktail","time","common","speed","chronic_chakram","quick little fox with a clock-face pattern at the tip of its tail. This mischievous little creature is able to steal objects from it's past or future self."},
        {"chronohare","Chronohare","time","uncommon","defense","temporal_loop","long-eared runner that seems to arrive just before it starts moving. It's non-causal nature lets it simply roll back time to avoid injury."},
        {"epochwyrm","Epochwyrm","time","rare","speed","time_wormhole","serpentine wyrm that slips through the seams between one moment and the next. It has a sister, the Parsecwyrm, that is said to coil around space itself."},
        {"fatespinner","Fatespinner","time","epic","speed","fortune","many-legged oracle that weaves glowing threads of possible futures. The Fatespinner can see multiple probable futures at once, and groups of them can be seen weaving the threads of fate for entire civilizations."},
        {"destinarch","Destinarch","time","legendary","speed","destiny","guardian that watches the past and future unfold at once. Its only goal is to keep the mainstream reality along it's predetermined path."},
    };
}
