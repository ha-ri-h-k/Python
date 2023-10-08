import sys
player_1_choice = 'x'
player_2_choice = 'o'
game_draw = 'DRAW'
grid = [cell for cell in range(9)]
def display_grid():

    print(f"{grid[0]}  {grid[1]}  {grid[2]}")
    print(f"{grid[3]}  {grid[4]}  {grid[5]}")
    print(f"{grid[6]}  {grid[7]}  {grid[8]}")

def check_winner():

    if grid[0] == grid[1] == grid[2]:
        return grid[0]
    elif grid[3] == grid[4] == grid[5]:
        return grid[3]
    elif grid[6] == grid[7] == grid[8]:
        return grid[6]

    # Check for columns
    elif grid[0] == grid[3] == grid[6]:
        return grid[0]

    elif grid[1] == grid[4] == grid[7]:
        return grid[1]

    elif grid[2] == grid[5] == grid[8]:
        return grid[2]

    # Check for diagonal
    elif grid[2] == grid[4] == grid[6]:
        return grid[2]

    elif grid[0] == grid[4] == grid[8]:
        return grid[0]

    # Check for draw.
    else:
        for cell in grid:
            if isinstance(cell, int):
                # Game is ongoing yet not finished
                # Do nothing
                # just return
                return

        return game_draw

def game():
    winner = check_winner()

    if winner == 'x':
        print("X: is the winner")
        display_grid()
        sys.exit()

    elif winner == 'o':
        print("O: is the winner")
        display_grid()
        sys.exit()

    elif winner == game_draw:
        print("Game is a draw ")
        sys.exit()


def update_grid(choice, location):
    """
    choice: 'x' or 'o'
    location: (0 to 8)
    """

    if location < 0 or location > 8:
        raise ValueError("Not a valid location")

    # Check for the occupied condition of grid cell
    if grid[location] == 'x' or grid[location] == 'o':
        raise ValueError(f"Location {location} already filled with {grid[location]}")

    else:
        grid[location] = choice

def main():
    while True:
        try:
            display_grid()
            player_1_location = int(input("Player [x] Enter your choice from (0 to 8): "))
            update_grid(player_1_choice, player_1_location)
        except ValueError as e:
            print(e)
            continue

        game()

        try:
            display_grid()
            player_2_location = int(input("Player [o] Enter your choice from (0 to 8): "))
            update_grid(player_2_choice, player_2_location)
        except ValueError as e:
            print(e)
            continue

        game()
main()