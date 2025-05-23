GAME_MAP = [
    "#####",
    "# P #",
    "#   #",
    "#  N#",
    "#####",
]

# Find initial player position
player_x, player_y = -1, -1
for r_idx, row in enumerate(GAME_MAP):
    for c_idx, char in enumerate(row):
        if char == 'P':
            player_x, player_y = c_idx, r_idx
            break
    if player_x != -1:
        break

if player_x == -1: # Should not happen with the default map
    print("Error: Player start position 'P' not found in map. Defaulting to (1,1).")
    player_x, player_y = 1, 1 # Fallback

def display_map(game_map, p_x, p_y):
    """Prints the map, marking the player's current position."""
    print("\\n--- MAP ---")
    for r_idx, row_str in enumerate(game_map):
        display_row = ""
        for c_idx, char_in_map in enumerate(row_str):
            if r_idx == p_y and c_idx == p_x:
                display_row += "@"
            else:
                display_row += char_in_map
        print(display_row)
    print("-----------")

def is_valid_move(game_map, x, y):
    """Checks if the target coordinates (x, y) are within map boundaries and not a wall ('#')."""
    if not (0 <= y < len(game_map) and 0 <= x < len(game_map[0])):
        return False # Out of bounds
    if game_map[y][x] == '#':
        return False # Hit a wall
    return True

def move_player(direction, game_map, current_x, current_y):
    """
    Takes a direction ("N", "S", "E", "W").
    Calculates new coordinates.
    If the move is valid, update player_x, player_y and return True and new coordinates.
    Otherwise, print an error message and return False and old coordinates.
    """
    new_x, new_y = current_x, current_y
    direction = direction.upper()

    if direction == "N":
        new_y -= 1
    elif direction == "S":
        new_y += 1
    elif direction == "E":
        new_x += 1
    elif direction == "W":
        new_x -= 1
    else:
        print("Invalid direction. Use N, S, E, W.")
        return False, current_x, current_y

    if is_valid_move(game_map, new_x, new_y):
        print(f"Moved {direction} to ({new_x}, {new_y}).")
        return True, new_x, new_y
    else:
        print("You can't go that way.")
        return False, current_x, current_y
