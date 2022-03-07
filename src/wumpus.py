import os
import random
from time import sleep
from subprocess import call

import interactions
from points import Points
from instructions import Instructions
from board import Board
from files import Files
from score import Score


def shoot_room(room_number, board, score):
    """Controls when shooting in a room
    """
    print("Shooting an arrow into room {}".format(room_number))
    board.arrows -= 1
    rival = board.rivals.get(room_number)
    if rival in ['bat', 'wumpus']:
        del board.rivals[room_number]
        if rival == 'wumpus':
            score.update_score(board, "Yeah, you killed the wumpus!", Points.kill_wumpus)
            return -1
        elif rival == 'bat':
            score.update_score(board, "You killed a bat", Points.kill_bat)
    elif rival in ['pit', None]:
        score.update_score(board, "This arrow is lost", Points.arrow_lost)

    if board.arrows < 1:
        print("Your quiver is empty")
        return -1

    if random.random() < 0.75:
        for room_number, rival in board.rivals.items():
            if rival == 'wumpus':
                wumpus_position = room_number
        new_position = random.choice(list(set(board.cave[wumpus_position]).difference(board.rivals.keys())))
        del board.rivals[room_number]
        board.rivals[new_position] = 'wumpus'
        if new_position == board.player_position:
            print("Wumpus enters your room and eats you!")
            return -1
    return board.player_position


class HuntWumpus(object):

    def enter_room(self, room_number, board, score):
        """Controls when entering a new room
        """
        print("")
        score.update_score(board, "Entering room {}".format(room_number), Points.zero)

        current_rival = board.rivals.get(room_number)
        if current_rival == 'bat':
            score.update_score(board, "You encounter a bat, it transports you to a random empty room", Points.bat_transport)
            return self.enter_room(random.choice(board.get_free_rooms()), board, score)
        elif current_rival == 'wumpus':
            score.update_score(board, "Wumpus eats you", Points.zero)
            return -1
        elif current_rival == 'pit':
            score.update_score(board, "You fall into a pit", Points.zero)
            return -1
        else:
            print("")
            for i in board.cave[room_number]:
                interactions.print_alerts(board.rivals.get(i))

            return room_number

    def main_loop(self):
        Instructions().show_header()
        sleep(3)
        Instructions().show_instructions()
        board = Board()
        score = Score()
        my_options = interactions.get_player_game_option()
        board.fill_cave_game_option(my_options[0], my_options[1])
        self.enter_room(board.player_position, board, score)

        while True:
            print("You are in room {}".format(board.player_position))
            print("Tunnels lead to: {0} {1} {2}".format(*board.cave[board.player_position]))

            player_input = interactions.get_player_input(board)

            if player_input[0] == 'm':
                score.update_with_movement(Points.movement)
                board.player_position = self.enter_room(player_input[1], board, score)
            elif player_input[0] == 's':
                board.player_position = shoot_room(player_input[1], board, score)
            elif player_input[0] == 'q':
                board.player_position = -1

            if board.player_position == -1:
                break

        Instructions().show_game_over()
        player_name = interactions.get_player_game_name()
        clear()
        Instructions().print_score_list(
            Files().save_new_score(player_name, score.current_score))


def clear():
    # for windows
    _ = call('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    bl = HuntWumpus()
    bl.main_loop()
