def update_progress(games):
    print("\n--- Update Game Progress ---")

    search_name = input("Enter game name to update: ")

    for game in games:
        if game["name"] == search_name:
            print("Game found!")

            new_hours = int(input("Enter new hours played: "))
            new_completion = int(input("Enter new completion percentage: "))
            game["hours"] = new_hours
            game["completion"] = new_completion
            if new_completion == 0:
                game["status"] = "Not Started"
            elif new_completion == 100:
                game["status"] = "Completed"
            else:
                game["status"] = "In Progress"
            print("Progress updated successfully!")