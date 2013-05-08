from random import *

global ship_length = 3                      # makes the ship 3 coordinates in length

def board_difficulty():                     # function where user inputs how large the board will be
    global size                             # Global variable declared for the size of the board
    size = int(raw_input("How Big?"))       # user input decides the value of size
    return size

def make_board():                           # function that takes value size to create a list filled with "O" 
    global board                            # Global variable declared 
    board = []                              # variable set to list
    for x in range(size):                   # For loop that fills the entire list with O's 
        board.append(["O"]*size)
    return

def print_board(board):                     # function that prints the board 
    for row in board:                       # I'm going to be honest, I don't really know exactly how this works
        print " ".join(row)                 # but it seems to do the trick

def get_vals():                             # function that prompts the player for a column and row value
    global guess_row                        # global variable for the user inputed row   
    guess_row = input("Guess Row: ") - 1    # defines the variable as user input -1 because lists start at 0
    global guess_col                        # global variable for the user inputed column
    guess_col = input("Guess Col: ") - 1    # defines the variable as user input -1 because lists start at 0

def set_row_and_col():                      # function that sets the row and column for the ship in the list          
    global vert_or_hort   #variable to determine ship orientation
    global ship_row         # Global variable for the ship row
    global ship_start
    vert_or_hort = randint(0,1)
    ship_row = []
    global ship_col         # Global variable for the ship column
    ship_col = []
    ship_start = randint(0,len(board))     # defines the variable as a random interger
    if vert_or_hort == 0:                       #if horizontal
        for x in range(ship_length):
            ship_row.append(ship_start + x)     #create list of horizontal ship locations
        ship_col = ship_start                   #set single vertical coordinates
    else:                                       #if not horizontal
        ship_row = ship_start                   #set as one coordinate
        for x in range(ship_length):            #set vertical coordinates
            ship_col.append(ship_start + x)
    print ship_col, ship_row                #PRINTS SHIP COORDINATES FOR TROUBLESHOOTING
    return ship_col, ship_row               # returns 2 random numbers 

def get_difficulty():                       # function that gets user input to determine how many guesses they will get
    print "How many guesses?"               #
    global difficulty                       # Global variable for the amount of guesses
    difficulty = input()                    # defines variable as user input
    return difficulty                       # returns the variable "difficulty"


def check():                                                        # function that will check the user inputed guesses against the random number generated for the ship
        if guess_row == ship_row and guess_col == ship_col:         # determines if ship is struck
                print "Congratulations! You sank my battleship!"
                return 1                                            # returns true
        else:
                if (guess_row < 0 or guess_row > int(len(board)) -1 or (guess_col < 0 or guess_col > int(len(board[0])) -1)):
                                                                    # checks to see if the user inputed guess is within the parameters of the baard
                  print "Oops, that's not even in the ocean."
                elif (board[guess_row][guess_col] == "X"):          # checks to see if the guess has already been inputted
                   print "You guessed that one already."
                else:
                   board[guess_row][guess_col] = "X"                # replaces the "O" with an "X" for a miss
                   print "You missed my battleship!"
        return 0                                                    # returns false


def play():                                                         # that creates and plays the board for the number of guesses inputted
    for turn in range(difficulty):                                  
        print "This is turn # " + str(turn + 1)
        print_board(board)
        get_vals()
        if check():
            break
    
        elif turn == difficulty:
            print "Game Over"

def playbattleship():
    print "welcome to battleship!"
    print "would you like to play? Y/N?"
    yesno = raw_input()

    if yesno.lower() == "y":
        get_difficulty()
        board_difficulty()
        make_board()
        set_row_and_col()
        play()
    else:
        print "goodbye"
