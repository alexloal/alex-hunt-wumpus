def print_score(message, arrows, pits, bats, current_score):

    print("{:<75}".format(message),
          "{:>35}".format("ARROWS: "), arrows,
          "{:>7}".format("PITS: "), pits,
          "{:>7}".format("BATS: "), bats,
          "{:>15}".format("SCORE: "), current_score)


class Score:

    def __init__(self):
        self.current_score = 0

    def update_with_movement(self, point):
        self.current_score += point.value

    def update_score(self, board, message, point):
        self.current_score += point.value
        print_score(message, board.arrows, board.get_number_of_pits(), board.get_number_of_bats(), self.current_score)
