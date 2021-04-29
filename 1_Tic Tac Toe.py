first_player_rounds = 0
second_player_rounds = 0
first_player_name = ' ' * 50
second_player_name = ' ' * 50
player_order = 0
player_mode = ''


def timer_multiplayer():
    clear_screen()
    import time
    print('****************************************************')
    print('*                                                  *')
    print("*  You can't beat me. Don't take it personally :)  *")
    print('*                                                  *')
    print('****************************************************')
    time.sleep(1)
    clear_screen()


def single_multiplayer():
    print('Welcome to Tic Tac Toe game!\n')
    global player_mode
    while player_mode not in ['s', 'S', 'm', 'M']:
        player_mode = input('\nSelect Single Player or Multiplayer mode ("S" or "M"): ').upper()
    clear_screen()


def random_player_choise():
    import random
    global player_order
    player_order = random.randint(1, 2)


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game(board):
    clear_screen()

    spaces_before_player1 = ' ' * (10 - len(first_player_name))

    print(f'\n{spaces_before_player1}{first_player_name} | {second_player_name}\n'
          f'\n     ({first_player_rounds})   |   ({second_player_rounds})\n'
          f'\n  *******************\n'
          f'  *  -------------  *\n'
          f'  *  | {board[7]} | {board[8]} | {board[9]} |  *\n'
          f'  *  -------------  *\n'
          f'  *  | {board[4]} | {board[5]} | {board[6]} |  *\n'
          f'  *  -------------  *\n'
          f'  *  | {board[1]} | {board[2]} | {board[3]} |  *\n'
          f'  *  -------------  *\n'
          f'  *******************\n')


def choose_symbol_p2p():
    global fpm, spm, first_player_name, second_player_name

    while len(first_player_name) > 10:
        first_player_name = input('Enter the first player name: ')
        if len(first_player_name) > 10:
            print('Too Long!\nMaximum 10 characters.')
    while len(second_player_name) > 10:
        second_player_name = input('Enter the second player name: ')
        if len(second_player_name) > 10:
            print('Too Long!\nMaximum 10 characters.')

    clear_screen()

    while fpm not in ['X', 'x', 'O', 'o', '0']:
        fpm = input(f'\nPlease, select what {first_player_name} plays with (X or O): ')
    if fpm in ['X', 'x']:
        fpm = 'X'
        spm = 'O'
    else:
        fpm = 'O'
        spm = 'X'


def choose_symbol_single():
    global fpm, first_player_name, second_player_name, spm

    while len(first_player_name) > 10:
        first_player_name = input('Enter the your name: ')
        if len(first_player_name) > 10:
            print('Too Long!\nMaximum 10 characters.')

    clear_screen()

    second_player_name = 'Computer'

    while fpm not in ['X', 'x', 'O', 'o', '0']:
        fpm = input(f'\n{first_player_name}, select what you want to play with (X or O): ')
    if fpm in ['X', 'x']:
        fpm = 'X'
        spm = 'O'
    else:
        fpm = 'O'
        spm = 'X'


def user_input_p2p(board, fpm, spm, first_player_name, second_player_name):
    global player_order

    player_input = 0
    while player_input not in range(1, 10):
        if player_order == 1:
            player_input = input(f'{first_player_name} it is you turn (use your numpad): ')
        else:
            player_input = input(f'{second_player_name} it is you turn (use your numpad): ')
        if player_input.isdigit():
            player_input = int(player_input)

    if player_order == 1 and board[player_input] != 'X' and board[player_input] != 'O':
        board[player_input] = fpm
        player_order = 2
    elif player_order == 2 and board[player_input] != 'X' and board[player_input] != 'O':
        board[player_input] = spm
        player_order = 1

    return board


def input_single(board, fpm, first_player_name):
    global player_order

    player_input = 0
    while player_input not in range(1, 10):
        player_input = input(f'{first_player_name} it is you turn (use your numpad): ')
        player_input = int(player_input)

    if board[player_input] != 'X' and board[player_input] != 'O':
        board[player_input] = fpm
        player_order = 2

    return board


def positions(board):
    def rot_1(board):
        rot_board_1 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_1[1] = board[1], 1
        rot_board_1[2] = board[2], 2
        rot_board_1[3] = board[3], 3
        rot_board_1[4] = board[4], 4
        rot_board_1[5] = board[5], 5
        rot_board_1[6] = board[6], 6
        rot_board_1[7] = board[7], 7
        rot_board_1[8] = board[8], 8
        rot_board_1[9] = board[9], 9
        return rot_board_1

    def rot_2(board):
        rot_board_2 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_2[3] = board[1], 9
        rot_board_2[6] = board[2], 8
        rot_board_2[9] = board[3], 7
        rot_board_2[2] = board[4], 6
        rot_board_2[5] = board[5], 5
        rot_board_2[8] = board[6], 4
        rot_board_2[1] = board[7], 3
        rot_board_2[4] = board[8], 2
        rot_board_2[7] = board[9], 1
        return (rot_board_2)

    def rot_3(board):
        rot_board_3 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_3[9] = board[1], 1
        rot_board_3[8] = board[2], 2
        rot_board_3[7] = board[3], 3
        rot_board_3[6] = board[4], 4
        rot_board_3[5] = board[5], 5
        rot_board_3[4] = board[6], 6
        rot_board_3[3] = board[7], 7
        rot_board_3[2] = board[8], 8
        rot_board_3[1] = board[9], 9
        return (rot_board_3)

    def rot_4(board):
        rot_board_4 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_4[7] = board[1], 9
        rot_board_4[4] = board[2], 8
        rot_board_4[1] = board[3], 7
        rot_board_4[8] = board[4], 6
        rot_board_4[5] = board[5], 5
        rot_board_4[2] = board[6], 4
        rot_board_4[9] = board[7], 3
        rot_board_4[6] = board[8], 2
        rot_board_4[3] = board[9], 1
        return (rot_board_4)

    def rot_5(board):
        rot_board_5 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_5[3] = board[1], 1
        rot_board_5[2] = board[2], 2
        rot_board_5[1] = board[3], 3
        rot_board_5[6] = board[4], 4
        rot_board_5[5] = board[5], 5
        rot_board_5[4] = board[6], 6
        rot_board_5[9] = board[7], 7
        rot_board_5[8] = board[8], 8
        rot_board_5[7] = board[9], 9
        return (rot_board_5)

    def rot_6(board):
        rot_board_6 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_6[7] = board[1], 1
        rot_board_6[8] = board[2], 2
        rot_board_6[9] = board[3], 3
        rot_board_6[4] = board[4], 4
        rot_board_6[5] = board[5], 5
        rot_board_6[6] = board[6], 6
        rot_board_6[1] = board[7], 7
        rot_board_6[2] = board[8], 8
        rot_board_6[3] = board[9], 9
        return (rot_board_6)

    def rot_7(board):
        rot_board_7 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_7[9] = board[1], 1
        rot_board_7[6] = board[2], 2
        rot_board_7[3] = board[3], 3
        rot_board_7[8] = board[4], 4
        rot_board_7[5] = board[5], 5
        rot_board_7[2] = board[6], 6
        rot_board_7[7] = board[7], 7
        rot_board_7[4] = board[8], 8
        rot_board_7[1] = board[9], 9
        return (rot_board_7)

    def rot_8(board):
        rot_board_8 = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rot_board_8[1] = board[1], 1
        rot_board_8[4] = board[2], 2
        rot_board_8[7] = board[3], 3
        rot_board_8[2] = board[4], 4
        rot_board_8[5] = board[5], 5
        rot_board_8[8] = board[6], 6
        rot_board_8[3] = board[7], 7
        rot_board_8[6] = board[8], 8
        rot_board_8[9] = board[9], 9
        return (rot_board_8)

    position_rot = [rot_1(board), rot_2(board), rot_3(board), rot_4(board), rot_5(board), rot_6(board), rot_7(board),
                    rot_8(board)]

    return position_rot


def comp_input(spm, rot_positions):
    global board, player_order
    # CHECK FOR WINNING MOVE
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[1] == spm and check_rotation[2] == spm and check_rotation[3] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[4] == spm and check_rotation[5] == spm and check_rotation[6] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 6:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[1] == spm and check_rotation[3] == spm and check_rotation[2] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 2:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[4] == spm and check_rotation[6] == spm and check_rotation[5] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[1] == spm and check_rotation[5] == spm and check_rotation[9] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation[7] == spm and check_rotation[3] == spm and check_rotation[5] != fpm:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    # comp is first
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
            import random
            first_comp_input = random.randint(1, 4)
            if first_comp_input == 1:
                board = [0, spm, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            elif first_comp_input == 2:
                board = [0, ' ', ' ', spm, ' ', ' ', ' ', ' ', ' ', ' ']
            elif first_comp_input == 3:
                board = [0, ' ', ' ', ' ', ' ', ' ', ' ', spm, ' ', ' ']
            else:
                board = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', spm]
    # FIRST CHAIN
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, ' ', ' ', spm, ' ', ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1

    # END FIRST CHAIN

    # CHAIN 2
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', ' ', ' ', ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', spm, ' ', ' ', fpm, fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1
    # END CHAIN 2

    # CHAIN 3
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', fpm, ' ', ' ', ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', fpm, ' ', fpm, ' ', ' ', ' ', spm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1
    # END CHAIN 3

    # CHAIN 4
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', ' ', ' ', ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', spm, fpm, ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', fpm, ' ', spm, ' ', ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 6:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', fpm, fpm, spm, spm, ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 8:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, fpm, fpm, spm, spm, ' ', spm, fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1
    # END CHAIN 4

    # CHAIN 5
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', fpm, ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', fpm, ' ', fpm, ' ', ' ', ' ', spm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', ' ', fpm, fpm, ' ', ' ', spm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 4:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, ' ', ' ', spm, fpm, fpm, fpm, ' ', spm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, spm, spm, fpm, fpm, fpm, ' ', spm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 8:
                    board[return_position] = spm
                    break
                return_position += 1

    # END CHAIN 5
    # END COMP IS FIRST

    # COMP IS SECOND
    # CHAN 1
    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] or check_rotation == [0, ' ', fpm, ' ',
                                                                                                    ' ', ' ', ' ', ' ',
                                                                                                    ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 5:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, fpm, ' ', ' ', spm, ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, fpm, spm, ' ', spm, ' ', fpm, ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 4:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, fpm, spm, spm, spm, fpm, fpm, ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 8:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', ' ', spm, ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 1:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', fpm, ' ', spm, ' ', ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 2:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, spm, fpm, ' ', spm, ' ', ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 4:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, spm, fpm, spm, spm, fpm, ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', ' ', ' ', spm, fpm, ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 2:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, spm, ' ', ' ', spm, fpm, ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, spm, fpm, ' ', spm, fpm, spm, fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', ' ', ' ', spm, ' ', ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 4:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', ' ', spm, spm, fpm, ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, fpm, ' ', spm, spm, spm, fpm, fpm, ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 8:
                    board[return_position] = spm
                    break
                return_position += 1
    # END CHAIN 1

    # CHAIN 2

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', ' ', spm, fpm, ' ', ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 3:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, spm, ' ', spm, fpm, fpm, ' ', ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 1:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, spm, ' ', spm, fpm, fpm, ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 8:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', ' ', spm, ' ', ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 6:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', fpm, spm, spm, ' ', ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, fpm, fpm, spm, spm, spm, ' ', fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 1:
                    board[return_position] = spm
                    break
                return_position += 1

    # END CHAIN 2
    # CHAIN 3

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', ' ', spm, ' ', ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 4:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, ' ', fpm, ' ', spm, spm, fpm, ' ', fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 1:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, ' ', spm, spm, fpm, fpm, fpm, ' ']:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 9:
                    board[return_position] = spm
                    break
                return_position += 1

    for x in rot_positions:
        check_rotation = []
        for rot_val, true_val in x:
            check_rotation.append(rot_val)

        if check_rotation == [0, spm, fpm, ' ', spm, spm, fpm, ' ', fpm, fpm]:
            return_position = 0
            for rot_val, true_val in x:
                if true_val == 7:
                    board[return_position] = spm
                    break
                return_position += 1
    #END CHAIN 3
    #CHAIN 5


    player_order = 1


def check_win_multiplayer(board):
    global winner, first_player_rounds, second_player_rounds

    if (board[7] == board[8] == board[9] != ' ' or
            board[4] == board[5] == board[6] != ' ' or
            board[1] == board[2] == board[3] != ' ' or
            board[7] == board[4] == board[1] != ' ' or
            board[8] == board[5] == board[2] != ' ' or
            board[9] == board[6] == board[3] != ' ' or
            board[1] == board[5] == board[9] != ' ' or
            board[7] == board[5] == board[3] != ' '):
        winner = True

        if player_order == 2:
            first_player_rounds += 1
        elif player_order == 1:
            second_player_rounds += 1

        clear_screen()
        display_game(board)

        if player_order == 2:
            print(f'\n{first_player_name} wins.\nCongratulations!\n')
        else:
            print(f'\n{second_player_name} wins.\nCongratulations!\n')

    elif (board[1] == 'X' or board[1] == 'O') and (board[2] == 'X' or board[2] == 'O') and (
            board[3] == 'X' or board[3] == 'O') and (board[4] == 'X' or board[4] == 'O') and (
            board[5] == 'X' or board[5] == 'O') and (board[6] == 'X' or board[6] == 'O') and (
            board[7] == 'X' or board[7] == 'O') and (board[8] == 'X' or board[8] == 'O') and (
            board[9] == 'X' or board[9] == 'O'):
        clear_screen()
        display_game(board)
        print('\nNo one wins this round!\n')
        winner = True


def check_win_single(board):
    global winner, first_player_rounds, second_player_rounds

    if (board[7] == board[8] == board[9] != ' ' or
            board[4] == board[5] == board[6] != ' ' or
            board[1] == board[2] == board[3] != ' ' or
            board[7] == board[4] == board[1] != ' ' or
            board[8] == board[5] == board[2] != ' ' or
            board[9] == board[6] == board[3] != ' ' or
            board[1] == board[5] == board[9] != ' ' or
            board[7] == board[5] == board[3] != ' '):
        winner = True

        if player_order == 2:
            first_player_rounds += 1
        elif player_order == 1:
            second_player_rounds += 1

        clear_screen()
        display_game(board)

        if player_order == 2:
            print(f'\n{first_player_name} wins.\nCongratulations!\n')
        else:
            print("\nComputer wins!\nTold you that you can't beat me!")

    if (board[1] == 'X' or board[1] == 'O') and (board[2] == 'X' or board[2] == 'O') and (
            board[3] == 'X' or board[3] == 'O') and (board[4] == 'X' or board[4] == 'O') and (
            board[5] == 'X' or board[5] == 'O') and (board[6] == 'X' or board[6] == 'O') and (
            board[7] == 'X' or board[7] == 'O') and (board[8] == 'X' or board[8] == 'O') and (
            board[9] == 'X' or board[9] == 'O'):
        clear_screen()
        display_game(board)
        print('\nNo one wins this round!\n')
        winner = True


def continue_():
    global going_on
    want_continue = ''
    while want_continue not in ['Y', 'N', 'y', 'n']:
        want_continue = input('Do you want to keep playing? (Y or N): ')
    if want_continue.upper() == 'N':
        going_on = False
    else:
        clear_screen()


fpm = ''
spm = ''

going_on = True

while going_on:
    board = [' '] * 10
    winner = False

    single_multiplayer()
    random_player_choise()

    player_order = 1

    if player_mode == "M":
        # Multiplayer Mode
        choose_symbol_p2p()
        while not winner:
            display_game(board)

            user_input_p2p(board, fpm, spm, first_player_name, second_player_name)

            check_win_multiplayer(board)

        continue_()
    else:
        # Single Player Mode

        timer_multiplayer()
        choose_symbol_single()
        positions(board)

        while not winner:
            display_game(board)

            if player_order == 1:
                input_single(board, fpm, first_player_name)
            else:
                rot_positions = positions(board)
                comp_input(spm, rot_positions)

            check_win_single(board)

        continue_()
