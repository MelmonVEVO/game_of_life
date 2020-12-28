class LifeBoard:
    def __init__(self, size: int):
        self.board = [[False for _ in range(size)] for _ in range(size)]  # False for dead, True for live
        self.size = size

    def step(self):
        new_board = [[False for _ in range(self.size)] for _ in range(self.size)]
        for j in range(self.size):
            for i in range(self.size):  # iterating through the board
                nb = self.count_neighbours(i, j)
                if not self.board[j][i] and nb == 3:  # dead cells with 3 live neighbours lives
                    new_board[j][i] = True
                elif not (self.board[j][i] and (nb == 2 or nb == 3)): # live cells without 2/3 neighbours die
                    new_board[j][i] = False
                else:
                    new_board[j][i] = self.board[j][i]
        self.board = new_board

    def switch(self, x, y):
        self.board[y][x] = not self.board[y][x]

    def count_neighbours(self, x, y):
        n = 0
        for jm in range(-1, 2):
            for im in range(-1, 2):
                if not (jm == 0 and im == 0):
                    try:
                        if self.board[y + jm][x + im]:
                            n += 1
                    except IndexError:
                        pass
        return n

    def __str__(self):
        ret = "\n\n\n"
        for b in self.board:
            for c in b:
                if c:
                    ret += "#"
                else:
                    ret += "."
            ret += "\n"
        return ret
