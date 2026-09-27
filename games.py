def add_game(games):

    print("\n ----add a game of your choice----")

    name = (input("enter the name of your game: "))
    #name of the game like BGMI, FREE FIRE, VALVORANT , APEX LEGEND , CLASH OF CLANS
    game_type = input("enter your game_type: ")
     #Genre of your play like survival, battle royal, strateggy , creativity
    mode = input("enter the modes of playing: ")
     #eg- PC, Console, Mobile, Laptop
    hours = int(input("Enter hours played: "))
    #how many hours u hav played the game

    while hours < 0:
    #since hours cannot be less than zero
        print("hours cannot be negative")
        hours = int(input("enter the hours played"))
    completion = int(input("Enter completion percentage: "))
    #enter the amount of game u have completed

    while completion <0 or completion>100:
        print("completion cant be more than 100")
        completion = int(input("Enter completion percentage: "))
        
    rating = int(input("Enter your rating out of 10: "))#The rating you would like to give to your game

    while rating < 0 or rating > 10:
        print("Rating must be between 0 and 10.")#we cannot allow the rating to go more than 105
        rating = int(input("Enter your rating out of 10: "))

    if completion == 0:
        status = "Not Started"

    elif completion == 100:
         status = "Completed"

    else:
        status = "In Progress"
    print(status)


    game = {
        "name": name,
        "game_type": game_type,
        "mode": mode,
        "hours": hours,
        "completion": completion,
        "status": status,
        "rating": rating
    }

    games.append(game)#this allows us to add the data to store into our dictionary
    print("Game added successfully!")

def view_games(games):

    print("\n--- All Games ---")

    for game in games:
        print("Name:", game["name"])
        print("Game Type:", game["game_type"])
        print("mode:", game["mode"])
        print("Hours Played:", game["hours"])
        print("Completion:", game["completion"], "%")
        print("Status:", game["status"])
        print("Rating:", game["rating"])
        print("--------------------")

def search_game(games   ):
    print("\n--- Search Game ---")

    search_name = input("Enter game name to search: ")

    found = False

    for game in games:
        if game["name"] == search_name:
            print("Game found!")
            print("Name:", game["name"])
            print("Game Type:", game["game_type"])
            print("Mode:", game["mode"])
            print("Hours Played:", game["hours"])
            print("Completion:", game["completion"], "%")
            print("Status:", game["status"])
            print("Rating:", game["rating"])

            found = True

    if found == False:
        print("Game not found.")