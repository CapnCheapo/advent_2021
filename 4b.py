boards = {}
board = {}
entry = []
itemcount = 0
boardcount = 0
won_boards = {}

with open("dataset4b.txt", "r") as items:
    plays = items.readline().strip().split(',')
    for item in items:
        if item.strip():
            for work in item.strip().split():
                entry = [work, False]
                board[itemcount] = entry
                itemcount += 1
                entry = []
                if itemcount % 25 == 0:
                    boards[boardcount] = board
                    board = {}
                    won_boards[boardcount] = False
                    boardcount += 1
                    itemcount = 0


def mark_number(num):
    for markboard in boards:
        for position in boards[markboard]:
            if boards[markboard][position][0] == num:
                boards[markboard][position][1] = True


def win_exists_in_board(check_board):
    possible_wins = [list(range(5)), list(range(5, 10)), list(range(10, 15)), list(range(15, 20)), list(range(20, 25)),
                     list(range(0, 21, 5)), list(range(1, 22, 5)), list(range(2, 23, 5)), list(range(3, 24, 5)),
                     list(range(4, 25, 5))]
    for win_type in possible_wins:
        row_count = 0
        for check_position in win_type:
            if boards[check_board][check_position][1]:
                row_count += 1
        if row_count == 5:
            won_boards[check_board] = True
            return True


def won_last_board():
    win_count = 0
    for won_board in won_boards:
        if won_boards[won_board]:
            win_count += 1
    if win_count == len(won_boards):
        return True
    return False


def tally_board(check_board):
    tally = 0
    for position in boards[check_board]:
        if not boards[check_board][position][1]:
            tally = tally + int(boards[check_board][position][0])
    return tally


for play in plays:
    mark_number(play)
    for board in boards:
        if win_exists_in_board(board) and won_last_board():
            print(f"Magic number: {tally_board(board) * int(play)}")
            exit()
