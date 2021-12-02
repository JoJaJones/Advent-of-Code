from int_code import IntCode
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
BLACK = "."
WHITE = "#"
SYMBOL_DICT = {UP: "^", LEFT: "<", RIGHT: ">", DOWN: "v"}
MOVE_DICT = {UP: (-1,0), LEFT: (0,-1), RIGHT: (0, 1), DOWN: (1, 0)}
COLOR_DICT = {0: BLACK, BLACK: 0, 1: WHITE, WHITE: 1}
D_SHIFT_DICT = {0: -1, 1: 1}

class Panel:
    def __init__(self, color=BLACK):

        self.color = color
        self.has_been_painted = False
        self.is_occupied = False

    def get_color(self, for_display=False):
        if self.is_occupied and for_display:
            return self.is_occupied
        else:
            return self.color

    def paint_panel(self, color=WHITE):
        if not self.has_been_painted:
            self.has_been_painted = True
        self.color = color

    def set_occupied(self, symbol=False):
        self.is_occupied = symbol

    def get_has_been_painted(self):
        return self.has_been_painted

class HullPainter:
    def __init__(self, int_code_program):
        self.memory = IntCode(int_code_program)
        self.rows = 5
        self.cols = 5
        self.direction = 0
        self.board = []
        self.pos = (2, 2)
        for r in range(self.rows):
            self.board.append([])
            for c in range(self.cols):
                self.board[r].append(Panel())
                if r == 2 and c == 2:
                    self.board[r][c].set_occupied(SYMBOL_DICT[DIRECTIONS[self.direction]])
                    self.board[r][c].color = WHITE

    def print_board(self):
        for row in self.board:
            print("".join([c.get_color(True) for c in row]))

    def process_step(self):
        # send panel color
        r, c = self.pos
        panel_color = self.board[r][c].get_color()
        paint_color = self.memory.run(0 if panel_color == BLACK else 1)
        if paint_color is not False:
            turn_direction = self.memory.run()
            # paint panel
            self.board[r][c].paint_panel(COLOR_DICT[paint_color])
            # move
            self.board[r][c].set_occupied()
            self.direction += 2 * turn_direction - 1
            while self.direction < 0:
                self.direction += 4
            self.direction %= 4
            dr, dc = MOVE_DICT[DIRECTIONS[self.direction]]
            r += dr
            c += dc
            self.adjust_size((r, c))
            r, c = self.pos
            self.board[r][c].set_occupied(SYMBOL_DICT[DIRECTIONS[self.direction]])
            self.print_board()
            return True

        return False

    def count_painted(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell.get_has_been_painted():
                    count += 1

        return count

    def adjust_size(self, pos):
        r, c = pos

        if r < 0:
            self.board = [[Panel() for _ in range(self.cols)]*(-r)] + self.board
            self.rows = len(self.board)
            r = 0

        if c < 0:
            for row in range(len(self.board)):
                self.board[row] = [Panel() for _ in range(-c)] + self.board[row]
            self.cols = len(self.board[0])
            c = 0

        if c >= self.cols:
            for row in range(len(self.board)):
                self.board[row] += [Panel() for _ in range(c + 1 - self.cols)]
            self.cols = len(self.board[0])

        if r >= self.rows:
            self.board += [[Panel() for _ in range(self.cols)]*(r + 1 - self.rows)]
            self.rows = len(self.board)

        self.pos = r, c


    def run_program(self):
        while self.process_step():
            pass

        print(self.count_painted())

