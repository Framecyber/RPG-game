# Simple Text-Based RPG

A basic text-based role-playing game implemented in Python. Players can explore a map, encounter NPCs, and engage in turn-based combat.

## Features

*   **Character System**: Player and Non-Player Characters (NPCs) with core stats (health, attack, defense).
*   **Turn-Based Combat**:
    *   Engage in combat with NPCs.
    *   Player can choose to Attack or Defend.
    *   NPCs will retaliate.
    *   Combat messages describe the actions and outcomes.
*   **Map Exploration**:
    *   Navigate a simple grid-based map.
    *   Movement commands: North (N), South (S), East (E), West (W).
    *   Combat is triggered by moving onto an NPC's tile.
*   **Text-Based UI**:
    *   Displays player and NPC stats during combat.
    *   Provides prompts for player actions.
*   **Gameplay**:
    *   Player health regenerates partially after a victorious combat.
    *   NPCs reset for subsequent encounters.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Clone this repository (or download the files).
3.  Navigate to the root directory of the project in your terminal.
4.  Run the game using the command:
    ```bash
    python rpg/game.py
    ```

## Dependencies

The game currently uses only standard Python libraries, so no external dependencies are required.
