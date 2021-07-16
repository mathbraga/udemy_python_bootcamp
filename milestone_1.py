def display_board(board):
    row1 = f" {board[6]} | {board[7]} | {board[8]} "
    row2 = f" {board[3]} | {board[4]} | {board[5]} "
    row3 = f" {board[0]} | {board[1]} | {board[2]} "
    print("   |   |   ")
    print(row1)
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(row2)
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(row3)
    print("   |   |   ")

def choose_player():
    has_chosen = False
    player1 = ''
    player2 = ''
    players = []

    while not has_chosen:
        player1 = input(f"Player 1: Do you want to be 'X' or 'O'? ").upper()
        if player1 not in ['X', 'O']:
            print("Please type X or O")
        else:
            if player1 == 'X':
                player2 = 'O'
                has_chosen = True
                print(f"Player 1 is {player1}.")
                print(f"Player 2 is {player2}.")
            elif player1 == 'O':
                player2 = 'X'
                has_chosen = True
                print(f"Player 1 is {player1}.")
                print(f"Player 2 is {player2}.")
    players = [player1, player2]
    return players

def choose_play(player, board_state):
    board = board_state
    next_pos = '0'

    while not next_pos.isdigit() or int(next_pos) not in range(1, 10):
        next_pos = input(f"Player ({player}): Choose next position (1-9). ")
        if not next_pos.isdigit():
            print("Please type a number in between 1 and 9.")
        elif int(next_pos) not in range(1, 10):
            print("Please type a number in between 1 and 9.")
        elif board[int(next_pos) - 1] != ' ':
            print("Position occupied, choose another one.")
            next_pos = '0'
    
    board[int(next_pos) - 1] = player
    return board

def check_game_end(board, player):
    if player == board[0] == board[1] == board[2]\
        or player == board[3] == board[4] == board[5]\
        or player == board[6] == board[7] == board[8]\
        or player == board[0] == board[4] == board[8]\
        or player == board[2] == board[4] == board[6]\
        or player == board[0] == board[3] == board[6]\
        or player == board[1] == board[4] == board[7]\
        or player == board[2] == board[5] == board[8]:
        return [True, player]
    elif ' ' in board:
        return [False, ' ']
    else:
        return [True, '']


def play_game(p1, p2):
    board_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_is_active = True
    game_over = None
    is_winner = None
    active_player = p1

    print(f"Player 1 ({p1}) goes 1st.")
    while game_is_active:
        display_board(board_state)
        board_state = choose_play(active_player, board_state)
        game_over, is_winner = check_game_end(board_state, active_player)

        if game_over:
            if len(is_winner) > 0:
                display_board(board_state)
                print(f"({is_winner}) is the winner.")
                game_is_active = False
            else:
                display_board(board_state)
                print(f"It is a tie.")
                game_is_active = False
        else:
            active_player = p1 if active_player == p2 else p2

        play_again = ' '
        if game_is_active == False:
            while play_again not in ['Y', 'N']:
                play_again = input("Would you like to play again (Y/N)? ").upper()
                if play_again not in ['Y', 'N']:
                    print("Please answer 'Y' for yes or 'N' for no.")
            if play_again == 'N':
                print("Game closed.")
            elif play_again == 'Y':
                print("Welcome to TicTacToe.")
                board_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                active_player = p1 if active_player == p2 else p2
                print(f"({active_player}) is the one that goes 1st now.")
                game_is_active = True

print("Welcome to TicTacToe.")
player1, player2 = choose_player()
play_game(player1, player2)