import enum


class Points(enum.Enum):
    kill_wumpus = 50
    kill_bat = 20
    arrow_lost = -2
    bat_transport = -5
    movement = -1
    zero = 0
