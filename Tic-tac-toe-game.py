import random
import colorama


check = []
play_again = None
winner = None
game_over = False
game_over_2 = False
test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
class Board:


    def display_board(self ,board):

        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def check_board(self):
       check.clear()
       for i in range  (1,10):
           # VERIFICAM DACA TABLA E GOALA / PLINA

           if test_board[i] == " ":
              check.append(False)

           else:
               check.append(True)
       return check

    def new_board(self):
        global test_board
        test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        return test_board






class Player:
    def __init__(self):
        self.ask = ""
        self.name1 = " "
        self.choose = " "
        self.name2 = " "
        self.index = 0
        self.my_plys= {1: "Player 1", 2:"Player 2"}

    def rand_choose(self):
            self.choose = self.my_plys[random.choice(list(self.my_plys))]
            return  colorama.Fore.GREEN  + f" {self.my_plys[random.choice(list(self.my_plys))]} " + colorama.Style.RESET_ALL + "will be the first"



    def asK_your_name1(self):
        self.name1 = input("What is your name?\nYour name is: ")
        return self.name1.upper()[0] + self.name1.lower()[1:]



    def asK_your_name2(self):
        self.name2 = input("What is your name?\nYour name is: ")

        return self.name2.upper()[0] + self.name2.lower()[1:]


    def ask_X_or_O(self):
         self.ask =input("What you want to be?" + colorama.Fore.RED + " X " + colorama.Style.RESET_ALL  + "or " + colorama.Fore.BLUE + "O" + colorama.Style.RESET_ALL + "?\n")

         return self.ask






    def choose_index(self):
        global test_board
        self.index = int(input("Please choose a position: "))
        while test_board[self.index] != " ":
            print(colorama.Fore.RED +"Invalid index!")
            self.index = int(input("Please choose a position: "+colorama.Style.RESET_ALL))
        return self.index

class Game:
    def check_for_win(self):

        global winner
        if test_board[7] == test_board[8] == test_board[9] and test_board[7] != " ":
            winner= test_board[7]
            print(f"The winner is {winner}")
        elif test_board[4] == test_board[5] == test_board[6] and test_board[4] != " ":
            winner = test_board[4]
            print(f"The winner is {winner}")
        elif test_board[1] == test_board[2] == test_board[3] and test_board[1] != " ":
            winner = test_board[1]
            print(f"The winner is {winner}")
        elif test_board[7] == test_board[5] == test_board[3] and test_board[7] != " ":
            winner = test_board[7]
            print(f"The winner is {winner}")
        elif test_board[9] == test_board[5] == test_board[1] and test_board[9] != " ":
            winner = test_board[9]
            print(f"The winner is {winner}")
        elif test_board[7] == test_board[4] == test_board[1] and test_board[4] != " ":
            winner = test_board[4]
            print(f"The winner is {winner}")
        elif test_board[8] == test_board[5] == test_board[2] and test_board[8] != " ":
            winner = test_board[8]
            print(f"The winner is {winner}")
        elif test_board[9] == test_board[6] == test_board[3] and test_board[9] != " ":
            winner = test_board[9]
            print(f"The winner is {winner}")

    def game_loop(self):
        play_again = input("Do you wanna play again?").upper().startswith("Y")
        return play_again



###### GAME LOGIC
used_board = []
markerply1 = ""
markerply2 = ""
first_player = " "
second_player = ""
index = None


print("Welcome to TIAC TAC TOE")
while not game_over:
        Board().new_board()
        question = input("Do you wanna play? Yes or No?: ")
        if question.upper() == "YES":
            player1 = Player().asK_your_name1()
            print(f"{player1} you are player 1\n")
            player2 = Player().asK_your_name2()
            print(f"{player2} you are player 2")



            rando = Player()
            rando.rand_choose()

            if rando.choose.upper() == "PLAYER 1":
                first_player = "PLAYER 1"
                second_player = "PLAYER 2"
                print(colorama.Fore.YELLOW + "\nPlayer 1" + colorama.Style.RESET_ALL + " wil start first")
                rando.ask_X_or_O()

                if rando.ask.upper() == "X":
                    print(f"PLayer 1 is {rando.ask.upper()} and player 2 is O")
                    markerply1 = "X"
                    markerply2 = "O"
                elif rando.ask.upper() == "O":
                    print(f"PLayer 1 is {rando.ask.upper()} and player 2 is X")
                    markerply1 = "O"
                    markerply2 = "X"



            elif rando.choose.upper() == "PLAYER 2":
                first_player = "PLAYER 2"
                second_player = "PLAYER 1"
                print(colorama.Fore.GREEN + "\nPlayer 2" + colorama.Style.RESET_ALL + " will start first")

                rando.ask_X_or_O()
                if rando.ask.upper() == "X":
                    print(f"PLayer 2 is {rando.ask.upper()} and player 1 is O")
                    markerply1 = "O"
                    markerply2 = "X"
                elif rando.ask.upper() == "O":
                    print(f"PLayer 2 is {rando.ask.upper()} and player 1 is X")
                    markerply1 = "X"
                    markerply2 = "O"




            print(colorama.Fore.LIGHTBLUE_EX +f"\n{first_player} "+colorama.Style.RESET_ALL + "will start first\n")

            board_instance = Board()
            mygame = Game()

            while not game_over_2:



                       if first_player == "PLAYER 1":
                           if winner is None:
                               if False in board_instance.check_board():
                                        print(f"{markerply1} is your turn!")
                                        index = rando.choose_index()
                                        test_board[index] = markerply1
                                        board_instance.display_board(test_board)
                                        mygame.check_for_win()

                                        if  winner is None:
                                            if False in  board_instance.check_board():



                                                print(f"{markerply2} is your turn!")
                                                index = rando.choose_index()
                                                test_board[index] = markerply2
                                                board_instance.display_board(test_board)

                                            else:
                                                print("There are no more empty boxes")
                                                if not (mygame.game_loop()):
                                                    game_over_2 = True
                                                    game_over = True
                                                else:
                                                    winner = None
                                                    Board().new_board()








                                        else:
                                            print(colorama.Fore.RED + "Game over!\n" + colorama.Style.RESET_ALL)
                                            if not (mygame.game_loop()):
                                                game_over_2 = True
                                                game_over = True
                                            else:
                                                winner = None
                                                Board().new_board()







                               else:
                                    print("There are no more empty boxes")

                                    if not (mygame.game_loop()):
                                        game_over_2 = True
                                        game_over = True
                                    else:
                                        winner = None
                                        Board().new_board()







                           else:
                                    print(colorama.Fore.RED +"Game over!\n"+colorama.Style.RESET_ALL)

                                    if not (mygame.game_loop()):
                                        game_over_2 = True
                                        game_over = True
                                    else:
                                        winner=None
                                        Board().new_board()






                       elif first_player == "PLAYER 2":
                                if  winner is None :
                                    if False in board_instance.check_board():

                                            print(f"{markerply2} is your turn!")
                                            index = rando.choose_index()
                                            test_board[index] = markerply2
                                            board_instance.display_board(test_board)
                                            mygame.check_for_win()

                                            if  winner is None :
                                                if False in board_instance.check_board():

                                                    print(f"{markerply1} is your turn!")
                                                    index = rando.choose_index()
                                                    test_board[index] = markerply1
                                                    board_instance.display_board(test_board)
                                                    mygame.check_for_win()
                                                    board_instance.check_board()
                                                else:
                                                    print("There are no more empty boxes")

                                                    if not (mygame.game_loop()):
                                                        game_over_2 = True
                                                        game_over = True
                                                    else:
                                                        winner = None
                                                        Board().new_board()









                                            else:
                                                print(colorama.Fore.RED +"Game over!\n" +colorama.Style.RESET_ALL )

                                                if not (mygame.game_loop()):
                                                    game_over_2 = True
                                                    game_over = True
                                                else:
                                                    winner = None
                                                    Board().new_board()







                                else:
                                        print("There are no more empty boxes")

                                        if not (mygame.game_loop()):
                                            game_over_2 = True
                                            game_over = True
                                        else:
                                            winner = None
                                            Board().new_board()



                       else:
                                    print(colorama.Fore.RED + "Game over!\n" + colorama.Style.RESET_ALL)

                                    if not (mygame.game_loop()):
                                        game_over_2 = True
                                        game_over = True
                                    else:
                                        winner = None
                                        Board().new_board()





































