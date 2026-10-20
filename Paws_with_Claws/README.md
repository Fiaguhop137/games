# Paws with Claws

A browser game with a kawaii pastel-pink aesthetic, built with HTML, CSS, and JavaScript.

## Current Implementation

- Centered title screen with a welcome message and Start Game button.
- Enter key support for starting the game.
- Full-viewport game screen with four directional arrows.
- Arrow key controls that change each arrow's appearance while pressed.
- Responsive title sizing using CSS `clamp()`.
- Pastel pink styling, rounded corners, borders, shadows, and button animations.
- SVG assets for directional arrows and the Enter key icon.

## Controls

| Input | Action |
|---|---|
| Enter | Start the game from the title screen |
| Up Arrow | Press the up arrow |
| Down Arrow | Press the down arrow |
| Left Arrow | Press the left arrow |
| Right Arrow | Press the right arrow |

Directional arrows return to their normal appearance when their keys are released.

## Running the Game

Open `index.html` in a web browser.

No compilation or installation is required.

## Architecture Notes

- `index.html` loads the stylesheet and JavaScript.
- `styles/style.css` defines the pastel color palette, title screen, button interactions, and directional arrow positioning.
- `scripts/script.js` creates the interface, handles keyboard input, and swaps arrow images.
- `textures/` contains the SVG graphics used by the interface.

The game screen uses absolutely positioned directional indicators arranged around the center of the viewport. The title screen is centered using CSS transforms.

## Not Implemented Yet

- Player movement or other gameplay mechanics.
- Objectives, scoring, or win conditions.
- Sound effects and music.
- A way to return to the title screen.