from random import choice
import json


class HangManGame:

    def __init__(self, name, lives, points):
        self.game_word = []
        self.guessed_letters = []
        self.displayed_word = []
        self.guessed_letters = []
        self.game_words = ["completed", "test", "beauty & the beast"]
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.game_active = True
        self.guess_state = bool
        self.lives = lives
        self.name = name
        self.points = points
        self.correct_guess_count = 0
        self.file_location = 'game_list.json'
        self.hangman_list = {}
        self.game_category = []

    def display_game_word(self):
        print(' '.join(self.displayed_word))

    def choose_category(self):
        with open(self.file_location, 'r') as f:
            self.hangman_list = json.load(f)
        print(f"Category's are: {list(self.hangman_list)}")
        while True:
            category_selection = input("which category do you want?: ")
            if category_selection in self.hangman_list:
                self.game_category = list(self.hangman_list[category_selection])
                break
            else:
                print(f"{category_selection} is not in the list")

    def game_setup(self):
        """sets up the game so a word from game word is added to the game"""
        self.game_word.clear()
        self.guessed_letters.clear()
        self.displayed_word.clear()
        self.guessed_letters.clear()
        self.game_active = True
        self.correct_guess_count = 0
        if self.lives == 0:
            self.lives = 8
        selected_word = choice(self.game_category)
        for letter in selected_word:
            self.game_word.append(letter)

        for j in selected_word:
            if j in self.alphabet:
                self.displayed_word.append("*")
            elif j == " ":
                self.displayed_word.append("_")
                self.correct_guess_count += 1
            else:
                self.displayed_word.append(j)
                self.correct_guess_count += 1
        print("Enter 'done' when finished playing, or 'change game' to select a new quiz")
        print(f"New game generated lives = {self.lives}")
        # print(' '.join(self.displayed_word))

    def check_guess(self, letter_entered):
        """checks the letter entered to see if its correct"""
        if letter_entered not in self.guessed_letters:
            self.guessed_letters.append(letter_entered)
            for i in self.game_word:
                if letter_entered == i:
                    return True
            else:
                self.lives -= 1
                if self.lives == 0:
                    self.points -= 250
                    print(f"Game lost, you lose 250 points! Total points = {self.points}")
                    self.game_active = False
                print(f"False, lives = {self.lives}")
        elif letter_entered in self.guessed_letters:
            self.guess_state = False
            print("This is already entered")
            return False

    def add_guess(self, correct_letter, count_1=0):
        """adds the guess to the displayed word"""
        for i in self.game_word:
            if correct_letter == i:
                self.displayed_word.pop(count_1)
                self.displayed_word.insert(count_1, correct_letter)
                self.correct_guess_count += 1
                self.points += 50
                print(f"You earned 50 points. Total = {self.points}")
            count_1 += 1
        if self.correct_guess_count == len(self.game_word):
            self.points += 150
            print(f"Congratulations {self.name} you completed this challenge + 150 points +3 lives! "
                  f"\ntotal points = {self.points}"
                  f"\nlives = {self.lives}")
            self.game_active = False

    def edit_game(self):
        with open(self.file_location, 'r') as f:
            self.hangman_list = json.load(f)
        print("welcome to game editor, enter 'done' to exit out menu")

        while True:
            print(list(self.hangman_list.Unencrypted()))
            category = input("add to existing game, or make new one by entering new name or existing one: ")
            if category in self.hangman_list:
                print("list already exists")
                while True:
                    message = input("what do you want to add?: ")
                    if message == "done":
                        with open(self.file_location, 'w') as f:
                            json.dump(self.hangman_list, f)
                            break
                    else:
                        self.hangman_list[category].append(message)
            elif category == "done":
                break
            else:
                while True:
                    message = input("category doesnt exist, do you want to add it (y/n)?: ")
                    if message == "y":
                        self.hangman_list[category] = []
                        with open(self.file_location, 'w') as f:
                            json.dump(self.hangman_list, f)
                            break
                    elif message == "n":
                        break
                    else:
                        print(f"{message} is invalid")


class UsersProfiles:
    def __init__(self):
        self.username = ""
        self.users = {}
        self.filename = 'Users.json'
        self.name = str
        self.lives = int
        self.points = int
        self.make_profile = bool

    def get_user_info(self):
        """opens the file with username information"""
        with open(self.filename, 'r') as f:
            self.users = json.load(f)
        while True:
            message = input("Do you have an account Y/N? ")
            if message.lower() == "y":
                self.username = input("what is your username?: ")
                if self.username in self.users:
                    self.name = self.users[self.username]['name']
                    self.lives = self.users[self.username]['lives']
                    self.points = self.users[self.username]['points']
                    self.make_profile = False
                    break
                else:
                    print("Profile doesnt exist")
            elif message.lower() == "n":
                print("making a profile now")
                self.make_profile = True
                break
            else:
                print(f"{message} is an invalid input")

    def create_profile(self):
        """creates a user profile"""
        new_username = input("what username do you want?: ")
        new_name = input("what is your name?: ")
        self.users[new_username] = {"name": new_name, "lives": 8, "points": 0}
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)
        self.make_profile = False

    def show_user_info(self):
        """Prints message about the users information"""
        print(f"Hello {self.name.title()}, welcome back to Hangman by Joe Leadbeater")

    def update_profile(self, lives, points):
        """updates the profile and saves it"""
        self.users[self.username]["lives"] = lives
        self.users[self.username]["points"] = points
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)


account = UsersProfiles()


def setup_user():
    while True:
        account.get_user_info()
        if account.make_profile:
            account.create_profile()
        else:
            account.show_user_info()
            break


def start_game():
    setup_user()
    game = HangManGame(account.name, account.lives, account.points)
    while True:
        message = input("Do you want to edit game categories, or use existing one?(existing/edit game): ")
        if message == "existing":
            game.choose_category()
            break
        elif message == "edit game":
            game.edit_game()
        else:
            print(f"{message} is an invalid input")

    while message != "done":
        game.game_setup()
        while game.game_active:
            game.display_game_word()
            message = input("What letter do you choose?: ")
            if message == "done":
                break
            elif message == "change game":
                game.choose_category()
                game.game_setup()
            elif len(message) == 1:
                add_letter = game.check_guess(message)
                account.update_profile(game.lives, game.points)
                if add_letter:
                    game.add_guess(message)
            else:
                print(f"{message} is too many characters, just use one!")


while True:
    start_game()
