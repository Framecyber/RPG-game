from rpg.characters import Player, NPC
from rpg.settings import (PLAYER_DEFAULT_HEALTH, NPC_DEFAULT_HEALTH, 
                        PLAYER_DEFAULT_ATTACK, PLAYER_DEFAULT_DEFENSE,
                        NPC_DEFAULT_ATTACK, NPC_DEFAULT_DEFENSE,
                        PLAYER_DEFAULT_NAME, NPC_DEFAULT_NAME)
from rpg.map import GAME_MAP, display_map, move_player, player_x as initial_player_x, player_y as initial_player_y

# Global variables for player position, to be updated by move_player
player_x = initial_player_x
player_y = initial_player_y

def player_action_attack(player, target_npc):
    # Player ends their defense at the start of their attack turn
    if player.is_defending:
        player.end_defense()

    # NPCs currently don't defend, but if they did, similar logic:
    # if target_npc.is_defending:
    #     target_npc.end_defense() # Or apply defense bonus to NPC

    damage = max(0, player.attack_power - target_npc.defense_power)
    target_npc.health -= damage
    print(f"{player.name} attacks {target_npc.name} for {damage} damage!")

def player_action_defend(player):
    player.start_defense()
    # Message printed by start_defense in Character class

def npc_behavior(npc, player):
    # NPC ends its defense at the start of its turn (if it was defending)
    if npc.is_defending: # Though NPCs don't defend yet
        npc.end_defense()

    # Player's defense is applied here
    effective_defense = player.defense_power
    if player.is_defending:
        effective_defense *= 2 # Double defense if player is defending
        print(f"{player.name} is defending, doubling defense to {effective_defense}!")
    
    damage = max(0, npc.attack_power - effective_defense)
    player.health -= damage
    print(f"{npc.name} attacks {player.name} for {damage} damage!")
    
    # Player's defense, if active, ends after this attack
    if player.is_defending:
        player.end_defense()


def display_combat_status(player, npc):
    print("\\n--- Your Stats ---")
    print(f"Name: {player.name}")
    print(f"Health: {player.health}/{player.max_health}")
    print("\\n--- Enemy Stats ---")
    print(f"Name: {npc.name}")
    print(f"Health: {npc.health}/{npc.max_health}")

def combat_round(player, npc):
    display_combat_status(player, npc)

    action_taken = False
    while not action_taken:
        print("\\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Do nothing")
        choice = input("Enter action (1-3): ")

        if choice == "1":
            player_action_attack(player, npc) # Player's defense (if any) ends here
            action_taken = True
            if npc.is_alive():
                npc_behavior(npc, player) # Player's defense (if chosen) applies here
        elif choice == "2":
            player_action_defend(player)
            action_taken = True
            # NPC attacks player who is now defending
            if npc.is_alive(): # Check if NPC is still alive before it attacks
                 npc_behavior(npc, player)
        elif choice == "3":
            if player.is_defending: # If player was defending and chose to do nothing
                player.end_defense()
            print(f"{player.name} does nothing.")
            action_taken = True
            if npc.is_alive(): # Check if NPC is still alive
                npc_behavior(npc, player) # Player's defense is not active
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    if not npc.is_alive():
        print(f"\\n{npc.name} has been defeated!")
    elif not player.is_alive():
        print(f"\\n{player.name} has been defeated!")

def main():
    player = Player(name="Hero", 
                    health=PLAYER_DEFAULT_HEALTH, 
                    max_health=PLAYER_DEFAULT_HEALTH, 
                    attack_power=PLAYER_DEFAULT_ATTACK, 
                    defense_power=PLAYER_DEFAULT_DEFENSE)
    
    npc = NPC(name="Goblin", 
              health=NPC_DEFAULT_HEALTH, 
              max_health=NPC_DEFAULT_HEALTH, 
              attack_power=NPC_DEFAULT_ATTACK, 
              defense_power=NPC_DEFAULT_DEFENSE)

    print(f"A wild {npc.name} appears! Time to explore.")

    game_state = "explore" # Can be "explore" or "combat"
    
    # Main game loop
    while True:
        if game_state == "explore":
            display_map(GAME_MAP, player_x, player_y)
            action = input("Enter move (N, S, E, W) or 'quit': ").upper()

            if action == "QUIT":
                print("Exiting game.")
                break
            elif action in ["N", "S", "E", "W"]:
                moved, new_x, new_y = move_player(action, GAME_MAP, player_x, player_y)
                if moved:
                    globals()['player_x'] = new_x
                    globals()['player_y'] = new_y
                    if GAME_MAP[new_y][new_x] == 'N':
                        print(f"You encounter {npc.name}!")
                        # Reset NPC for combat
                        npc.health = npc.max_health
                        npc.end_defense() # Ensure NPC isn't stuck defending
                        player.end_defense() # Ensure player isn't stuck defending from previous unfinished states
                        game_state = "combat"
            else:
                print("Invalid action. Try again.")

        elif game_state == "combat":
            print(f"\\n--- Engaging {npc.name} in Combat! ---")
            # NPC health is reset when combat is initiated from explore state.
            turn = 1
            while player.is_alive() and npc.is_alive():
                print(f"\\n--- Round {turn} ---")
                combat_round(player, npc)
                
                if not npc.is_alive():
                    print(f"\\nVictory! {player.name} defeated {npc.name}.")
                    # Player health regeneration
                    health_regained = player.max_health // 2
                    player.health = min(player.max_health, player.health + health_regained)
                    print(f"{player.name} regained {health_regained} health. Current health: {player.health}/{player.max_health}.")
                    game_state = "explore" 
                    # NPC 'N' remains on map, can be fought again.
                    break 
                if not player.is_alive():
                    print(f"\\nGame Over! {player.name} was defeated by {npc.name}.")
                    return # Exit main function, thus ending the game.
                turn += 1
            
            if game_state == "explore": 
                print(f"Returning to exploration.")
            elif not player.is_alive(): 
                print("\\n--- Final Status ---")
                display_combat_status(player, npc)
                break


if __name__ == "__main__":
    main()
