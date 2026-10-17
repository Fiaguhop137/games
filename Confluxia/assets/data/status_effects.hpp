#pragma once
#include <string_view>
namespace confluxed_assets{
    struct status_effect_data{
        std::string_view id;
        std::string_view name;
        std::string_view affected_stat;
        std::string_view description;
        std::string_view type;
    };
    constexpr status_effect_data status_effects[]={
        {"blind","Blinded","attack","unable to see, reducing accuracy and damage output.","debuff"},
        {"burn","Burned","health","suffers damage over time due to burns.","debuff"},
        {"insomnia","Insomniac","speed","unable to sleep, reducing speed and stamina.","debuff"},
        {"echoes","Echoes","defense","suffers from echoes, reducing defense and resistance.","debuff"},
        {"huge","Huge","defense","increased size, increasing durability output.","buff"},
        {"swift","Swift","speed","increased speed, allowing for faster actions and reactions.","buff"},
        {"lucky","Lucky","attack","increased luck, improving critical hit chance and item drops.","buff"},
        {"regeneration","Regeneration","health","recovered health over time.","buff"},
    };
}
