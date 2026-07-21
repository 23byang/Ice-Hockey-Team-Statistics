"""This code is a user interface where fans and atheletes can track the rankings of teams in a league, as well as view match scores."""
game_database = [
    {"Game Date dd/mm/yy": "22/02/24", "Team 1 (Home)": "Carolina Hurricanes", "Team 2 (Away)": "Florida Panthers", "Team 1 Score": 1, "Team 2 Score": 0, "OT/SO?": False},
    {"Game Date dd/mm/yy": "25/02/24", "Team 1 (Home)": "Buffalo Sabres", "Team 2 (Away)": "Carolina Hurricanes", "Team 1 Score": 3, "Team 2 Score": 2, "OT/SO?": True},
    {"Game Date dd/mm/yy": "19/02/24", "Team 1 (Home)": "Minnesota Wild", "Team 2 (Away)": "Vancouver Canucks", "Team 1 Score": 10, "Team 2 Score": 7, "OT/SO?": False},
    {"Game Date dd/mm/yy": "19/02/24", "Team 1 (Home)": "Seattle Kraken", "Team 2 (Away)": "Detroit Red Wings", "Team 1 Score": 3, "Team 2 Score": 4, "OT/SO?": True},
    {"Game Date dd/mm/yy": "04/04/24", "Team 1 (Home)": "Carolina Hurricanes", "Team 2 (Away)": "Boston Bruins", "Team 1 Score": 1, "Team 2 Score": 4, "OT/SO?": False},
    {"Game Date dd/mm/yy": "14/10/24", "Team 1 (Home)": "Boston Bruins", "Team 2 (Away)": "Florida Panthers", "Team 1 Score": 3, "Team 2 Score": 4, "OT/SO?": False},
    {"Game Date dd/mm/yy": "14/10/24", "Team 1 (Home)": "Ottawa Senators", "Team 2 (Away)": "Los Angeles Kings", "Team 1 Score": 8, "Team 2 Score": 7, "OT/SO?": True},
    {"Game Date dd/mm/yy": "15/10/24", "Team 1 (Home)": "Dallas Stars", "Team 2 (Away)": "San Jose Sharks", "Team 1 Score": 3, "Team 2 Score": 2, "OT/SO?": True},
    {"Game Date dd/mm/yy": "15/10/24", "Team 1 (Home)": "Edmonton Oilers", "Team 2 (Away)": "Philadelphia Flyers", "Team 1 Score": 4, "Team 2 Score": 3, "OT/SO?": True},
    {"Game Date dd/mm/yy": "07/04/26", "Team 1 (Home)": "Boston Bruins", "Team 2 (Away)": "Carolina Hurricanes", "Team 1 Score": 5, "Team 2 Score": 6, "OT/SO?": True}
    ]
"""These are dictionaries in lists for my database storage. They include keys and values for two teams, as well as their score, and the date of the game as well as if the match went into extra time."""


def clean_text(database, tally):
    """This function cleans the text, removing all the syntax as to produce a user friendly product."""
    print(f"\n\nGame #{tally} - Game Details:")
    for key, value in database.items():
        print(f"{key}: {value}", end=", ")


def match_history(database):
    """This function allows users to look at the entire database's match history."""
    tally = 1
    for game in database:
        clean_text(game, tally)
        tally += 1


def points_extractor(team):
    """This function facilitates the sort function by extracting the points from each team so that the program can sort the teams in the database."""
    return team[1]


def view_rank(database):
    """This function allows users to observe the rankings of all the teams in the league by points."""
    team_points = {}
    for game in database:
        team_points[game["Team 1 (Home)"]] = 0
        team_points[game["Team 2 (Away)"]] = 0
    for game in database:

        score_1 = game["Team 1 Score"]
        score_2 = game["Team 2 Score"]
        ot_or_so = game["OT/SO?"]
        if score_1 > score_2:
            if ot_or_so:
                team_points[game["Team 1 (Home)"]] += 2
                team_points[game["Team 2 (Away)"]] += 1
            else:
                team_points[game["Team 1 (Home)"]] += 3
                team_points[game["Team 2 (Away)"]] += 0
        if score_2 > score_1:
            if ot_or_so:
                team_points[game["Team 2 (Away)"]] += 2
                team_points[game["Team 1 (Home)"]] += 1
            else:
                team_points[game["Team 2 (Away)"]] += 3
                team_points[game["Team 1 (Home)"]] += 0
    temp_list = list(team_points.items())
    temp_list.sort(key=points_extractor, reverse=True)
    print(f"\n{'Rank'} | {'Team'} | {'Points'}")
    print("-" * 40)
    rank = 1
    for item in temp_list:
        team_name = item[0]
        points_value = item[1]
        print(f"{rank} | {team_name} | {points_value}")
        rank += 1


def team_matches(database):
    """This function allows users to track the games of specific teams."""
    found = False
    team = input("What is the name of the team you would like to see? ").strip().lower()
    tally = 1
    for teams in database:
        if team == teams["Team 1 (Home)"].strip().lower():
            clean_text(teams, tally)
            tally += 1
            found = True

        elif team == teams["Team 2 (Away)"].strip().lower():
            clean_text(teams, tally)
            tally += 1
            found = True
    if not found:
        print("Sorry, the team cannot be found in the database.")


def add_match(database):
    """This allows the user to add matches to the game database."""
    extra_time_value = True
    while True:
        date = input("Enter Date of Game (dd/mm/yy): ")
        if date == "":
            print("Invalid Option, please input the date in the form of dd/mm/yy")
        else:
            break
    while True:
        home_team = input("Enter Name of Home Team: ")
        if home_team == "":
            print("Invalid Option, please input the name of the home team")
        else:
            break
    while True:
        away_team = input("Enter Name of Away Team: ")
        if away_team == "":
            print("Invalid Option, please input the name of the away team")
        else:
            break
    try:
        while True:
            home_score = int(input("Enter the Score of the Home Team: "))
            away_score = int(input("Enter the score of the Away Team: "))
            if home_score == away_score:
                print("Invalid Option, both scores cannot be equal.")
            else:
                break
    except ValueError:
        print("Invalid Input, Match Not Added.")
        return
    while True:
        extra_time = input("Did the game require extra time e.g OT or SO (Yes/No) ").lower()
        if extra_time == "yes":
            extra_time_value = True
            break
        elif extra_time == "no":
            extra_time_value = False
            break
        else:
            print("Invalid Option")
    new_game = {"Game Date dd/mm/yy": date, "Team 1 (Home)": home_team, "Team 2 (Away)": away_team, "Team 1 Score": home_score, "Team 2 Score": away_score, "OT/SO?": extra_time_value}
    database.append(new_game)
    print("Match has been added to the database.")


def remove_match(database):
    """This function allows the user to remove a match from the database."""
    tally = 1
    match_history(database)
    for game in database:
        tally += 1
    if database == []:
        print("Match Database is empty, returning to main menu.")
    else:
        try:
            choice = int(input("\nWhich match would you like to remove 1,2,3... etc. "))
            if choice not in range(1, tally):
                print("Invalid Option, please input a positive integer within the options corresponding to your desired choice.")
            else:
                database.pop(choice - 1)
                print("Item removed successfully.")
        except ValueError:
            print("Invalid Option, please input a positive integer corresponding to your desired choice.")


def menu_display():
    """This function codes for the visual part of the main menu, displaying all the choices available to the user."""
    print("\n----------------------------------------------------------")
    print("\nWelcome To The Ice Hockey Database!")
    print("1. View Ranks Of Teams")
    print("2. Add A Match ")
    print("3. Remove A Match ")
    print("4. View Match History ")
    print("5. Exit Program ")
    print("6. View Team Match History ")


def menu_function():
    """This function acts as the brains behind the menu, recieving an input then using it to decide what function to run according to the user's choice."""
    while True:
        menu_display()
        while True:
            try:
                choice = int(input("What would you like to do? (1-6) "))

                if choice == 6:
                    team_matches(game_database)
                elif choice == 5:
                    print("Exiting Program.")
                    exit()
                elif choice == 4:
                    match_history(game_database)
                elif choice == 3:
                    remove_match(game_database)
                elif choice == 2:
                    add_match(game_database)
                elif choice == 1:
                    view_rank(game_database)
                else:
                    print("Invalid Choice.")
                    continue
                break
            except ValueError:
                print("Invalid choice, please input the corresponding number to you choice from 1-6. Ensure that it does not have syntax(symbols) and is typed as a number.")
                continue


menu_function()
"""This calls menu_function, kickstarting the entire program."""
