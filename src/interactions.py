import random


def get_player_input(board):
    """
    Return the player input
    :param board: for checking the target
    :return: option selected and the target
    """
    while True:
        try:
            option = str(input("Shoot(S) or Move(M)?: ")).lower()
            assert option in ['s', 'm']
            break
        except (ValueError, AssertionError):
            print("Invalid option: Type Shoot(S) or Move(M)")

    while True:
        try:
            target = int(input("Where to?: "))
        except ValueError:
            print("Invalid room number")
            continue

        if option == 'm':
            try:
                assert target in board.cave[board.player_position]
                break
            except AssertionError:
                print("Unreachable room. Use one of the adjacent rooms")
        elif option == 's':
            search_result = board.search(board.player_position, target)
            try:
                assert search_result[0]
                break
            except AssertionError:
                if search_result[1] == -1:
                    print("This room does not exist in the cave")
                    target = random.choice(board.cave.keys())

                if search_result[1] > board.arrow_travel_distance:
                    print("Arrows aren't that crooked")
    return option, target


def get_player_game_option():
    """
    :return: The game option setting for the board and the number of arrows
    """
    while True:
        try:
            option = str(input("Hard(H), Normal(N) or Easy(E)?: ")).lower()
            assert option in ['h', 'n', 'e']
            break
        except (ValueError, AssertionError):
            print("Invalid game option: Type Hard(H), Normal(N) or Easy(E)")

    if option == 'h':
        return ['bat', 'bat', 'pit', 'pit', 'pit', 'pit', 'pit', 'wumpus'], 3
    elif option == 'n':
        return ['bat', 'bat', 'pit', 'pit', 'wumpus'], 5
    elif option == 'e':
        return ['bat', 'pit', 'wumpus'], 5


def get_player_game_name():
    """
    :return: The player name for the score
    """
    option = str(input("Type your name: ")[:15])
    if option.strip() == '':
        option = "new user"
    return option.upper()


def print_alerts(rival):
    """Print an alert when entering a room
    """
    if rival == 'bat':
        print("You hear a rustling")
    elif rival == 'pit':
        print("You feel a cold wind blowing from a nearby cavern")
    elif rival == 'wumpus':
        print("You smell something terrible nearby")


class Interactions:
    pass
