
print("========================================")
print("========================================")
print("========================================")
print("         Game Progress Tracker          ")
print("========================================")
print("========================================")
print("========================================")

from games import add_game, view_games, search_game
from progress import update_progress
from analytics import view_statistics
from reports import game_report , overall_report
games = []

while True:
    print("\n===== GAME PROGRESS TRACKER =====")
    print("1. Add Game")
    print("2. View Games")
    print("3. Search Game")
    print("4. Update progress")
    print("5. View Statistics")
    print("6. Game Report")
    print("7. Overall Report")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_game(games)
    elif choice == "2":
        view_games(games)
    elif choice == "3":
        search_game(games)
    elif choice == "4":
        update_progress(games)
    elif choice == "5":
        view_statistics(games)
    elif choice == "6":
        game_report(games)
    elif choice == "7":
        overall_report(games)
    elif choice == "8":
        print("Thank you for using my progress tracker")
        break
    else:
        print("Invalid choice. Please try again.")

    