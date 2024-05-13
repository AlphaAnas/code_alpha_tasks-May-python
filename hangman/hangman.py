import random
import pygame, os
import re
'''
    music of success and lost
    take random words
    display the words that can be used
    make a hangman structure
    5 levels
    score
    display

'''
class Hangman():
    def __init__(self):


        # **Initialize the pygame variables**
        pygame.init()
        pygame.mixer.init()


       ## Initialize the in-game variables
        self.level = "easy"
        self.word_memory = []
        self.words = self.get_words()
        self.max_attempts =  5
        self.attempts_left = self.max_attempts
        self.word = ""
        self.word_lst = []
        self.category = ""
        self.guessed_chars = []
        self.status = "lost"
        self.lives = 5
        self.reveal_word = []
        self.score = 0
        

    def initialize(self):
        self.level = "hard"
        self.word_memory = []
        self.words = self.get_words()
        self.max_attempts = 5
        self.attempts_left = self.max_attempts
        self.word = ""
        self.word_lst = []
        self.category = ""
        self.guessed_chars = []
        self.status = "lost"
        self.lives = 5
        self.score = 0
        self.reveal_word = []





    def get_words(self)->list:
        lst = []
     
        file = open(f"levels\{self.level}.tsv",'r')
        for line in file:
            lst1 = re.split(r'\s{2,}', line.strip())
            word, category = lst1[1], lst1[0]
            lst.append([category.lower(), word.lower()])
            self.word_memory.append(word)
        return lst
    
    def print_words(self):
        for word in self.word_memory:
            print(word, end=" ")
        print()

    def get_shape(self, index):

            stages = [
                """
                _________
                |         |
                |
                |
                |
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |
                |
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |         |
                |
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |        /|
                |
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |        /|\\
                |
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |        /|\\
                |        /
                |
                |
                |_________
                """,
                """
                _________
                |         |
                |         O
                |        /|\\
                |        / \\  
                |
                |
                |_________
                """
                #\\ is the newline character
            ]

            # Ensure the index is within the range of stages list
         

            return stages[index]
    
    import random

    def set_reveal(self):
        # Create a list of indices to reveal
        reveal_count = 2 if self.level == "easy" else 3
        indices_to_reveal = random.sample(range(len(self.word)), min(reveal_count, len(self.word)))

        # Replace characters at revealed indices with '#'
        self.reveal_word = [ch if i not in indices_to_reveal else '_' for i, ch in enumerate(self.word)]
         
    def update_guess_word(self):
        
        if (len(self.guessed_chars) > 0):

            for ch in self.guessed_chars:

                if ch in self.word:
                    ind = list(self.word).index(ch)
                    if self.reveal_word[ind] == "_":
                        self.reveal_word[ind] = list(self.word)[ind]
                    else:
                        continue
        for i in self.reveal_word:
            print(i, end=" ")
               
            
    def play_sound(self,audio,delay=0):
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
        pygame.time.wait(delay)

# the main function to start the game
    def start_game(self):
            self.play_sound("music\hangman.wav", 1000)


           
            self.word_lst = []
            os.system("cls")

            while True:
                    # choose a random word from the list
                    index = random.randint(0, len(self.words)-1)
                    self.category, self.word = self.words[index]
                    self.lives -= 1
                    self.word_lst = list(self.word)
                    self.guessed_chars = []
                    self.attempts_left = self.max_attempts

                   
                
                    self.set_reveal() # make some characters of thw word reveal
                    #like _a_o_e = lahore
                    while self.attempts_left > 0:
                        

                    
                        print(f"\n {self.category}\t\tScore:{self.score}\t\tLives:{self.lives}\t\tLevel:{self.level}\n") #Displaying score and lives
                        print("Attempts left : ", self.attempts_left)


                        # self.print_dashes()
                        # print the updated word
                        self.update_guess_word()

                        # Get user input
                        guess = input("Enter a character: ").lower()
                        self.play_sound("music\hit.mp3", 0)
                        

                        # Check input validity
                        if len(guess) != 1 or not guess.isalpha():
                            print("Please enter a single letter.")
                            continue

                        # Add the guessed letter to the list
                        self.guessed_chars.append(guess)

                        # Check if the guess is correct
                        if guess in self.word_lst:
                            print("Correct guess!")
                            self.play_sound("music\correct.wav",0)
               
                            index = self.max_attempts - self.attempts_left
                            print(self.get_shape(index))
                            ind =  self.word_lst.index(guess)
                            self.word_lst = [ch if ch != guess else '#' for ch in self.word_lst]
                            #we donot want the words which are already in reveal_word
                            for i,ch in enumerate(self.reveal_word):
                                 if ch != "_":
                                        self.word_lst[i] = "#"

                            pygame.time.wait(1000)
                           
                        
                        else:
                            # Decrement the attempts left on every wrong guess
                            self.attempts_left -= 1 
                            print(self.get_shape(self.max_attempts - self.attempts_left))
                            print("Wrong guess")
                            self.play_sound("music\wrong.wav",0)
                            pygame.time.wait(1000)
                            continue

                        
                        ## winning condition
                        if  self.word_lst.count('#') == len(self.word):
                            self.status = "win"
                            self.score += 20
                            self.word = ""
                            self.word_lst = []
                            self.guessed_chars = []
                            print("Congratulations! You have guessed the word correctly!")
                            print(f"Score = {self.score}")
                            print(f"Lives = {self.lives}")
                            #give a delay of 2 seconds
                            pygame.mixer.init()
                            pygame.time.wait(2000)
                            os.system("cls")
                            break

                        

           
          

                    if self.lives == 0:
                        self.end_game() # the game will show the correct words and exit

                        option = input("Do you want to try again? (y/n) ")
                        if option == "n":
                        #The game will announce the result and exit
                            os.system("cls")
                            break
                        else:
                            #The game will continue
                            os.system("cls")
                
                            self.score = 0
                            self.lives = 3
                    else:
                   
                        #The game will continue
                        os.system("cls")
    
                        if self.score >= 60:
                             print("Congratulations! You have reached the next level!")
                             self.play_sound("music\win.mp3",0)
                           

                             print(f"Lives = {self.lives}, Score = {self.score}, Level = {self.level}, Status = {self.status}")
                             print("The next level is hard")

                             self.initialize()
                             continue

                           
                 

    def end_game(self):
            print("Game Over!")
            print(f"The words were {self.print_words()}")
            self.play_sound("music\gameover.wav",0)
            print(f"You {self.status}!")
            pygame.time.wait(2000)

hangman = Hangman()
print("Welcome to hangman game !")
n = input("press any key to start: ")
if n :
    hangman.start_game()

