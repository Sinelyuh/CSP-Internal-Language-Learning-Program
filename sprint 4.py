import random

# constants used throughout the program
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
    """Encrypt a password using a caesar cipher, returns encrypted password"""

    # defining string to be edited later
    encrypted = ""

    # looping through every character in the password 
    for character in password:
        
        # in the case of letters
        if character.isalpha():

            # if uppercase
            if character.isupper():

                # encrypting using unicodes
                encrypted += chr((ord(character) - ord("A") + CAESAR_KEY) % ALPHABET_LETTERS + ord("A"))
      
            # if lowercase
            else:

                # encrypting using unicodes
                encrypted += chr((ord(character) - ord("a") + CAESAR_KEY) % ALPHABET_LETTERS + ord("a"))

        # in the case of digits
        elif character.isdigit():
            
            encrypted += str((int(character) + CAESAR_KEY) % 10 )

        # in the case of special characters
        # ranges of constants taken from ASCII value tables
        elif 33 <= ord(character) <= 47:
            encrypted += chr((ord(character) - 33 + CAESAR_KEY) % 15 + 33)

        # in the case of special characters
        # ranges of constants taken from ASCII value tables
        elif 58 <= ord(character) <= 64:
            encrypted += chr((ord(character) - 58 + CAESAR_KEY) % 7 + 58)

        # in the case of special characters
        # ranges of constants taken from ASCII value tables
        elif 91 <= ord(character) <= 96:
            encrypted += chr((ord(character) - 91 + CAESAR_KEY) % 6 + 91)

        else:
            encrypted += character

    return encrypted


def special_character(password):
    """Check if the password contains a special character, returns true/false """
    
    # check if one of the characters falls within a range of common special characters

    # looping through each character in the password
    for character in password:
        # checking for a special character
        if 33 <= ord(character) <= 47 or 58 <= ord(character) <= 64 or 91 <= ord(character) <= 96:
            # breaks the function and returns true
            return True
    
    # if no special character is found, returns false
    return False
  

def username_exists(username):
    """check whether a username is already registered, return True/False"""

    # checking if file exists
    try:
        # opening file
        with open("progress.txt", "r") as file:

            # making a list of all info
            for line in file:
                data = line.strip().split(",")

                # checking for username
                if data[0].lower() == username.lower():
                    return True

    # if file doesn't exist
    except FileNotFoundError:
        return False

    return False


def load_progress(name, password):
    """load a user's saved progress after checking their password, returns saved info"""

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
                        # if the user hasn’t learned any words, an empty list is created
                        learned_words = []

                    # Store the user's saved progress in a dictionary
                    # the data indexes match the order of information to the progress.txt file
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
    """save or update a user's progress in the progress file"""

    lines = []
    found = False

    # checking if file exists
    try:
        # opening and reading file
        with open("progress.txt", "r") as file:
            lines = file.readlines()

    # if file doesn't exist
    except FileNotFoundError:
        pass

    # opening progress file
    with open("progress.txt", "w") as file:

        #looping through file
        for line in lines:

            #forming list of data
            data = line.strip().split(",")

            # if first item matches name
            if data[0] == name:

                #adding user stats
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

        # if user doesn't already exist in file
        if not found:

            # adding user stats
            file.write(
                f"{name},{password},{stats['xp']},"
                f"{stats['questions_answered']},"
                f"{stats['correct_answers']},"
                f"{stats['highest_streak']},"
                f"{'|'.join(stats['achievements'])},"
                f"{'|'.join(learned_words)}\n"
            )

def create_account():
    """create a new account with a unique username and password"""

    while True:
        # asking the user for a username
        username = input("Create a username: ").strip()

        # username restrictions
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
        # printing password requirements
        print("\nPassword requirements:")
        print("- At least 6 characters")    
        print("- Must contain a special character") 
        print("- Cannot contain commas \n")

        # asking the user for a password
        password = input("Create a password: ").strip()

        # password restrictions
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

    # encrypting the password
    encrypted_password = caesar_encrypt(password)

    # defining the user's starting statistics
    stats = {
        "xp": 0,
        "questions_answered": 0,
        "correct_answers": 0,
        "current_streak": 0,
        "highest_streak": 0,
        "achievements": []
    }

    # creating an empty list for learned words
    learned_words = []

    # saving the new account to the progress file
    with open("progress.txt", "a") as file:
        file.write(f"{username},{encrypted_password},0,0,0,0,,\n")

    print(f"Account created! Welcome, {username}!")

    return username, encrypted_password, stats, learned_words


def login():
    """Log an existing user into their account."""

    # asking the user for their username
    username = input("Enter your username: ").strip()

    # asking the user for their password
    password = input("Enter your password: ").strip()

    # encrypting the password before checking it
    encrypted_password = caesar_encrypt(password)

    # checking the username and encrypted password
    saved_progress = load_progress(username, encrypted_password)

    if saved_progress is not None:

        # finding the exact username saved in the file
        stats, learned_words, saved_username = saved_progress

        print(f"Welcome back, {saved_username}!")

        return (
            saved_username,
            encrypted_password,
            stats,
            learned_words
        )

    else:
        print("Incorrect username or password.")


def learn_beginner(dictionary, learned_words, count, stats):
    """beginner learning level, prints flashcards for basic Norwegian words"""

    # making a list of words
    words = list(dictionary.keys())

    # looping through as many words as requested
    for index in range(count):

        # choosing a word from the previously defined list
        word = random.choice(words)

        # removing a word once it has been chosen
        words.remove(word)

        # adding a word to a list of learned words if it isn't already there
        if word not in learned_words:
            learned_words.append(word)

        # defining the translation and pronunciation of words
        english = dictionary[word]["trans"].lower()
        pronunciation = dictionary[word]["pron"].lower()

        # making flashcards
        print("\n------------------------------------------------")

        print(f"{'FLASHCARD ' + str(index + 1) + '/' + str(count):^{FLASHCARD_WIDTH}}")
        print()
        print(f"{word:^{FLASHCARD_WIDTH}}")
        print(f"{'↓':^{FLASHCARD_WIDTH}}")
        print(f"{english:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{'Pronunciation:':^{FLASHCARD_WIDTH}}")
        print(f"{pronunciation:^{FLASHCARD_WIDTH}}")

        print("------------------------------------------------")
        input("Press Enter for the next word...")

        # achievement when the user learns their first word
        if (
            len(learned_words) == FIRST_WORD_REQUIRED
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")
            print("-" * SEPARATOR_LENGTH)
            print("☆ Achievement unlocked: First Steps!")
            print("You learned your first word!")
            print("-" * SEPARATOR_LENGTH)

    # message when lesson is finished
    print("\n✰ Study Session Complete! ✰\n")
    print()


def learn_intermediate(phrase_dictionary, learned_words, count, stats):
    """Learn phrases of Norwegian using flashcards."""

    # making a list of phrases
    phrases = list(phrase_dictionary.keys())

    # looping through as many phrases as requested
    for index in range(count):

        # choosing a phrase from the previously defined list
        phrase = random.choice(phrases)

        # removing a phrase once it has been chosen
        phrases.remove(phrase)

        # adding a phrase to learned items if it isn't already there
        if phrase not in learned_words:
            learned_words.append(phrase)
        
        # defining the translation and pronunciation of phrases
        english = phrase_dictionary[phrase]["trans"].lower()
        pronunciation = phrase_dictionary[phrase]["pron"].lower()

        # making flashcards
        print("\n--------------------------------")

        print(f"{'FLASHCARD ' + str(index + 1) + '/' + str(count):^{FLASHCARD_WIDTH}}")
        print()
        print(f"{phrase:^{FLASHCARD_WIDTH}}")
        print(f"{'↓':^{ARROW_WIDTH}}")
        print(f"{english:^{FLASHCARD_WIDTH}}")
        print()
        print(f"{'Pronunciation:':^{FLASHCARD_WIDTH}}")
        print(f"{pronunciation:^{FLASHCARD_WIDTH}}")

        print("--------------------------------")
        input("Press Enter for the next word...")

        # achievement when the user learns their first word
        if (
            len(learned_words) == FIRST_WORD_REQUIRED
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")
            print("-" * SEPARATOR_LENGTH)
            print("Achievement Unlocked: First Steps!")
            print("You learned your first word!")
            print("-" * SEPARATOR_LENGTH)

    # message when lesson is finished
    print("\n✰ Study Session Complete! ✰\n")
    print()


def quiz(dictionary, count, stats):
    """Ask users for the English translations of Norwegian words."""

    # defining the user's score in the current quiz session
    score = 0

    
    # clearing screen
    for i in range(CLEAR_SCREEN):
        print("") 

    # setting a variable for the keys of the dictionary
    words = list(dictionary.keys())

    # looping through as many words as the user wants
    for index in range(count):

        # ensures each question is asked in random order
        word = random.choice(words)

        # removes words already asked, preventing repetition
        words.remove(word)
        english = dictionary[word]["trans"].lower()

        # getting the user's answer
        while True:
            print()
            response = input(
                f"What is the translation of {word}? "
            ).strip().lower()

            # making sure the user gives an answer
            if response == "":
                print("Please enter an answer")
                
            # making sure input is not a number
            elif response.isdigit():
                print("Please enter a word, not a number")

            else:
                break

        # tracking how many questions have been answered
        stats["questions_answered"] += 1

        # checking if their answer is correct
        if response == english:
            print("Correct :)")

            # updating all necessary stats
            score += 1
            stats["correct_answers"] += 1
            # adding the set amount of XP for a correct answer
            stats["xp"] += XP_PER_CORRECT
            stats["current_streak"] += 1

            # updating highest streak
            if stats["current_streak"] > stats["highest_streak"]:
                stats["highest_streak"] = stats["current_streak"]

            # checking if the user earned any achievements
            if (
                stats["correct_answers"] == QUESTIONS_ACHIEVEMENT
                and "No translation needed !!" not in stats["achievements"]
            ):
                stats["achievements"].append("No translation needed !!")
                print("-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "No translation needed !!"
                )
                print("Answer 5 questions right")
                print("-" * SEPARATOR_LENGTH)
                
            if (
                stats["current_streak"] == STREAK_ACHIEVEMENT
                and "5 STREAK !!" not in stats["achievements"]
            ):
                stats["achievements"].append("5 STREAK !!")
                print("-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "5 STREAK !!🔥🔥🔥"
                )
                print("You answered 5 questions right in a row !!")
                print("-" * SEPARATOR_LENGTH)

        # if their answer is wrong
        else:
            print(f"Wrong :( The correct answer is {english}")
            stats["current_streak"] = 0

    # congratulate at the end of the lesson
    print()
    print("✰Well Done✰")
    print()
    return score


def quiz_learned(
    dictionary, phrase_dictionary, learned_words, count, stats
):
    """Quiz users on words they have previously learnt."""

    # defining the user's score in the current quiz session
    score = 0
    
    # clearing screen
    for i in range(CLEAR_SCREEN):
        print("") 

    # making a copy so items can be removed without changing
    # the original learned_words list
    words = learned_words.copy()

    for index in range(count):

        # choosing a random word
        word = random.choice(words)
        words.remove(word)

        # defining its translation depending on its dictionary
        if word in dictionary:
            english = dictionary[word]["trans"].lower()

        elif word in phrase_dictionary:
            english = phrase_dictionary[word]["trans"].lower()

        # asking the user their answer
        while True:
            print()
            response = input(
                f"What is the translation of {word}? "
            ).strip().lower()

            # making sure the input is not an empty string
            if response == "":
                print("Please enter an answer")

            # making sure input is not a number   
            elif response.isdigit():
                print("Please enter a word, not a number")

            else:
                break

        # tracking how many questions have been answered
        stats["questions_answered"] += 1

        # checking the answer
        if response == english:
            print("Correct :)")

            # updating all necessary stats
            score += 1
            stats["correct_answers"] += 1
            # adding the set amount of XP for a correct answer
            stats["xp"] += XP_PER_CORRECT
            stats["current_streak"] += 1

            # updating highest streak
            if stats["current_streak"] > stats["highest_streak"]:
                stats["highest_streak"] = stats["current_streak"]

            # checking if the user earned any achievements
            if (
                stats["correct_answers"] == QUESTIONS_ACHIEVEMENT
                and "No translation needed !!" not in stats["achievements"]
            ):
                stats["achievements"].append("No translation needed !!")
                print("-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "No translation needed !!"
                )
                print("Answer 5 questions right")
                print("-" * SEPARATOR_LENGTH)

            if (
                stats["current_streak"] == STREAK_ACHIEVEMENT
                and "5 STREAK !!" not in stats["achievements"]
            ):
                stats["achievements"].append("5 STREAK !!")
                print("-" * SEPARATOR_LENGTH)
                print(
                    "☆ Achievement unlocked: "
                    "5 STREAK !!🔥🔥🔥"
                )
                print("You answered 5 questions right in a row !!")
                print("-" * SEPARATOR_LENGTH)

        # if their answer is wrong
        else:
            print(f"Wrong :( The correct answer is {english}")
            stats["current_streak"] = 0

    # congratulate at the end of the lesson
    print()
    print("✰Well Done✰")
    print()
    return score


if __name__ == "__main__":

    # defining global information needed through the whole program
    dictionary = {
        "Hei": {"trans": "Hello", "pron": "hey"},
        "Ha det": {"trans": "Goodbye (less formal)", "pron": "hah-deh"},
        "God morgen": {"trans": "Good morning", "pron": "goo mor-gen"},
        "God dag": {"trans": "Good day", "pron": "goo dahg"},
        "God kveld": {"trans": "Good evening", "pron": "goo kvel"},
        "Takk": {"trans": "Thank you", "pron": "tahk"},
        "Beklager": {"trans": "I'm sorry", "pron": "beh-klah-ger"},
        "Vær så snill": {"trans": "Please", "pron": "vair soh snill"},
        "Unnskyld": {"trans" : "Excuse me", "pron": "oon-shill"},
        "Ja": {"trans": "Yes", "pron": "yah"},
        "Nei": {"trans": "No", "pron": "nigh"},
        "God natt": {"trans": "Good night", "pron": "goo naht"},
        "Velkommen": {"trans": "Welcome", "pron": "vel-kom-men"},
        "Skål": {"trans": "Cheers", "pron": "skohl"},
        "Mor": {"trans": "Mother", "pron": "moor"},
        "Far": {"trans": "Father", "pron": "fahr"},
        "Søster": {"trans": "Sister", "pron": "sur-ster"},
        "Bror": {"trans": "Brother", "pron": "broor"},
        "Datter": {"trans": "Daughter", "pron": "daht-ter"},
        "Sønn": {"trans": "Son", "pron": "surn"},
        "Bestemor": {"trans": "Grandmother", "pron": "bes-teh-moor"},
        "Bestefar": {"trans": "Grandfather", "pron": "bes-teh-fahr"},
        "Tante": {"trans": "Aunt", "pron": "tahn-teh"},
        "Onkel": {"trans": "Uncle", "pron": "ong-kel"},
        "Venn": {"trans": "Friend (male)", "pron": "ven"},
        "Taxi": {"trans": "Taxi", "pron": "tak-see"},
        "Kone": {"trans": "Wife", "pron": "koo-neh"},
        "Mann": {"trans": "Husband", "pron": "mahn"},
        "Tog": {"trans": "Train", "pron": "toog"},
        "Buss": {"trans": "Bus", "pron": "booss"}
    }


    phrase_dictionary = {
        "Hvordan går det?": {"trans": "How are you", "pron": "vor-dan gor deh"},
        "Det går bra": {"trans": "I'm doing well.", "pron": "deh gor brah"},
        "Hva heter du": {"trans": "What is your name", "pron": "vah hay-ter doo"},
        "Jeg heter": {"trans": "My name is...", "pron": "yai hay-ter"},
        "Hyggelig å møte deg": {"trans": "Nice to meet you", "pron": "hig-eh-lee oh muh-teh die"},
        "Hvor kommer du fra": {"trans": "Where are you from", "pron": "vor kom-er doo frah"},
        "Jeg kommer fra New Zealand": {"trans": "I come from New Zealand", "pron": "yai kom-er frah noo zee-lahnd"},
        "Hvor bor du": {"trans": "Where do you live", "pron": "vor boor doo"},
        "Jeg bor i Wellington": {"trans": "I live in Wellington", "pron": "yai boor ee wel-ling-ton"},
        "Kan du hjelpe meg": {"trans": "Can you help me", "pron": "kahn doo yelp-eh my"},
        "Jeg forstår ikke": {"trans": "I don't understand", "pron": "yai for-stor ik-eh"},
        "Kan du gjenta det": {"trans": "Can you repeat that", "pron": "kahn doo yen-tah deh"},
        "Kan du snakke saktere": {"trans": "Can you speak more slowly", "pron": "kahn doo snak-eh sahk-ter-eh"},
        "Snakker du engelsk": {"trans": "Do you speak English", "pron": "snak-er doo eng-elsk"},
        "Jeg snakker litt norsk": {"trans": "I speak a little Norwegian", "pron": "yai snak-er lit norshk"},
        "Jeg lærer norsk": {"trans": "I am learning Norwegian", "pron": "yai lair-er norshk"},
        "Hva gjør du": {"trans": "What are you doing", "pron": "vah yur doo"},
        "Jeg vet ikke": {"trans": "I don't know", "pron": "yai vayt ik-eh"},
        "Jeg er sulten": {"trans": "I am hungry", "pron": "yai air sool-ten"},
        "Jeg er tørst": {"trans": "I am thirsty", "pron": "yai air turst"},
        "Jeg vil ha vann": {"trans": "I want water", "pron": "yai vil hah vahn"},
        "Jeg vil ha kaffe": {"trans": "I want coffee", "pron": "yai vil hah kah-feh"},
        "Hvor er toalettet": {"trans": "Where is the bathroom", "pron": "vor air too-ah-let-eh"},
        "Hva er klokken": {"trans": "What time is it", "pron": "vah air klok-en"},
        "Jeg er klar": {"trans": "I am ready", "pron": "yai air klar"},
        "Jeg er sliten": {"trans": "I am tired", "pron": "yai air slee-ten"},
        "Jeg liker dette": {"trans": "I like this", "pron": "yai lee-ker det-eh"},
        "Jeg elsker Norge": {"trans": "I love Norway", "pron": "yai el-sker nor-geh"},
        "Ha en fin da": {"trans": "Have a nice day", "pron": "hah en feen dahg"},
        "Vi sees senere": {"trans": "See you later", "pron": "vee says seh-neh-reh"}
    }

    learned_words = []

    stats = {
        "xp": 0,
        "questions_answered": 0,
        "correct_answers": 0,
        "current_streak": 0,
        "highest_streak": 0,
        "achievements": []
    }

    while True:

        # printing account meni
        print("\n--- Account Menu ---")
        print("1. Create account")
        print("2. Log in")
        print("3. Exit")

        # asking the user what they want to do
        account_choice = input("Choice: ").strip()

        # if user creates new account
        if account_choice == "1":

            name, password, stats, learned_words = create_account()
            break

        # if account already exists
        elif account_choice == "2":

            login_result = login()

            if login_result is not None:
                
                # loading user info
                name, password, stats, learned_words = login_result
                break
            
        # if user wants to exit
        elif account_choice == "3":
            exit()

        else:
            print("Please choose 1 or 2.")


    # disclaimer
    print("\n ---- Pronunication Disclaimer ---- \n")
    print("The pronunciations provided are approximate guides")
    print("Norwegian pronunciations can vary depending on dialect")
    print("")
    print("--- Norwegian Learning App ---")

    # looping until the user chooses to exit the program
    while True:

        # main menu
        print("1. learn")
        print("2. quiz")
        print("3. view statistics")
        print("4. view achievements")
        print("5. exit")
        print()

        # asking user what they want to do
        choice = input("Number choice: ").strip()

        if choice == "1":

            # ensuring a valid difficulty is chosen
            while True:

                # printing learning levels
                print("\n--- Learning Levels ---")
                print("1. Beginner")
                print("2. Intermediate")
                print()

                # asking what level they want to learn at
                difficulty_choice = input(
                    "What difficulty level do you want to learn at? "
                ).strip()

                if difficulty_choice == "1":
                    break

                elif difficulty_choice == "2":
                    break

                else:
                    print("Please enter a valid option")

            while True:
                try:

                    # asking how many words they want to learn
                    count = int(
                        input(
                            "Enter how many words/phrases you want to learn:\n"
                        )
                    )

                    # setting the maximum number of items based on the dictionary being used
                    if difficulty_choice == "1":
                        max_count = len(dictionary)
                    else:
                        max_count = len(phrase_dictionary)

                    # making sure the word is within the limit
                    if count < MIN_COUNT or count > max_count:
                        print(
                            f"Please enter a number between {MIN_COUNT} and {max_count}"
                        )
                    else:
                        break

                # if user input is not a valid number
                except ValueError:
                    print("Please enter a valid number")

            if difficulty_choice == "1":

                # running beginner learning
                learn_beginner(
                    dictionary, learned_words, count, stats
                )

            elif difficulty_choice == "2":

                # running intermediate learning
                learn_intermediate(
                    phrase_dictionary, learned_words, count, stats
                )

        elif choice == "2":

            # looping until valid input
            while True:

                # printing options for quizzing
                print("\n--- Quizzing Options ---")
                print("1. Quiz on random words")
                print("2. Quiz on previously learned words")
                print()

                # asking user what they want to do
                quiz_choice = input("Choice? ").strip()

                if quiz_choice == "1":

                    while True:
                        
                        try:
                            # asking how many questions the user wants
                            count = int( input( "Enter how many questions you want to do: "))

                            # setting the maximum number of questions to the number of available words
                            max_count = len(dictionary)

                            # checking if input is within the valid range
                            if count < MIN_COUNT or count > max_count:
                                print(
                                    f"Please enter a number between {MIN_COUNT} and {max_count}."
                                )
                            else:
                                break

                        # if user does not input a valid number
                        except ValueError:
                            print("Please enter a valid number")

                    # running the quiz function
                    score = quiz(dictionary, count, stats)

                    print(
                        f"You got {score}/{count} questions right"
                    )

                    print()
                    break

                elif quiz_choice == "2":

                    # defining maximum possible learned words
                    max_words = len(learned_words)

                    # if user hasn't learned any words yet
                    if max_words == 0:
                        print(
                            "Learn some words in order to use "
                            "this feature :)"
                        )
                        break

                    # if user has learned words
                    else:
                        
                        while True:
                            try:
                                # asking for the user's input
                                count = int(
                                    input("Enter how many questions you want to do: "))

                                # making sure input fits within valid range
                                if count < MIN_COUNT or count > max_words:
                                    print(
                                        f"Please enter a number between 1 and {max_words}"
                                    )
                                else:
                                    break

                            # making sure input is a valid number
                            except ValueError:
                                print("Please enter a valid number")

                        # running function and updating score
                        score = quiz_learned(
                            dictionary,
                            phrase_dictionary,
                            learned_words,
                            count,
                            stats
                        )

                        print(
                            f"You got {score}/{count} questions right"
                        )

                        print()
                        break

                # in case a valid quiz choice is not made
                else:
                    print("Please choose a valid option")

        elif choice == "3":

            # defining all of the user's statistics
            # calculating the user's level from their XP
            level = stats["xp"] // XP_PER_LEVEL

            # calculating number of wrong answers
            incorrect_answers = (
                stats["questions_answered"]
                - stats["correct_answers"]
            )

            # if user has answered questions
            if stats["questions_answered"] > 0:
                # calculating accuracy
                accuracy = (
                    stats["correct_answers"]
                    / stats["questions_answered"]
                ) * PERCENT
                
            else:
                accuracy = 0

            # printing all statistics neatly
            print("-------- Your Statistics --------")
            print(f"XP: {stats['xp']}")
            print(f"Level: {level}")
            print(
                f"Total questions answered: "
                f"{stats['questions_answered']}"
            )
            print(f"Correct answers: {stats['correct_answers']}")
            print(f"Incorrect answers: {incorrect_answers}")
            print(f"Accuracy: {accuracy:.1f}%")
            print(f"Total words learned: {len(learned_words)}")
            print(f"Highest streak: {stats['highest_streak']}")
            print()

        elif choice == "4":

            # printing achievements menu
            while True:
                print("-------- Achievements --------")
                print("1. View all achievements")
                print("2. View earned achievements")
                print("3. Back")
                print()
 
                # asking the user what they want to do
                achievement_choice = input("Choice: ").strip()
  
                # viewing all achievements
                if achievement_choice == "1":
   
                    # neatly printing a menu of all achievements
                    print()
                    print("-------- All Achievements --------")
                    print("1. First Steps")
                    print("   Learn your first word or phrase.")
                    print()
                    print("2. No translation needed !!")
                    print("   Answer 5 questions correctly.")
                    print()
                    print("3. 5 STREAK !!")
                    print("   Answer 5 questions correctly in a row.")
                    print()

                # viewing earned achievements
                elif achievement_choice == "2":

                    # heading
                    print()
                    print("-------- Your Achievements --------")

         
                    if len(stats["achievements"]) == 0:

                        # in case the user has no achievements
                        print("No achievements earned yet :(")

                    else:
              
                        # printing achievements neatly
                        for achievement in stats["achievements"]:
                            print("✰" + achievement)
                            print()
 
                # exiting achievements menu
                elif achievement_choice == "3":
                    break

                # if invalid option chosen
                else:
                    print("Please choose a valid option.")


        elif choice == "5":

            #saving progress
            print("Progress saved!")
            save_progress(name, password, stats, learned_words)


            # exiting the program
            print("Goodbye!")
            break

        else:

            # in case a valid choice for main menu was not made
            print("Invalid choice. Please select a valid option")  
