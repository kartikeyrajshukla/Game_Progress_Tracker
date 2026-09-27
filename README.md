# Game Progress Tracker

## Overview

The Game Progress Tracker is a basic Python command-line application developed to manage and track game progress.

The application allows users to add games, view and search games, update their progress, calculate statistics, and generate individual and overall reports.

This project applies concepts from CSE1021 Introduction to Problem Solving and Programming, including variables, data types, conditional statements, loops, functions, lists, dictionaries, and basic algorithms.

## Features

* Add a new game
* View all stored games
* Search for a game
* Update game progress
* Calculate game statistics
* Generate an individual game report
* Generate an overall game report
* Validate hours, completion percentage, and rating

## Technologies Used

* Python
* Lists and dictionaries
* Functions
* Conditional statements
* Loops
* Command-line interface

No external libraries or database are used.

## How to Run

1. Make sure Python is installed on your system.

2. Open the project folder in VS Code.

3. Open the terminal in VS Code.

4. Run the following command:

   `py main.py`

5. Use the menu displayed in the terminal to select an operation.

## Project Structure

```text
Game-Progress-Tracker/
├── main.py
├── games.py
├── progress.py
├── analytics.py
├── reports.py
├── statement.md
├── README.md
└── text_tracker/
    └── test.py
```

## Module Description

* `main.py` – Controls the main menu and connects the modules.
* `games.py` – Handles adding, viewing, and searching games.
* `progress.py` – Handles updating game progress.
* `analytics.py` – Calculates game statistics.
* `reports.py` – Generates individual and overall reports.
* `statement.md` – Contains the project statement, scope, target users, and features.
* `text_tracker/test.py` – Contains basic tests for adding, searching, and updating a game.

## Testing

Basic testing was performed to verify the main operations of the application.

The tests checked whether a game could be added, searched, and updated successfully. All three test cases passed.

## Data Storage

Game information is stored temporarily in an in-memory Python list containing dictionaries. The data is not permanently stored after the program is closed.

## Future Enhancements

Possible future enhancements include permanent data storage, additional statistics and filtering options, sorting games, and tracking progress over time.
