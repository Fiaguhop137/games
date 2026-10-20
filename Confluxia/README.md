# Confluxia

A C++ RPG where you wield elemental, alignment, and cosmic powers, collect magical pets, and fight enemies who gradually learn what you're capable of.

## The Game

- Every character has three power categories: basic, alignment, and cosmic.
- Basic powers are fire, metal, wood, earth, and water.
- Alignment powers are light and dark.
- Cosmic powers are space and time.
- Rare powers exist beyond the normal categories: Nexus, Objectivity, and Axiom.
- Characters begin with 10 speed, 10 attack, 10 defense, and 100 health.
- Powers determine a character's starting moves and contribute to their lore.
- Combat is turn-based, with speed determining turn order and cooldowns restricting move usage.
- Damage depends on the attacker's attack, the defender's defense, the move's base damage, and type interactions.
- Enemies can learn about the player's powers by observing their attacks.
- Players can encounter three pets before battle and choose one to collect. Pets increase a stat by 10 and grant an additional move.
- Pet rarities range from common to legendary.
- The current implementation ends after one battle against Bob.

## Current Implementation

The game is written in C++17 or later and uses a terminal interface.

Currently implemented:
- Character naming and manual or randomized power selection.
- Random generation of basic, alignment, and cosmic powers.
- Rare-trait tracking and special lore for rare power combinations.
- Character stat initialization.
- Data-driven move, pet, lore, and damage modifier definitions.
- Move selection and damage calculation.
- Type-based damage multipliers.
- Speed-based turn scheduling.
- Move cooldown tracking.
- Enemy move selection based on estimated damage.
- Enemy adaptation to the player's powers.
- Randomized pet encounters and pet collection.
- Pet stat bonuses and additional moves.
- Health comparisons and victory/defeat messages.
- Startup license integrity verification using FNV-1a 64-bit hashing.
- Gradual text output with a configurable delay.

Not implemented yet:
- Multiple enemies or a larger progression system.
- Saving and loading character progress.
- A system for retrying after defeat.
- Status effect application and processing.
- Pet abilities beyond stat bonuses and granting moves.
- A graphical interface.
- A complete campaign or exploration system.
- A player inventory or equipment system.

## Running the Game

Compile with a C++17-compatible compiler. Recommended: Use .build.sh

Run the executable from the project root:

```bash
./Confluxia
```

The program checks the `LICENSE` file before launching the game. The file must match the expected hash, and the executable should be run from a working directory where the relative path `LICENSE` resolves correctly.

## Architecture Notes

- `main.cpp` performs the startup license check and calls `desktop::run()`.
- `desktop.hpp` contains the game logic, data loading, character creation, combat, pet encounters, and terminal interaction.
- `data/lore.hpp` defines the descriptions associated with standard powers, rare traits, and their combinations.
- `data/modifiers.hpp` defines which power types have advantages against other types.
- `data/moves.hpp` defines move identifiers, display names, base damage, cooldowns, types, and power categories.
- `data/pets.hpp` defines pet identifiers, names, types, rarities, stat bonuses, associated moves, and descriptions.
- `data/status_effects.hpp` defines potential buffs and debuffs, including blindness, burning, insomnia, and regeneration. These definitions are not yet integrated into the battle loop.

### Data Loading

The `confluxed_assets` namespace contains the game's static content definitions.

`load_moves()`, `load_pets()`, `load_lore()`, and `load_modifiers()` convert these definitions into lookup tables used by the game.

The main lookup tables are:
- `moves`: maps move IDs to their names, damage, cooldowns, types, and categories.
- `pets`: maps pet IDs to their names, types, rarities, stat bonuses, associated moves, and descriptions.
- `lore_defs`: maps power and trait IDs to their lore descriptions.
- `modifiers`: maps power types to the types they are effective against.

### Character State

`player` stores the player's name, powers, stats, known moves, collected pets, cooldowns, and rare-trait count.

`enemy` stores equivalent combat information, along with a `memory` power construct used to track its understanding of the player's powers.

`stat_block` stores speed, attack, defense, current health, and maximum health.

`power_construct` stores the character's basic, alignment, and cosmic powers.

### Combat

`battle_loop()` determines whose turn it is, handles move selection, applies damage, updates cooldowns, and updates the enemy's knowledge of the player's powers.

`get_damage()` calculates damage and optionally applies the move's cooldown.

`hp_print()` reports the relative health of the combatants and detects victory or defeat.

`stat_change()` modifies a character's stats, including maximum health and current health when health is increased.

### Randomization

The game uses `std::mt19937` seeded by `std::random_device` for random selection. Randomness determines randomized character powers, turn-order tie-breaking, enemy powers and moves, and pet encounters.

## License Check

The entry point calculates the FNV-1a 64-bit hash of `LICENSE` and compares it with the expected value.

If the hash does not match, the program prints an error and exits with status code `402`.

This check detects changes to the expected license contents, but it is not a cryptographic signature or a robust security boundary.