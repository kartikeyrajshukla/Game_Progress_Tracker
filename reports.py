def game_report(games):
    print("\n--- Game Report ---")

    search_name = input("Enter game name for report: ")

    found = False

    for game in games:
        if game["name"] == search_name:
            print("\n===== GAME REPORT =====")
            print("name:", game["name"])
            print("Game Type:", game["game_type"])
            print("Mode:", game["mode"])
            print("Hours Played:", game["hours"])
            print("Completion:", game["completion"], "%")
            print("Status:", game["status"])
            print("Rating:", game["rating"], "/ 10")
            print("======================")

            found = True

    if found == False:
        print("Game not found.")
def overall_report(games):
    print("\n--- Overall Game Report ---")

    count = 0
    total_hours = 0
    total_rating = 0

    for game in games:
        count = count + 1
        total_hours = total_hours + game["hours"]
        total_rating = total_rating + game["rating"]

    print("\n===== OVERALL GAME REPORT =====")
    print("Total games:", count)
    print("Total hours played:", total_hours)

    if count > 0:
        average_rating = total_rating / count
        print("Average rating:", average_rating)
    else:
        print("Average rating: No games available")

    print("===============================")