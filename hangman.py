import random
LIVES = 6
# the following is a list of countries which the game will index randomly
country_list = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda",
                "Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain",
                "Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia",
                "Bosnia","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso",
                "Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia",
                "Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus",
                "Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador",
                "Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France",
                "French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece",
                "Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras",
                "Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy",
                "Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon",
                "Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi",
                "Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia",
                "Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles",
                "New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine",
                "Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico",
                "Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre and Miquelon","Samoa","San Marino",
                "Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia",
                "Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts","St Lucia","St Vincent",
                "St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan",
                "Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad","Tunisia","Turkey","Turkmenistan",
                "Turks and Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan",
                "Venezuela","Vietnam","Virgin Islands","Yemen","Zambia","Zimbabwe"]

def Main():

    
    print("Welcome to guess the country!")
    print("")
    # 205 items in the list (for indexing reference)
    randomNumber = random.randint(1,205) #this number will be used to randomly pick a country

    countryQuestion = Country_To_Guess(randomNumber) # this stores the country that is chosen for the game

    print(countryQuestion)
    
    letter_counter(countryQuestion)
    
    Display_Dashes(countryQuestion)

    y = LIVES
    lettercombo = [] #this list will be used to store every correct guess to update the words will all the correct guesses


    check(countryQuestion,lettercombo)




def Country_To_Guess(randomNumber):
    country_choice = country_list[randomNumber]
    return country_choice

def letter_counter(countryQuestion):
    letter_count = 0
    for i in countryQuestion:
        if i.isalpha():
            letter_count += 1
    return letter_count


def Display_Dashes(countryQuestion):
    letter_count = letter_counter(countryQuestion)
    print("Your Country has " + str(letter_count) + " letters")
    for i in countryQuestion:
        if i == " ":
            print(i , end="")
        else:
            print("_" , end=" ")
    print('')

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


Main()