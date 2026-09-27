def view_statistics(games):
    print("\n--- Game Statistics ---")

    count = 0

    for game in games:
        count = count + 1

    print("Total games:", count)
    total_hours = 0

    for game in games:
        total_hours = total_hours + game["hours"]

    print("Total hours played:", total_hours)
    highest_rating = 0
    highest_game = ""

    for game in games:
        if game["rating"] > highest_rating:
            highest_rating = game["rating"]
            highest_game = game["name"]

    print("Highest rated game:", highest_game)
    print("Highest rating:", highest_rating)
    completed = 0
    in_progress = 0
    not_started = 0

    for game in games:
        if game["status"] == "Completed":
            completed = completed + 1
        elif game["status"] == "In Progress":
            in_progress = in_progress + 1
        elif game["status"] == "Not Started":
            not_started = not_started + 1

    print("Completed games:", completed)
    print("Games in progress:", in_progress)
    print("Not started games:", not_started)
    total_rating = 0

    for game in games:
        total_rating = total_rating + game["rating"]

    if count > 0:
        average_rating = total_rating / count
        print("Average rating:", average_rating)
    else:
        print("Average rating: no games found")

    unique_games = []
    for game in games:
            if game["name"] not in unique_games:
                unique_games.append(game["name"])
    
    print("Unique games:", len(unique_games))
    
    highest_hours = 0
    highest_hours_game = ""
    
    for game in games:
        if game["hours"] > highest_hours:
            highest_hours = game["hours"]
            highest_hours_game = game["name"]
    
        print("Most played game:", highest_hours_game)
        print("Most played hours:", highest_hours)
        lowest_rating = 10
        lowest_game = ""
    
        for game in games:
            if game["rating"] < lowest_rating:
                lowest_rating = game["rating"]
                lowest_game = game["name"]
        print("Lowest rated game:", lowest_game)
        print("Lowest rating:", lowest_rating)
        completed_percentage = 0
    
        for game in games:
            if game["completion"] == 100:
                completed_percentage = completed_percentage + 1
    
        print("Games with 100% completion:", completed_percentage)