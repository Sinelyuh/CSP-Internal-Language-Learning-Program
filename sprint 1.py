import random

def learn(dictionary, count):
    """displays a series of flashcards to teach Norwegian words."""
    #Extracts all Norwegian vocabulary words into a list
    words = list(dictionary.keys())

    #Loops through the number of words requested by the user
    for index in range(count):
        #Randomly chooses one Norwegian word from the remaining word pool
        word = random.choice(words)

        #Prevents duplicate selections
        words.remove(word)

        #Retrieves and lowercases the english translation and pronounciation
        english = dictionary[word]["trans"].lower()
        pronunciation = dictionary[word]["pron"].lower()
        
        #Prints the formatted flashcards 
        print(f"\n--- Flashcard {index + 1}/{count} ---")
        print(f"The Norwegian word for {english} is {word}")
        print(f"How to say it: [{pronunciation}]")
        print("-" * 25)

        #Pauses the loop to let the user study before continuing
        try:
            input("Press Enter for the next word...")
        except Exception:  #Catches anomalies 
            print("Something went wrong. Please try again.")

    print("\n✰ Study Session Complete! ✰\n")

def question(dictionary, count):
    """runs an interactive translation quiz for the user."""
    #Extracts all Norwegian vocabulary words into a list
    words = list(dictionary.keys())

    #Randomly selects a fixed subset of unique words
    quiz_words = random.sample(words, count)

    #Loops through each selected word 
    for word in quiz_words:
        #Retrieves the correct english answer and pronunciation
        english = dictionary[word]["trans"].lower()
        pronunciation = dictionary[word]["pron"].lower()
        
        #Prompts the user for their translation answer
        response = input(f"What is the translation of '{word}'? ").strip().lower()
        
        #Checks if the user's answer matches the translation
        if response == english:
            print("Correct :)")
        else:
            print(f"WRONG :( The correct answer is '{dictionary[word]['trans']}'.")
            
        #Displays the pronunciation
        print(f"Pronunciation: [{pronunciation}]\n")


if __name__ == "__main__":
    #Dictionary of norwegian words
    dictionary = {
        "Hei": {"trans": "Hello", "pron": "hey"},
        "Ha det": {"trans": "Goodbye (less formal)", "pron": "hah-deh"},
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
        "Måned": {"trans": "Month", "pron": "moh-ned"},
        "Kone": {"trans": "Wife", "pron": "koo-neh"},
        "Mann": {"trans": "Husband", "pron": "mahn"},
        "Tog": {"trans": "Train", "pron": "toog"},
        "Buss": {"trans": "Bus", "pron": "booss"},
    }

    #Counts the maximum available items in the dictionary
    max_words = len(dictionary)

    #Menu system
    while True:
        #Displays navigation options
        print("\n--- Norwegian Learning App ---")
        print("1. Learn")
        print("2. Quiz")
        print("0. Exit")
        choice = input("What do you want to do? ").strip()

        #Learning mode
        if choice == "1":
            try:
                
                count = int(input("Enter how many words do you want to learn: "))
                #Enforces minimum lower boundary
                if count <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                
                #Enforces upper boundary based on dictionary length
                if count > max_words:
                    print(f"Error: You cannot request more than {max_words} words. Please try again.")
                    continue
                
                #Triggers the learn function
                learn(dictionary, count)
            except ValueError:
                #Catches non-integer text
                print("Invalid input. Please enter a valid number.")
                
        #User chooses Quiz Mode
        elif choice == "2":
            try:
                count = int(input("Enter how many questions you want to do: "))
                #Enforces minimum lower boundary
                if count <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                
                #Enforces upper boundary based on dictionary length
                if count > max_words:
                    print(f"Error: You cannot request more than {max_words} questions. Please try again.")
                    continue
                
                #Triggers the quiz function
                question(dictionary, count)
            except ValueError:
                #Catches non-integer text entries 
                print("Invalid input. Please enter a valid number.")
                
        #Exits if the user chooses to
        elif choice == "0":
            print("Goodbye! Ha det bra!")
            break 
            
        #Fallback catch for invalid menu choices
        else:
            print("Invalid choice. Please select 1 or 2 or 0.")
