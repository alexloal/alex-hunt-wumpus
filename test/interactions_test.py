import io
import unittest.mock

import interactions
from board import Board
from unittest.mock import patch


class InteractionsTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, input_option, expected_output, mock_stdout):
        interactions.print_alerts(input_option)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def assert_stdout_stdin(self, given_answer, expected_out, board):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            interactions.get_player_input(board)
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def assert_stdout_stdin_check_result(self, given_answer, expected_result, board):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()):
            self.assertEqual(interactions.get_player_input(board), expected_result)

    def test_bat_alert(self):
        self.assert_stdout('bat', 'You hear a rustling\n')

    def test_pit_alert(self):
        self.assert_stdout('pit', 'You feel a cold wind blowing from a nearby cavern\n')

    def test_wumpus_alert(self):
        self.assert_stdout('wumpus', 'You smell something terrible nearby\n')

    def test_player_quit(self):
        self.assert_stdout_stdin_check_result('q', ('q', 0), Board())


if __name__ == '__main__':
    unittest.main()
