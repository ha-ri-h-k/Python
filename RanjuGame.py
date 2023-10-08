import random
import time

# Define the game grid
GRID_SIZE = 10
ROAD_WIDTH = 3

# Initialize player position
player_position = GRID_SIZE // 2

# Initialize zombie positions
zombie_positions = [random.randint(0, GRID_SIZE - 1) for _ in range(3)]

# Initialize traffic signal
signal_color = 'green'
signal_timer = 0

# Game loop
while True:
    # Clear the screen
    print("\033[H\033[J")

    # Update and display game grid
    for i in range(GRID_SIZE):
        if i == player_position:
            print("P", end="")
        elif i in zombie_positions:
            print("Z", end="")
        else:
            print(".", end="")
    print("\n" + "=" * (ROAD_WIDTH * GRID_SIZE))

    # Handle player input
    user_input = input("Press 'a' to move left, 'd' to move right, or 'q' to quit: ")
    if user_input == 'q':
        break
    elif user_input == 'a' and player_position > 0:
        player_position -= 1
    elif user_input == 'd' and player_position < GRID_SIZE - 1:
        player_position += 1

    # Update zombie positions
    for i in range(len(zombie_positions)):
        zombie_positions[i] = (zombie_positions[i] + 1) % GRID_SIZE

    # Update traffic signal
    if signal_timer > 0:
        signal_timer -= 1
    else:
        signal_color = random.choice(['green', 'red'])
        signal_timer = random.randint(1, 5)

    # Check for collisions
    if signal_color == 'red' and player_position in zombie_positions:
        print("Game Over - You were caught by a zombie!")
        break

    # Sleep for a short time
    time.sleep(0.5)

print("Thanks for playing!")
