games = []

# Test 1: Add a game
game = {
    "name": "Minecraft",
    "game_type": "Sandbox",
    "mode": "Single Player",
    "hours": 10,
    "completion": 50,
    "status": "In Progress",
    "rating": 9
}

games.append(game)

if len(games) == 1:
    print("Test 1 passed: Game was added successfully.")


# Test 2: Search for a game
search_name = "Minecraft"
found = False

for game in games:
    if game["name"] == search_name:
        found = True

if found:
    print("Test 2 passed: Game was found successfully.")


# Test 3: Update game progress
games[0]["hours"] = 20
games[0]["completion"] = 80
games[0]["status"] = "In Progress"

if games[0]["hours"] == 20 and games[0]["completion"] == 80:
    print("Test 3 passed: Game progress updated successfully.")
