# Making code to help people learn norwegian
#
import random


def learn_beginner(dictionary, learned_words, count):
    """beginner learning level, prints flashcards explaining basic norwegian words"""
    # making a list of words
    words = list(dictionary.keys())

    # looping through as many words as the user wanted to
    for index in range(count):

        # choosing a word from the previously defined list
        word = random.choice(words)

        # removing a word once it has been chosen
        words.remove(word)

        # adding the word to a list of learned words
        learned_words.append(word)

        # defining the translation and pronunciations of words
        english = dictionary[word]["trans"].lower()
        pronunciation = dictionary[word]["pron"].lower()

        # making flashcards
        print(f"\n--- Flashcard {index + 1}/{count} ---")
        print(f"The norwegian word for {english} is {word}")
        print(f"How to say it: [{pronunciation}]")
        print("-" * 25)
        input("Press Enter for the next word...")

    # message when lesson is finished
    print("\n✰ Study Session Complete! ✰\n")


def learn_intermediate(phrase_dictionary, learned_words, count):
    """learn phrases of norwegian, prints flashcards of words and their info"""

    # making a list of phrases
    phrases = list(phrase_dictionary.keys()) 

    # looping through as many phrases as the user chose to
    for index in range(count):

        # choosing a phrase from the previously defined list
        phrase = random.choice(phrases)

        # removing a phrase once it has been chosen
        phrases.remove(phrase)

        # adding that word to a list of learned items
        learned_words.append(phrase)

        # defining the translation and pronunciations of phrases
        english = phrase_dictionary[phrase]["trans"].lower()
        pronunciation = phrase_dictionary[phrase]["pron"].lower()

        # making flashcards
        print(f"\n--- Flashcard {index + 1}/{count} ---")
        print(f"The norwegian translation for {english} is {phrase}")
        print(f"How to say it: [{pronunciation}]")
        print("-" * 25)
        input("Press Enter for the next word...")

    # message when lesson is finished
    print("\n✰ Study Session Complete! ✰\n")


def quiz(dictionary, count):
    """asks users the english words for norwegian words, returns score"""
    score = 0
    words = list(dictionary.keys())  # setting a variable for the key of each dictionary

    # looping through as many words as the user wants
    for index in range(count):

        # ensures each question is asked in random order
        word = random.choice(words)

        # removes words already asked, preventing repetition
        words.remove(word)
        english = dictionary[word]["trans"].lower()

        # getting answer from user to assess
        while True:
            response = input(f"\nWhat is the translation of {word}? ").strip().lower()
            
            #making sure input is not an empty string
            if response == "":
                print("Please enter an answer")

            # making sure the input is not a number
            elif response.isdigit():
                print("Please enter a word, not a number")

            else:
                break

        # checking if their answer is correct
        if response == english:
            print("Correct :)\n")
            score += 1

        # if their answer is wrong
        else:
            print("\nWrong :( The correct answer is {}".format(english))

    # congratulate at the end of the lesson
    print("✰Well Done✰\n")
    return score


def quiz_learned(dictionary, phrase_dictionary, learned_words, count):
    """quizzes users on words they have preiviously learnt, returns score"""
    
    score = 0

    # making a copy of the list so items can be removed without changing it
    words = learned_words.copy()

    for index in range(count):

        # choosing a random word
        word = random.choice(words)
        words.remove(word)

        # defining its translation depending on whether it is a word or a phrase
        if word in dictionary:
            english = dictionary [word]["trans"].lower()

        elif word in phrase_dictionary:
            english = phrase_dictionary [word]["trans"].lower()

        # asking the user their answer
        while True:
            response = input(
            f"\nWhat is the translation of {word}? ").strip().lower()

            #making sure input is not an empty string
            if response == "":
                print("Please enter an answer")

            #making sure input is not a number
            elif response.isdigit():
                print("Please enter a word, not a number")

            else:
                break


        # checking the answer
        if response == english:
            print(" Correct :)\n ")
            score += 1
        else:
            print("Wrong :( The correct answer is {}".format(english))
    
    # congratulate at the end of the lesson
    print("✰Well Done✰")
    return score


def difficulty(level, learned_words):
    """allows the user to set their difficulty, runs functions accordingly"""

    #if beginner chosen
    if level == "1":
        learn_beginner(dictionary, learned_words, count)

    # if intermediate chosen
    elif level == "2":
        learn_intermediate(phrase_dictionary, learned_words, count)


# MAIN ROUTINE
if __name__ == "__main__":

    # defining dictionaries/lists used globally
    dictionary = {
        "Hei": {"trans": "Hello", "pron": "hey"},
        "Ha det": {"trans": "Goodbye", "pron": "hah-deh"},
        "God morgen": {"trans": "Good morning", "pron": "goo mor-gen"},
        "God dag": {"trans": "Good day", "pron": "goo dahg"},
        "God kveld": {"trans": "Good evening", "pron": "goo kvel"},
        "Takk": {"trans": "Thank you", "pron": "tahk"},
        "Beklager": {"trans": "I'm sorry", "pron": "beh-klah-ger"},
        "Vær så snill": {"trans": "Please", "pron": "vair soh snill"},
        "Unnskyld": {"trans": "Excuse me", "pron": "oon-shill"},
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
        "År": {"trans": "Year", "pron": "ohr"},
        "Måned ": {"trans": "Month", "pron": "moh-ned"},
        "Kone": {"trans": "Wife", "pron": "koo-neh"},
        "Mann": {"trans": "Husband", "pron": "mahn"},
        "Tog": {"trans": "Train", "pron": "toog"},
        "Buss": {"trans": "Bus", "pron": "booss"}
    }

    phrase_dictionary = {
        "Hvordan går det?": {"trans": "'How are you?'", "pron": "vor-dan gor deh"},
        "Det går bra.": {"trans": "'I'm doing well.'", "pron": "deh gor brah"},
        "Hva heter du?": {"trans": "'What is your name?'", "pron": "vah hay-ter doo"},
        "Jeg heter...": {"trans": "'My name is...'", "pron": "yai hay-ter"},
        "Hyggelig å møte deg.": {"trans": "'Nice to meet you'", "pron": "hig-eh-lee oh muh-teh die"},
        "Hvor kommer du fra?": {"trans": "'Where are you from?'", "pron": "vor kom-er doo frah"},
        "Jeg kommer fra New Zealand.": {"trans": "'I come from New Zealand'", "pron": "yai kom-er frah noo zee-lahnd"},
        "Hvor bor du?": {"trans": "Where do you live?", "pron": "vor boor doo"},
        "Jeg bor i Wellington.": {"trans": "'I live in Wellington'", "pron": "yai boor ee wel-ling-ton"},
        "Kan du hjelpe meg?": {"trans": "'Can you help me?'", "pron": "kahn doo yelp-eh my"},
        "Jeg forstår ikke.": {"trans": "'I don't understand'", "pron": "yai for-stor ik-eh"},
        "Kan du gjenta det?": {"trans": "'Can you repeat that?'", "pron": "kahn doo yen-tah deh"},
        "Kan du snakke saktere?": {"trans": "'Can you speak more slowly?'", "pron": "kahn doo snak-eh sahk-ter-eh"},
        "Snakker du engelsk?": {"trans": "''Do you speak English?''", "pron": "snak-er doo eng-elsk"},
        "Jeg snakker litt norsk.": {"trans": "'I speak a little Norwegian'", "pron": "yai snak-er lit norshk"},
        "Jeg lærer norsk.": {"trans": "'I am learning Norwegian'", "pron": "yai lair-er norshk"},
        "Hva gjør du?": {"trans": "'What are you doing?'", "pron": "vah yur doo"},
        "Jeg vet ikke.": {"trans": "'I don't know'", "pron": "yai vayt ik-eh"},
        "Jeg er sulten.": {"trans": "'I am hungry'", "pron": "yai air sool-ten"},
        "Jeg er tørst.": {"trans": "'I am thirsty'", "pron": "yai air turst"},
        "Jeg vil ha vann.": {"trans": "'I want water'", "pron": "yai vil hah vahn"},
        "Jeg vil ha kaffe.": {"trans": "'I want coffee'", "pron": "yai vil hah kah-feh"},
        "Hvor er toalettet?": {"trans": "'Where is the bathroom?'", "pron": "vor air too-ah-let-eh"},
        "Hva er klokken?": {"trans": "'What time is it?'", "pron": "vah air klok-en"},
        "Jeg er klar.": {"trans": "'I am ready'", "pron": "yai air klar"},
        "Jeg er sliten.": {"trans": "'I am tired'", "pron": "yai air slee-ten"},
        "Jeg liker dette.": {"trans": "'I like this'", "pron": "yai lee-ker det-eh"},
        "Jeg elsker Norge.": {"trans": "'I love Norway'", "pron": "yai el-sker nor-geh"},
        "Ha en fin dag!": {"trans": "'Have a nice day!'", "pron": "hah en feen dahg"},
        "Vi sees senere.": {"trans": "'See you later'", "pron": "vee says seh-neh-reh"}
    }

    learned_words = []

    # disclaimer
    print("\n ---- Pronounication Disclaimer ---- \n")
    print("The pronounciations provided are approximate guides.")
    print("Norwegian pronounciations can vary depending on dialect.\n")

    # looping until the user chooses to exit the program
    while True:

        # main menu
        print("1. learn")
        print("2. quiz")
        print("3. exit")

        # asking the user what they want to do
        choice = input("\nNumber choice:")

        if choice == "1":

            # printing learning levels
            print("\n1. Beginner")
            print("2. Intermediate")

            # asking the user what level they want to learn at
            while True:
                level = input("\nWhat difficulty level do you want to learn at?")

                # making sure a valid option is chosen
                if level == "1" or level == "2":
                    break

                else:
                    print("Please enter a valid option")

            # asking the user how many words they want to learn
            while True:
                try:
                    count = int(input("\nEnter how many words you want to learn:"))

                    # making sure count fits within the range
                    if count < 1 or count > 30:
                        print("Please enter a number between 1 and 30")

                    else:
                        break

                # making sure input is a valid number        
                except ValueError:
                    print("Please enter a valid number")
                
            # running a function depending on the difficulty the user chose
            difficulty(level, learned_words)

        elif choice == "2":
            print("\n1. Quiz on random words")
            print("2. Quiz on previously learned words" + "\n")

            #asking user what they want to do
            while True:
                quiz_choice = input("Selected number:")

                # making sure they pick one of the valid options
                if quiz_choice == "1" or quiz_choice == "2":
                    break

                else:
                    print("Please enter a valid option")

            if quiz_choice == "1":

               # asking the user how many words they want to be quizzed on
                while True:
                    try:
                        count = int(input("\nEnter how many words you want to learn:"))

                        # making sure count falls within the valid range
                        if count < 1 or count > 30:
                            print("Please enter a number between 1 and 30")

                        else:
                            break
                        
                    # making sure input is a valid number
                    except ValueError:
                        print("Please enter a valid number")

                # running the quiz function
                score = quiz(dictionary, count)
                print(f" You got {score}/{count} questions right")

            elif quiz_choice == "2":

                #defining maximum possible words/phrases that can be learnt
                limit = len(learned_words)

                # if user has not learnt any words yet
                if limit == 0:
                    print("Learn some words in order to use this feature :)\n")

                # asking user for input
                else:
                    while True:
                        try:
                            count = int(input("Enter how many questions you want to do:"))

                            # making sure input is within range
                            if count < 1 or count > limit:
                                print("Please enter a valid number")

                            else:
                                break

                        # making sure input is a valid number
                        except ValueError:
                            print("Please enter a number.")

                    #printing score for user to see
                    score = quiz_learned(dictionary, phrase_dictionary, learned_words, count)
                    print(f"You got {score}/{count} questions right")
            

        elif choice == "3":

            # exiting the program
            print("\nGoodbye! Ha det Bra!")
            break
        
        # making sure the user picks a valid option from main menu
        else:
            print("Please enter a valid option")
