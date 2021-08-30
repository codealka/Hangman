import random
LIVES = 6
# the following is a list of countries, fruits and superheros which the game will index randomly
# 0th item = country , 1st item = fruits , 2nd = Superheros
Hangman = [["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland",
            "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Luxembourg", "Lithuania", "Malta",
            "Netherlands", "Poland", "Portugal", "Romania", "Slovak Republic", "Slovenia", "Spain", "Sweden", "United Kingdom"],
           ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'],
           ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']]
def Main():

    
    print("Welcome to Hangman !")
    print("")

    category = random.randint(1, 3)

    if category == 1:
            print("Guess the EU Country !")
            length = len(Hangman[0])

    if category == 2:
            print("Guess the Fruit !")
            length = len(Hangman[1])

    if category == 3:
            print("Guess the SuperHero")
            length = len(Hangman[2])



    word = Hangman[category - 1][random.randint(1,length)]


    countryQuestion = word

    # the following will display to the user the amount of letters the country to guess has.
    letter_count = letter_counter(countryQuestion)
    print("Your word has " + str(letter_count) + " letters")
    for i in countryQuestion:
        if i == " ":
            print(i , end="")
        else:
            print("_" , end=" ")
    print('')

    y = LIVES

    # this list will be used to store every correct guess to update the words will all the correct guesses
    lettercombo = []

    check(countryQuestion,lettercombo)


def letter_counter(countryQuestion):
    letter_count = 0
    for i in countryQuestion:
        if i.isalpha():
            letter_count += 1
    return letter_count


def check(countryInquestion, lettercombo):
    x = 0 # used to determine a win
    y = LIVES # used to determine a loss
    s = '' # used to store a successful guess
    letter_count = letter_counter(countryInquestion)
    while ( y > 0):

        if x == letter_count:
            print("YOU WIN!!!")
            break

        while True:
            letterGuessed =input("Enter your guess here: ")
            letterGuessed = letterGuessed.upper() # this will be used to unify the case used in the input
            print('')

            if letterGuessed.isalpha() and len(letterGuessed) == 1: #checks one alphabetical character only
                break
            else:
                print("You must enter an alphabetical character")

        if letterGuessed in countryInquestion.upper():
            for i in countryInquestion.upper():
                if letterGuessed == i:
                    x += 1

        while True:
            if letterGuessed in countryInquestion.upper():
                lettercombo.append(letterGuessed)

                for item in lettercombo:
                    s += item

                for i in countryInquestion.upper(): # goes over every letter and check against guess
                    if i in s:
                        print(i + " ", end='')
                    elif i == " ":
                        print(i + " ", end='')
                    else:
                        print("_ ", end='')
                break

            else:
                print("-1 life, this letter is not in the word")
                y -= 1
                print("You have " + str(y)+ " lives left" )
                break
        print("")

    if y == 0:
        print("The word is " + countryInquestion)

Main()
