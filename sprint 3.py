# Making code to help people learn Norwegian

import random

def learn_beginner(dictionary, learned_words, count, stats):
    """Beginner learning level, prints flashcards for basic Norwegian words."""

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
        print(f"\n--- Flashcard {index + 1}/{count} ---")
        print(f"The Norwegian word for {english} is {word}")
        print(f"How to say it: [{pronunciation}]")
        print("-" * 25)
        input("Press Enter for the next word...")

        # achievement when the user learns their first word
        if (
            len(learned_words) == 1
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")
            print("-" * 50)
            print("☆ Achievement unlocked: First Steps!")
            print("You learned your first word!")
            print("-" * 50)

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

        # adding the phrase to learned items if it isn't already there
        if phrase not in learned_words:
            learned_words.append(phrase)
        
        # defining the translation and pronunciation of phrases
        english = phrase_dictionary[phrase]["trans"].lower()
        pronunciation = phrase_dictionary[phrase]["pron"].lower()

        # making flashcards
        print(f"\n--- Flashcard {index + 1}/{count} ---")
        print(f"The Norwegian translation for {english} is {phrase}")
        print(f"How to say it: [{pronunciation}]")
        print("-" * 25)
        input("Press Enter for the next word...")

        # achievement when the user learns their first word
        if (
            len(learned_words) == 1
            and "First Steps" not in stats["achievements"]
        ):
            stats["achievements"].append("First Steps")
            print("-" * 50)
            print("Achievement Unlocked: First Steps!")
            print("You learned your first word!")
            print("-" * 50)

    # message when lesson is finished
    print("\n✰ Study Session Complete! ✰\n")
    print()


def quiz(dictionary, count, stats):
    """Ask users for the English translations of Norwegian words."""

    # defining the user's score in the current quiz session
    score = 0

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
            stats["xp"] += 50
            stats["current_streak"] += 1

            # updating highest streak
            if stats["current_streak"] > stats["highest_streak"]:
                stats["highest_streak"] = stats["current_streak"]

            # checking if the user earned any achievements
            if (
                stats["correct_answers"] == 5
                and "No translation needed !!" not in stats["achievements"]
            ):
                stats["achievements"].append("No translation needed !!")
                print("-" * 50)
                print(
                    "☆ Achievement unlocked: "
                    "No translation needed !!"
                )
                print("Answer 5 questions right")
                print("-" * 50)
                
            if (
                stats["current_streak"] == 5
                and "5 STREAK !! " not in stats["achievements"]
            ):
                stats["achievements"].append("5 STREAK !! ")
                print("-" * 50)
                print(
                    "☆ Achievement unlocked: "
                    "5 STREAK !! 🔥🔥🔥"
                )
                print("You answered 5 questions right in a row !!")
                print("-" * 50)

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

    score = 0

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
            stats["xp"] += 50
            stats["current_streak"] += 1

            # updating highest streak
            if stats["current_streak"] > stats["highest_streak"]:
                stats["highest_streak"] = stats["current_streak"]

            # checking if the user earned any achievements
            if (
                stats["correct_answers"] == 5
                and "No translation needed !!" not in stats["achievements"]
            ):
                stats["achievements"].append("No translation needed !!")
                print("-" * 50)
                print(
                    "☆ Achievement unlocked: "
                    "No translation needed !!"
                )
                print("Answer 5 questions right")
                print("-" * 50)

            if (
                stats["current_streak"] == 5
                and "5 STREAK !! " not in stats["achievements"]
            ):
                stats["achievements"].append("5 STREAK !! ")
                print("-" * 50)
                print(
                    "☆ Achievement unlocked: "
                    "5 STREAK !! 🔥🔥🔥"
                )
                print("You answered 5 questions right in a row !!")
                print("-" * 50)

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
        "Venninne": {"trans": "Friend (female)", "pron": "ven-in-neh"},
        "Kone": {"trans": "Wife", "pron": "koo-neh"},
        "Mann": {"trans": "Husband", "pron": "mahn"},
        "Tog": {"trans": "Train", "pron": "toog"},
        "Buss": {"trans": "Bus", "pron": "booss"}
        }


    phrase_dictionary = {
        "Hvordan går det?": {"trans": "How are you?", "pron": "vor-dan gor deh"},
        "Det går bra.": {"trans": "I'm doing well.", "pron": "deh gor brah"},
        "Hva heter du?": {"trans": "What is your name?", "pron": "vah hay-ter doo"},
        "Jeg heter...": {"trans": "My name is...", "pron": "yai hay-ter"},
        "Hyggelig å møte deg.": {"trans": "Nice to meet you", "pron": "hig-eh-lee oh muh-teh die"},
        "Hvor kommer du fra?": {"trans": "Where are you from?", "pron": "vor kom-er doo frah"},
        "Jeg kommer fra New Zealand.": {"trans": "I come from New Zealand", "pron": "yai kom-er frah noo zee-lahnd"},
        "Hvor bor du?": {"trans": "Where do you live?", "pron": "vor boor doo"},
        "Jeg bor i Wellington.": {"trans": "I live in Wellington", "pron": "yai boor ee wel-ling-ton"},
        "Kan du hjelpe meg?": {"trans": "Can you help me?", "pron": "kahn doo yelp-eh my"},
        "Jeg forstår ikke.": {"trans": "I don't understand", "pron": "yai for-stor ik-eh"},
        "Kan du gjenta det?": {"trans": "Can you repeat that?", "pron": "kahn doo yen-tah deh"},
        "Kan du snakke saktere?": {"trans": "Can you speak more slowly?", "pron": "kahn doo snak-eh sahk-ter-eh"},
        "Snakker du engelsk?": {"trans": "Do you speak English?", "pron": "snak-er doo eng-elsk"},
        "Jeg snakker litt norsk.": {"trans": "I speak a little Norwegian", "pron": "yai snak-er lit norshk"},
        "Jeg lærer norsk.": {"trans": "I am learning Norwegian", "pron": "yai lair-er norshk"},
        "Hva gjør du?": {"trans": "What are you doing?", "pron": "vah yur doo"},
        "Jeg vet ikke.": {"trans": "I don't know", "pron": "yai vayt ik-eh"},
        "Jeg er sulten.": {"trans": "I am hungry", "pron": "yai air sool-ten"},
        "Jeg er tørst.": {"trans": "I am thirsty", "pron": "yai air turst"},
        "Jeg vil ha vann.": {"trans": "I want water", "pron": "yai vil hah vahn"},
        "Jeg vil ha kaffe.": {"trans": "I want coffee", "pron": "yai vil hah kah-feh"},
        "Hvor er toalettet?": {"trans": "Where is the bathroom?", "pron": "vor air too-ah-let-eh"},
        "Hva er klokken?": {"trans": "What time is it?", "pron": "vah air klok-en"},
        "Jeg er klar.": {"trans": "I am ready", "pron": "yai air klar"},
        "Jeg er sliten.": {"trans": "I am tired", "pron": "yai air slee-ten"},
        "Jeg liker dette.": {"trans": "I like this", "pron": "yai lee-ker det-eh"},
        "Jeg elsker Norge.": {"trans": "I love Norway", "pron": "yai el-sker nor-geh"},
        "Ha en fin dag!": {"trans": "Have a nice day!", "pron": "hah en feen dahg"},
        "Vi sees senere.": {"trans": "See you later", "pron": "vee says seh-neh-reh"}
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

    # disclaimer
    print("\n ---- Pronounication Disclaimer ---- \n")
    print("The pronounciations provided are approximate guides")
    print("Norwegian pronounciations can vary depending on dialect")
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

        # asking the user what they want to do
        choice = input("Number choice: ").strip()

        if choice == "1":

            while True:
                try:
                    # asking the user how many words they want to learn
                    count = int(
                        input(
                            "Enter how many words you want to learn:\n"
                        )
                    )

                    # making sure the word is within the limit
                    if count < 1 or count > 30:
                        print(
                            "Please enter a number between 1 and 30"
                        )
                    else:
                        break

                # if user input is not a valid number
                except ValueError:
                    print("Please enter a valid number")

            # ensuring a valid difficulty is chosen
            while True:

                # printing learning levels
                print("1. Beginner")
                print("2. Intermediate")
                print()

                # asking the user what level they want to learn at
                difficulty_choice = input(
                    "What difficulty level do you want to learn at? "
                ).strip()

                if difficulty_choice == "1":

                    # running beginner learning
                    learn_beginner(
                        dictionary, learned_words, count, stats
                    )
                    break

                elif difficulty_choice == "2":

                    # running intermediate learning
                    learn_intermediate(
                        phrase_dictionary, learned_words, count, stats
                    )
                    break

                else:
                    print("Please enter a valid option")

        elif choice == "2":

            # looping until valid input
            while True:

                # printing options for quizzing
                print("1. Quiz on random words")
                print("2. Quiz on previously learned words")
                print()

                quiz_choice = input("Choice? ").strip()

                if quiz_choice == "1":

                    while True:
                        try:
                            # asking how many questions the user wants
                            count = int(
                                input(
                                    "Enter how many questions you "
                                    "want to do: "
                                )
                            )

                            # checking if input is within the valid range
                            if count < 1 or count > 30:
                                print(
                                    "Please enter a number between 1 and 30."
                                )
                            else:
                                break

                        # if the user does not input a valid number
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

                    if max_words == 0:
                        print(
                            "Learn some words in order to use "
                            "this feature :)"
                        )
                        break

                    else:
                        while True:
                            try:
                                # asking for the user's input
                                count = int(
                                    input(
                                        "Enter how many questions you "
                                        "want to do: "
                                    )
                                )

                                # making sure input fits within valid range
                                if count < 1 or count > max_words:
                                    print(
                                        f"Please enter a number between 1 "
                                        f"and {max_words}"
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
            level = stats["xp"] // 100 
            incorrect_answers = (
                stats["questions_answered"]
                - stats["correct_answers"]
            )

            if stats["questions_answered"] > 0:
                accuracy = (
                    stats["correct_answers"]
                    / stats["questions_answered"]
                ) * 100
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

            # printing achievements neatly
            print("-------- Your Achievements --------")

            if len(stats["achievements"]) == 0:

                # in case the user has no achievements
                print("No achievements earned yet :(")

            else:
                for achievement in stats["achievements"]:
                    print("✰" + achievement)
                    print()

        elif choice == "5":

            # exiting the program
            print("Goodbye!")
            break

        else:

            # in case a valid choice for main menu was not made
            print("Invalid choice. Please select a valid option")
