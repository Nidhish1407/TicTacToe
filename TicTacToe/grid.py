class TTT:
    grid = [['...', '|', '...', '|', '...'],
            ['...', '|', '...', '|', '...'],
            ['...', '|', '...', '|', '...']]

    def init(self):
        pass

    def showGrid(self):
        print(
            f'{self.grid[0][0]}{self.grid[0][1]}{self.grid[0][2]}{self.grid[0][3]}{self.grid[0][4]}')
        print(
            f'{self.grid[1][0]}{self.grid[1][1]}{self.grid[1][2]}{self.grid[1][3]}{self.grid[1][4]}')
        print(
            f'{self.grid[2][0]}{self.grid[2][1]}{self.grid[2][2]}{self.grid[2][3]}{self.grid[2][4]}')
        print()

    def update(self, pos, val):
        if pos == 1:
            self.grid[0][0] = val
        elif pos == 2:
            self.grid[0][2] = val
        elif pos == 3:
            self.grid[0][4] = val
        elif pos == 4:
            self.grid[1][0] = val
        elif pos == 5:
            self.grid[1][2] = val
        elif pos == 6:
            self.grid[1][4] = val
        elif pos == 7:
            self.grid[2][0] = val
        elif pos == 8:
            self.grid[2][2] = val
        elif pos == 9:
            self.grid[2][4] = val
        else:
            print(f"{pos} position is invalid.")

    def isspacefree(self, pos):
        if pos == 1:
            return self.grid[0][0] == '...'
        elif pos == 2:
            return self.grid[0][2] == '...'
        elif pos == 3:
            return self.grid[0][4] == '...'
        elif pos == 4:
            return self.grid[1][0] == '...'
        elif pos == 5:
            return self.grid[1][2] == '...'
        elif pos == 6:
            return self.grid[1][4] == '...'
        elif pos == 7:
            return self.grid[2][0] == '...'
        elif pos == 8:
            return self.grid[2][2] == '...'
        elif pos == 9:
            return self.grid[2][4] == '...'
        else:
            print(f"{pos} position is invalid.")

    def refresh(self):
        for i in range(1, 10):
            self.update(i, '...')
        self.showGrid()

    def iswinner(self, S):
        # check horizontally
        for row1 in self.grid:
            if row1[0] == S:
                row = [i for i in row1 if i != '|']
                if len(set(row)) == 1:
                    print("row")
                    return True
        # check vertically
        grid1 = [[row[i] for row in self.grid]
                 for i in range(len(self.grid[0]))]
        for col1 in grid1:
            if col1[0] == S:
                col = [i for i in col1 if i != '|']
                if len(set(col)) == 1:
                    print("col")
                    return True

       # check diagonally
        grid1 = [[i for i in row if i != '|'] for row in self.grid]
        return ((grid1[0][0] == grid1[1][2] == grid1[2][2] == S) or
                (grid1[0][2] == grid1[1][2] == grid1[2][0] == S))
        # n = len(grid1)
        # for i in range(0, n):
        #     if grid1[i][i] == grid1[0][0] and grid1[0][0] != '...':
        #         if i == 2:
        #             print("main diagonal")
        #             return True

        # for i in range(0, n):
        #     if grid1[i][(n-1)-i] == grid1[0][2] and grid1[0][2] != '...':
        #         if i == 2:
        #             print("Other Diagonal")
        #             return True

        return False

    def iswinner1(self, S, grid):
        return((grid[0] == grid[1] == grid[2] == S) or
               (grid[3] == grid[4] == grid[5] == S) or
               (grid[6] == grid[7] == grid[8] == S) or

               (grid[0] == grid[3] == grid[6] == S) or
               (grid[1] == grid[4] == grid[7] == S) or
               (grid[2] == grid[5] == grid[8] == S) or

               (grid[0] == grid[4] == grid[8] == S) or
               (grid[2] == grid[4] == grid[6] == S))

    def isboardfull(self):
        for row in self.grid:
            if row.count('...') > 0:
                return False
        return True

    def playermove(self):
        run = True
        while run:
            move = input("Enter position to place 'X' at|(1-9):")
            try:
                move = int(move)
                if 0 < move < 10:
                    if self.isspacefree(move):
                        self.update(move, '.X.')
                        run = False
                    else:
                        print(f"Sorry,this {move} is occupied.")
                else:
                    print("Please enter integer in range (1-9).")
            except:
                print("Please enter integer value.")

    def cpumove(self):
        grid1 = [i for row in self.grid for i in row if i != '|']
        print(grid1)
        possiblemoves = [i for i, val in enumerate(grid1) if val == '...']
        print(possiblemoves)
        move = -1

        for let in ['.X.', '.O.']:
            for i in possiblemoves:
                grid1[i] = let
                if self.iswinner1(let, grid1):
                    print(f"winner {i}")
                    move = i+1
                    return move

        cornersOpen = []
        for i in possiblemoves:
            if i in [0, 2, 6, 8]:
                cornersOpen.append(i)
        if len(cornersOpen) > 1:
            move = self.selectrandom(cornersOpen)
            # print("corner")
            return move+1

        if 4 in possiblemoves:
            move = 5
            return move

        edgesOpen = []
        for i in possiblemoves:
            if i in [1, 3, 5, 7]:
                edgesOpen.append(i)
        if len(edgesOpen) > 1:
            move = self.selectrandom(edgesOpen)
            # print("edge")
            move += 1

        return move

    def selectrandom(self, li):
        import random as rd
        n = len(li)
        return li[rd.randrange(0, n)]


def start():
    X = '.X.'
    O = '.O.'
    S = '...'
    t = TTT()
    print("Welcome to TicTacToe")
    while not t.isboardfull():
        if not t.iswinner(O):
            t.playermove()
            t.showGrid()
        else:
            print("O won this time.")
            break

        if not t.iswinner(X):
            move = t.cpumove()
            if move == -1:
                print("Tie Game!")
                t.showGrid()
                break
            else:
                t.update(move, O)
                print(f"Computer placed 'O' at position {move}.")
                t.showGrid()
        else:
            print("X won this time.")
            break

    if t.isboardfull():
        print("out")
        print("Tie Game!!")


start()
