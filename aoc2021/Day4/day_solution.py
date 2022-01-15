import time
from util import *

data = load_and_parse("data.txt")

picks = [int(x) for x in data.pop(0).split(",")]
data.pop(0)

class Number:
    def __init__(self, num):
        self.val = num
        self.active = False

    def is_active(self):
        return 1 if self.active else 0

    def activate(self):
        self.active = True

    def get_val(self, only_active=True):
        if not self.active or not only_active:
            return self.val

        return -1

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"[{self.val}:{self.active}]"

numbers = []
boards = []
for i in range(100):
    numbers.append(Number(i))

picks = [numbers[x] for x in picks]

class Board:
    def __init__(self, board):
        self.board = []
        for i in range(len(board)):
            self.board.append([])
            for j in range(len(board[0])):
                self.board[i].append(numbers[board[i][j]])

    def is_winner(self):
        for i in range(5):
            if sum([x.is_active() for x in self.board[i]]) == 5:
                return True

            if sum([x[i].is_active() for x in self.board]) == 5:
                return True

        # if sum([self.board[x][x].is_active() for x in range(len(self.board))]) == 5:
        #     return True
        #
        # if sum([self.board[x][-(x + 1)].is_active() for x in range(len(self.board))]) == 5:
        #     return True

        return False

    def sum_inactive(self):
        count = 0
        for r in self.board:
            count += sum([max(x.get_val(), 0) for x in r])

        return count

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        res = ""
        for i in range(5):
            res += " ".join([f'{x.get_val():2}' for x in self.board[i]]) + "\n"

        return res


def load_boards(data):
    while len(data) > 0:
        cur_board = []
        for i in range(5):
            cur_board.append([int(x) for x in data.pop(0).strip().split()])

        if len(data) > 0:
            data.pop(0)

        boards.append(Board(cur_board))


def check_boards(boards):
    for idx, b in enumerate(boards):
        if b.is_winner():
            return idx

    return None


load_boards(data)

win_order = []
# print(boards[25])
bor = boards[-18]
def part_one(data):

    while len(picks) > 0:
        num = picks.pop(0)
        num.activate()
        # print(numbers)
        b = check_boards(boards)
        if b is not None:
            win_order.append(b)
            b = boards.pop(b)
            print(b, num.val, b.sum_inactive(), )
            return b.sum_inactive() * num.val, num




def part_two(num):
    board = None
    while len(boards) > 0:
        b = check_boards(boards)
        while b is not None and len(boards) > 0:
            win_order.append(b)
            board = boards.pop(b)
            b = check_boards(boards)

        if len(boards) > 0:
            num = picks.pop(0)
            # print(num, len(picks))
            num.activate()

    for row in board.board:
        print(" ".join([f'{x.get_val():2}' for x in row]))
    print()

    return board.sum_inactive() * num.val



# for i in range(len(picks)):
#     print(numbers[i-1], picks[i])
#     numbers[picks[i]-1].activate()
#     print(numbers[i - 1], picks[i])
#     print(boards[-18].is_winner())

# b = Board(
#     [
#         [82 for x in range(5)],
#         [x+1 for x in range(5, 10)],
#         [x+1 for x in range(10, 15)],
#         [x+1 for x in range(15, 20)],
#         [x+1 for x in range(20, 25)]
#     ]
# )
# while not b.is_winner():
#     print(b)
#     n = int(input("Enter next number: "))
#     numbers[n-1].activate()
#     print(b.is_winner(), "\n")

start = time.perf_counter()
target = part_one(data)
print(target[0])
print(part_two(target[1]))
print(picks)
end = time.perf_counter()
print(end-start)
