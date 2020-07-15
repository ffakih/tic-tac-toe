import random
import copy


class tictactoe:
    #init
    def __init__(self):
        self.curr = 1
        # Board Indexing
        # 0 1 2
        # 3 4 5
        # 6 7 8
        self.Board = [0,0,0,0,0,0,0,0,0]
        self.Robot = 1
    
    # Programs AI-who starts?
    def programRobot(self,myTurn):
        if myTurn == True:
            return self.Robot
        else:
            self.Robot = 2
            return self.Robot
    
    def getRobot(self):
        return self.Robot

    def GameBoard(self):
        return self.Board
    
    
    # Check if game is going on
    def Ongoing(self):
        inGame = False
        if self.result() == -1:
            inGame = True
        return inGame

    # Copy of game state
    def CurrentState(self):
        Game1 = tictactoe()
        Game1.curr = self.curr
        Game1.Robot = self.Robot
        Game1.Board = self.Board[:]
        return Game1
    
    # Changing turns between user and AI    
    def changeTurn(self):
        if (self.curr == 2):
            self.curr = 1
        else:
            self.curr = 2
        return self.curr
    
    # Make a move
    def makeaMove(self,x,player):
        self.Board[x] = player
        return x
    
    # Check if there are zero tiles
    def zeroTile(self,board):
        chk = True
        for i in board:
            if self.Board[i] == 0:
                chk = False
        return chk
    
    
    
    def result(self):
        # Result of game
        # Win state is :
        # 0 1 2, 0 3 6, 0 4 8, 1 4 7, 2 5 8, 2 4 6, 3 4 5, 6 7 8

        if all( [self.Board[0] == self.Board[1],self.Board[0] == self.Board[2],self.zeroTile( [ 0,1,2])]):
            if (self.Board[0] == 1):
                checker = 1
            else:
                checker = 2

        elif all( [self.Board[0] == self.Board[3],self.Board[0] == self.Board[6],self.zeroTile( [ 0,3,6]) ]):
            if (self.Board[0] == 1):
                checker = 1
            else:
                checker = 2 

        elif all( [self.Board[0]==self.Board[4],self.Board[0] == self.Board[8] , self.zeroTile( [ 0,4,8])]):
            if (self.Board[0] == 1):
                checker = 1
            else:
                checker = 2

        elif all( [self.Board[1]==self.Board[4],self.Board[1] == self.Board[7] ,self.zeroTile( [ 1,4,7])]):
            if (self.Board[1] == 1):
                checker = 1
            else:
                checker = 2

        elif all( [self.Board[2]==self.Board[5],self.Board[2] == self.Board[8] , self.zeroTile( [ 2,5,8])]):
            if (self.Board[2] == 1):
                checker = 1
            else:
                checker = 2
        
        elif all( [self.Board[2]==self.Board[4],self.Board[2] == self.Board[6], self.zeroTile( [ 2,4,6]) ]):
            if (self.Board[2] == 1):
                checker = 1
            else:
                checker = 2
        
        elif all( [self.Board[3]==self.Board[4],self.Board[3] == self.Board[5] , self.zeroTile( [ 3,4,5])]):
            if (self.Board[3] == 1):
                checker = 1
            else:
                checker = 2
        
        elif all( [self.Board[6]==self.Board[7],self.Board[6] == self.Board[8] , self.zeroTile( [ 6,7,8])]):
            if (self.Board[6] == 1):
                checker = 1
            else:
                checker = 2

        elif 0 not in self.Board:
            checker = 0
        
        else:
            checker = -1
        
        return checker
    
    def drawBoard(self):
        board = ['| ', '| ', '| ', '| ', '| ', '| ', '| ', '| ', '| ']
        stringDisplay = ''
        i = 0
        while (i < 9):
            # Player 1 using X and Player 2 using O
            if self.Board[i] == 1:
                board[i] = 'X '
            if self.Board[i] == 2:
                board[i] = 'O '
            if (i == 2 or i == 5):
                stringDisplay = stringDisplay + (board[i] + '\n')
            else:
                stringDisplay = stringDisplay + board[i]
            i = i + 1
        print("\nBoard Format, enter the desired number of your X or O placement.\nFor example: enter 0 to put your X/O in the top left corner\n\n\n" + '0 1 2 \n3 4 5\n6 7 8\n\n')
        print("Your Current Game:\n" + stringDisplay)

    def EndGame(self):
        # Display End game board
        board = ['| ', '| ', '| ', '| ', '| ', '| ', '| ', '| ', '| ']
        stringDisplay = ''
        i = 0
        while (i < 9):
            # Player 1 using X and Player 2 using O
            if self.Board[i] == 1:
                board[i] = ' X '
            if self.Board[i] == 2:
                board[i] = ' O '
            if (i == 2 or i == 5):
                stringDisplay = stringDisplay + (board[i] + '\n')
            else:
                stringDisplay = stringDisplay + board[i]
            i = i + 1
        print("Your Current Game:\n" + stringDisplay)
        print("\nGame Over!\n")
        if self.result() == 0:
            print("Result: Draw\n")
        elif self.result() == 1:
            print("Result: YOU WON!\n")
        elif self.result() == 2:
            print("Result: AI WON!\n")
    # Store the number of legal moves
    def DBLegalMoves(self):
        idx = []
        for i in range(9):
            if self.Board[i] == 0:
                idx.append(i)
        return idx
    
    # MONTE CARLO TREE SEARCH ALGORITHM
class MonteCarloTreeSearch:
    def __init__(self,game,rand1):
        self.game = game
        self.board = self.game.GameBoard()
        self.state = self.game.Ongoing()
        self.rand1 = rand1

    def MonteCarloMove(self):
        legalMoves_1 = self.game.DBLegalMoves()
        numWins = {}

        for i in legalMoves_1:
            numWins[i] = 0
        for j in legalMoves_1:
            for i in range(self.rand1):
                # Set number of random playouts and store the result when playout is over
                numWins[j] += self.randPlay(j)
        choice = legalMoves_1[0]
        choiceWin = numWins[choice]
        for w in numWins:
            if numWins[w] >= choiceWin:
                choice = w
                choiceWin = numWins[w]
        self.game.makeaMove(int(choice),self.game.curr)
        
        
            
    
    # Computer makes a list of all legals moves, Then for each of these moves it does some number of random playouts. 
    # It records the result (a win, loss, or draw), and then does some more random playouts. 
    # It does random playouts for every possible move, and when they’re done it choses the 
    # move that resulted in the greatest number of wins.

    def randPlay(self,move):
        copyGame = copy.deepcopy(self.game)
        # Make move
        copyGame.makeaMove(move,copyGame.curr)
        # Switch Player
        copyGame.changeTurn()
        while (copyGame.Ongoing() == True):
            legalMoves = copyGame.DBLegalMoves()
            randomMove = random.randint(0,8)
            while (randomMove not in legalMoves):
                randomMove = random.randint(0,8)
            copyGame.makeaMove(randomMove , copyGame.curr)
            copyGame.changeTurn()
            copyGame.state = copyGame.Ongoing()

        if copyGame.getRobot() == 1:
            if copyGame.getRobot() == 2:
                return -5
            elif copyGame.result() == 1:
                return 2
            else:
                return 1
        else:
            if copyGame.result() == 2:
                return 2
            elif copyGame.result() == 1:
                return -5
            else:
                return 1
    
def play_a_new_game():
    game = tictactoe()
    robotMonteCarlo = MonteCarloTreeSearch(game,1000)
    gameState = game.Ongoing()
    myMove = ''
    first = input('Do you want to go first? (type Y or N): ')
    if first.upper() == 'N':
        robotMonteCarlo.MonteCarloMove()
        game.changeTurn()
        game.drawBoard()
        myMove = input('Choose your next move: ')
    else:
        game.programRobot(False)
        game.drawBoard()
        myMove = input('Choose your next move: ')
    while gameState == True:
        myMove = game.makeaMove(int(myMove) , game.curr)
        game.drawBoard()
        game.changeTurn()
        robotMonteCarlo.MonteCarloMove()
        gameState = game.Ongoing()
        if gameState ==  True:
            game.changeTurn()
            game.drawBoard()
            myMove = input('Choose your next move: ')
            gameChk = game.CurrentState()
            myMove = gameChk.makeaMove(int(myMove),gameChk.curr)
            gameState = gameChk.Ongoing()

    game.makeaMove(int(myMove),gameChk.curr)
    print('\n')
    game.EndGame()


if __name__ == '__main__':
    play_a_new_game()





    