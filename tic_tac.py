import re

in_game_board = {'0': '', '1': '', '2': '', '3': '', '4': '',
                 '5': '', '6': '', '7': '', '8': '', '9': ''}
help_game_board = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                   '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
win_paths = {'789', '456', '123', '963', '852', '741', '951', '753'}

players = {'1': 'X', '2': 'O'}

found_winner = False

player_one_turn = True


def start_game():
    global found_winner
    global player_one_turn
    welcome_message()

    while not found_winner:
        print("")
        print(f"Player {'1' if player_one_turn else '2'}")
        print("Select a number from 0 - 9")
        print("h = Help board | b = Game board | e = End game")
        print("")
        player_move = input()

        if player_move.lower() == 'h':
            print_game_board(help_game_board)
            continue

        if player_move.lower() == 'b':
            print_game_board(in_game_board)
            continue

        if player_move.lower() == 'e':
            exit()

        if len(''.join(re.findall('\d', player_move))) > 1:
            print("")
            print("Please only enter a number from 0 - 9")
            continue

        if player_move in ''.join([str(x) for x in range(0, 10)]):
            if check_board(player_move):
                continue
            update_board(
                players['1'] if player_one_turn else players['2'], player_move)
            print_game_board(in_game_board)
            found_winner = check_for_winner()
            player_one_turn = not player_one_turn
        else:
            print("Sorry that was invalid, please try again..")

        if found_winner:
            rematch()


def reset():
    for pos in in_game_board:
        in_game_board[pos] = ''


def check_board(player_move):
    if in_game_board[player_move] != '':
        print(f'pos {player_move} has already been selected!')
        return True
    return False


def update_board(player, pos):
    in_game_board[pos] = player


def print_game_board(game_board):
    row = "{:-^17}"
    print("")
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print('{1:>3}{0:>3}{2:>3}{0:>3}{3:>3}'.format(
        '|', game_board['7'], game_board['8'], game_board['9']))
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print(row.format('-'))
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print('{1:>3}{0:>3}{2:>3}{0:>3}{3:>3}'.format(
        '|', game_board['4'], game_board['5'], game_board['6']))
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print(row.format('-'))
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print('{1:>3}{0:>3}{2:>3}{0:>3}{3:>3}'.format(
        '|', game_board['1'], game_board['2'], game_board['3']))
    print('{1:>3}{0:>3}{1:>3}{0:>3}{1:>3}'.format('|', ''))
    print("")


def check_for_win(player):
    player_path = [x for x in in_game_board if in_game_board[x].lower()
                   == player.lower()]
    if len(player_path) < 3:
        return False

    for path in win_paths:
        i = 0
        matches = 0
        while i < len(player_path):
            if player_path[i] in path:
                matches += 1
            i += 1
        if matches == 3:
            return True
    return False


def check_for_winner():
    for player in players:
        if check_for_win(players[player]):
            print(f"Player {player} wins!")
            return True
    return False


def welcome_message():
    print("{:-^17}".format('-'))
    print("Welcome to Tic Tac Py\n")
    print(f"Player 1 will be: '{players['1']}'")
    print(f"Player 2 will be: '{players['2']}'")
    print("")
    print("Hit 'h' to see the game board layout")
    print("{:-^17}".format('-'))


def rematch():
    global found_winner
    global player_one_turn
    print("")
    print("Rematch? y/n")
    decided = False
    while not decided:
        decision = input()
        if decision.lower() == 'y':
            reset()
            player_one_turn = True
            found_winner = False
            decided = True
        elif decision.lower() == 'n':
            decided = True
        else:
            print("")
            print("Invalid choice type either y/n..")


start_game()
