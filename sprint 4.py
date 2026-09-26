import random


# Constants used throughout the program

XP_PER_CORRECT = 50
XP_PER_LEVEL = 100
MIN_COUNT = 1
FIRST_WORD_REQUIRED = 1
QUESTIONS_ACHIEVEMENT = 5
STREAK_ACHIEVEMENT = 5
FLASHCARD_WIDTH = 32
ARROW_WIDTH = 40
SEPARATOR_LENGTH = 50
PERCENT = 100
ALPHABET_LETTERS = 26
CLEAR_SCREEN = 50
CAESAR_KEY = 3


def caesar_encrypt(password):
    """Encrypt a password using a caesar cipher, returns encrypted password."""

    # Defining string to be edited later
    encrypted = ""

    # Looping through every character in the password
    for character in password:

        # In the case of letters
        if character.isalpha():

            # If uppercase
            if character.isupper():

                # Encrypting using unicodes
                encrypted += chr(
                    (ord(character) - ord("A") + CAESAR_KEY)
                    % ALPHABET_LETTERS
                    + ord("A")
                )

            # If lowercase
            else:

                # Encrypting using unicodes
                encrypted += chr(
                    (ord(character) - ord("a") + CAESAR_KEY)
                    % ALPHABET_LETTERS
                    + ord("a")
                )

        # In the case of digits
        elif character.isdigit():
            encrypted += str((int(character) + CAESAR_KEY) % 10)

        # In the case of special characters
        else:
            encrypted += character

    return encrypted


def special_character(password):
    """Check if password contains a special character, returns True/False."""

    # Check if a character falls within a range of common special characters.

    # Looping through each character in the password
    for character in password:

        # Checking for a special character
        if (
            33 <= ord(character) <= 47
            or 58 <= ord(character) <= 64
            or 91 <= ord(character) <= 96
        ):

            # Breaks the function and returns true
            return True

    # If no special character is found, returns false
    return False


def username_exists(username):
    """Check whether a username is already registered, return True/False."""

    # Checking if file exists
    try:

        # Opening file
        with open("progress.txt", "r") as file:

            # Making a list of all info
            for line in file:
                data = line.strip().split(",")

                # Checking for username
                if data[0].lower() == username.lower():
                    return True

    # If file doesn't exist
    except FileNotFoundError:
        return False

    return False


def load_progress(name, password):
    """Load saved progress after checking the user's password."""

    try:

        # Open the progress file so the user's saved data can be checked
        with open("progress.txt", "r") as file:

            # Go through each saved user's information
            for line in file:

                # Remove whitespace and split the data into separate values
                data = line.strip().split(",")

                # Check if the name and password match the saved account
                if data[0].lower() == name.lower() and data[1] == password:

                    # Load the user's achievements if they have any saved
                    if data[6]:
                        achievements = data[6].split("|")
                    else:
                        achievements = []

                    # Load the user's learned words if they have any
                    # data [7] stores all learned words, separated by "|"
                    if len(data) > 7 and data[7]:
                        learned_words = data[7].split("|")
                    else:
                        # If the user has not learned any words,
                        # create an empty list.
                        learned_words = []

                    # Store the user's saved progress in a dictionary

                    # The data indexes match the order of information
                    # in the progress.txt file
                    # data[2] = XP
                    # data[3] = total questions answered
                    # data[4] = total correct answers
                    # data[5] = highest streak
                    # data[6] = saved achievements

                    stats = {
                        "xp": int(data[2]),
                        "questions_answered": int(data[3]),
                        "correct_answers": int(data[4]),
                        "current_streak": 0,
                        "highest_streak": int(data[5]),
                        "achievements": achievements
                    }

                    # Return the saved statistics and learned words
                    return stats, learned_words, data[0]

    # If the progress file does not exist, no saved progress can be loaded
    except FileNotFoundError:
        return None

    # Return None if no matching account was found
    return None


def save_progress(name, password, stats, learned_words):
    """Save or update a user's progress in the progress file."""

    lines = []
    found = False

    # Checking if file exists
    try:

        # Opening and reading file
        with open("progress.txt", "r") as file:
            lines = file.readlines()

    # If file doesn't exist
    except FileNotFoundError:
        pass

    # Opening progress file
    with open("progress.txt", "w") as file:

        # Looping through file
        for line in lines:

            # Forming list of data
            data = line.strip().split(",")

            # If first item matches name
            if data[0] == name:

                # Adding user stats
                file.write(
                    f"{name},{password},{stats['xp']},"
                    f"{stats['questions_answered']},"
                    f"{stats['correct_answers']},"
                    f"{stats['highest_streak']},"
                    f"{'|'.join(stats['achievements'])},"
                    f"{'|'.join(learned_words)}\n"
                )

                found = True

            else:
                file.write(line)

        # If user doesn't already exist in file
        if not found:

            # Adding user stats
            file.write(
                f"{name},{password},{stats['xp']},"
                f"{stats['questions_answered']},"
                f"{stats['correct_answers']},"
                f"{stats['highest_streak']},"
                f"{'|'.join(stats['achievements'])},"
                f"{'|'.join(learned_words)}\n"
            )


def create_account():
    """Create a new account with a unique username and password."""

    while True:

        # Asking the user for a username
        username = input("Create a username: ").strip()

        # Username restrictions
        if username == "":
            print("Username cannot be empty.")

        elif " " in username:
            print("Username cannot contain spaces.")

        elif "," in username:
            print("Username cannot contain commas.")

        elif username_exists(username):
            print("That username is already taken.")

        else:
            break

    while True:

        # Printing password requirements
        print("\nPassword requirements:")
        print("- At least 6 characters")
        print("- Must contain a special character")
        print("- Cannot contain commas\n")

        # Asking the user for a password
        password = input("Create a password: ").strip()

        # Password restrictions
        if password == "":
            print("Password cannot be empty.")

        elif len(password) < 6:
            print("Password must be at least 6 characters long.")

        elif " " in password:
            print("Password cannot contain spaces.")

        elif "," in password:
            print("Password cannot contain commas")

        elif not special_character(password):
            print("Password must contain at least one special character.")

        else:
            break

    # Encrypting the password
    encrypted_password = caesar_encrypt(password)

    # Defining the user's starting statistics
    stats = {
        "xp": 0,
        "questions_answered": 0,
        "correct_answers": 0,
        "current_streak": 0,
        "highest_streak": 0,
        "achievements": []
    }

    # Creating an empty list for learned words
    learned_words = []

    # Saving the new account to the progress file
    with open("progress.txt", "a") as file:
        file.write(
            f"{username},{encrypted_password},0,0,0,0,,\n"
        )

    print(f"Account created! Welcome, {username}!")

    return username, encrypted_password, stats, learned_words


def login():
    """Log an existing user into their account."""

    # Asking the user for their login details
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # Encrypting the entered password so it can be compared
    # with the encrypted password stored in the file
    encrypted_password = caesar_encrypt(password)

    # Loading the user's saved progress
    saved_progress = load_progress(username, encrypted_password)

    # If the login details are correct
    if saved_progress is not None:

        # Loading the saved statistics and learned words
        stats, learned_words, saved_username = saved_progress

        print(f"\nWelcome back, {saved_username}!")

        return (
            saved_username,
            encrypted_password,
            stats,
            learned_words
        )

    # If the login details are incorrect
    print("Incorrect username or password.")


def learn_beginner(dictionary, learned_words, count, stats):
    """Teach beginner vocabulary using flashcards."""

    words = list(dictionary.keys())

    # Loop through the requested number of words
    for index in range(count):

        # Select a random word
        word = random.choice(words)

        # Remove the word so it cannot be selected again
        words.remove(word)

        # Add the word to the learned words list
        if word not in learned_words:
            learned_words.append(word)

        # Getting the translation and pronunciation
        english = dictionary[word]["trans"].lower()
        pronunciation = dictionary[word]["pron"].lower()

        # Displaying the flashcard
        print("\n------------------------------------------------")
        flashcard_title = f"FLASHCARD {index + 1}/{count}"
        print(f"{flashcard_title:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{word:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{'↓':^{ARROW_WIDTH}}")
        print()
        print(f"{english:^{FLASHCARD_WIDTH}}")
        print()
        print(
            f"{'Pronunciation:':^{FLASHCARD_WIDTH}}"
        )
        print(f"{pronunciation:^{FLASHCARD_WIDTH}}")
        print("------------------------------------------------")

        input("\nPress Enter for the next word...")

        # Unlocking the First Steps achievement
        if (
            len(learned_words) == FIRST_WORD_REQUIRED
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")

            print("\n------------------------------------------------")
            print("☆ Achievement unlocked: First Steps!")
            print("You learned your first word!")
            print("------------------------------------------------")

    print("\n✰ Study Session Complete! ✰\n")


def learn_intermediate(
    phrase_dictionary,
    learned_words,
    count,
    stats
):
    """Teach intermediate phrases using flashcards."""

    phrases = list(phrase_dictionary.keys())

    # Loop through the requested number of phrases
    for index in range(count):

        # Select a random phrase
        phrase = random.choice(phrases)

        # Remove the phrase so it cannot be selected again
        phrases.remove(phrase)

        # Add the phrase to the learned words list
        if phrase not in learned_words:
            learned_words.append(phrase)

        # Getting the translation and pronunciation
        english = phrase_dictionary[phrase]["trans"].lower()
        pronunciation = phrase_dictionary[phrase]["pron"].lower()

        # Displaying the flashcard
        print("\n--------------------------------")
        flashcard_title = f"FLASHCARD {index + 1}/{count}"
        print(f"{flashcard_title:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{phrase:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{'↓':^{ARROW_WIDTH}}")
        print()
        print(f"{english:^{FLASHCARD_WIDTH}}")
        print()
        print(
            f"{'Pronunciation:':^{FLASHCARD_WIDTH}}"
        )
        print(f"{pronunciation:^{FLASHCARD_WIDTH}}")
        print("--------------------------------")

        input("\nPress Enter for the next phrase...")

        # Unlocking the First Steps achievement
        if (
            len(learned_words) == FIRST_WORD_REQUIRED
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")

            print("\n--------------------------------")
            print("☆ Achievement unlocked: First Steps!")
            print("You learned your first word!")
            print("--------------------------------")

    print("\n✰ Study Session Complete! ✰\n")


def quiz(dictionary, count, stats):
    """Quiz the user on vocabulary and update their statistics."""

    score = 0

    # Clearing the screen before starting the quiz
    for i in range(CLEAR_SCREEN):
        print("")

    words = list(dictionary.keys())

    # Loop through the requested number of questions
    for index in range(count):

        # Select a random word
        word = random.choice(words)

        # Remove the word so it cannot be selected again
        words.remove(word)

        # Getting the English translation
        english = dictionary[word]["trans"].lower()

        # Asking the user for an answer
        while True:
            response = input(
                f"What is the translation of {word}? "
            ).strip().lower()

            # Checking for an empty answer
            if response == "":
                print("Please enter an answer.")

            # Checking if the answer is a number
            elif response.isdigit():
                print("Please enter a word, not a number.")

            else:
                break

        # Updating the total number of questions
        stats["questions_answered"] += 1

        # Checking if the answer is correct
        if response == english:

            print("Correct!")

            # Updating score and statistics
            score += 1
            stats["correct_answers"] += 1
            stats["xp"] += XP_PER_CORRECT
            stats["current_streak"] += 1

            # Updating the highest streak if necessary
            if stats["current_streak"] > stats["highest_streak"]:
                stats["highest_streak"] = stats["current_streak"]

            # Checking for the five correct answers achievement
            if (
                stats["correct_answers"] == QUESTIONS_ACHIEVEMENT
                and "No translation needed !!"
                not in stats["achievements"]
            ):
                stats["achievements"].append(
                    "No translation needed !!"
                )

                print("\n" + "-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "No translation needed !!"
                )
                print("Answer 5 questions right")
                print("-" * SEPARATOR_LENGTH)

            # Checking for the five-question streak achievement
            if (
                stats["current_streak"] == STREAK_ACHIEVEMENT
                and "5 STREAK !!" not in stats["achievements"]
            ):
                stats["achievements"].append("5 STREAK !!")

                print("\n" + "-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "5 STREAK !! 🔥🔥🔥"
                )
                print(
                    "You answered 5 questions right in a row !!"
                )
                print("-" * SEPARATOR_LENGTH)

        # If the answer is incorrect
        else:
            print(
                f"Wrong :( The correct answer is {english}"
            )

            # Resetting the current streak
            stats["current_streak"] = 0

    print("\n✰Well Done✰\n")

    return score
