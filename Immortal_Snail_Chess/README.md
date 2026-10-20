# Immortal Snail Chess

A chess variant where an immortal snail slowly hunts the kings and deletes anything unfortunate enough to share its square.

## The Rules

- At the start of the game, the snail spawns at a random position on the 8×8 board, determined by rolling 2d8.
- Every 3 full turns (White -> Black -> White -> Black -> White -> Black), the snail moves one square toward the nearest king.
- The snail moves like a king, including diagonally.
- The snail chooses a square closer to its target king than its current square.
- Any piece the snail lands on is permanently removed from the game.
- The snail cannot be captured. Attempting to capture it destroys the attacking piece and incurs the snail's ire.
- The snail is immortal. This is not up for debate.

### Unresolved Rules

- What happens when both kings are equally close to the snail?
  - Flip a coin
- What exactly does incurring the snail's ire do?
  - The coin hates you now
- What happens when the snail reaches a king?
  - Presumably, the king dies and you lose

## Current Implementation

The game is written in Python using Pygame Community Edition (`pygame-ce`).

Currently implemented:
- Pygame window with an 800×800 display.
- Chessboard background texture.
- Textures for all 12 chess piece types (6 per color).
- `Piece` class storing a piece's name, board coordinates, and image.
- `Snail` class storing the snail's name, coordinates, and image.
- Standard chess starting positions.
- Random initial snail position.
- Board-state synchronization that removes overlapping pieces, including pieces occupying the snail's starting square.
- Rendering of the board, pieces, and snail.

Not implemented yet:
- Player input and piece movement.
- Legal chess moves and captures.
- Turn tracking.
- Snail movement and its three-full-turn timer.
- King targeting and tie-breaking.
- Win/loss conditions.
- Multiplayer or AI opponents.

## Running the Game

Install Pygame Community Edition:

```bash
pip install pygame-ce
```

Run the game from the project root:

```bash
python assets/src/main.py
```

The code imports the module as `pygame`, even though the installed distribution is named `pygame-ce`.

## Architecture Notes

- `PIECES` is a dictionary containing loaded and scaled piece images, indexed by names such as `"white_king"` and `"black_pawn"`.
- `pieces` is a list of `Piece` instances currently on the board.
- `board_state` is intended to represent the board as an 8×8 grid, indexed as `board_state[y][x]`. Each occupied square references its corresponding `Piece` instance; empty squares contain `None`.
- `Snail` stores its position in board coordinates, from 0 to 7 on each axis.
- `TILE_WIDTH` and `TILE