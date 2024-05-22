import random


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(0, False) for i in range(self.N)] for j in range(self.N)]
        self.init()

    def init(self):
        for m in range(self.M):
            while True:
                x = random.randint(0, self.N - 1)
                y = random.randint(0, self.N - 1)
                if not self.pole[x][y].mine:
                    self.pole[x][y].mine = True
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if not (i == x and j == y) and -1 < i < self.N and -1 < j < self.N:
                                self.pole[i][j].around_mines += 1
                    break

    def show(self):
        view = [[0 for i in range(self.N)] for j in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].fl_open:
                    view[i][j] = '#'
                elif self.pole[i][j].mine:
                    view[i][j] = '*'
                else:
                    view[i][j] = self.pole[i][j].around_mines
            print(*view[i])


pole_game = GamePole(10, 12)
