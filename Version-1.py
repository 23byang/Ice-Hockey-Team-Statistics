"""This code is a user interface where fans and atheletes can track the rankings of teams in a league, as well as view match scores."""
game_database = [{"Game Date dd/mm/yy" : "22/02/24", "Team 1 (Home)" : "Carolina Hurricanes", "Team 2 (Away)" : "Florida Panthers", "Team 1 Score" : 1, "Team 2 Score" : 0, "OT/SO?": False},
    {"Game Date dd/mm/yy" : "25/02/24", "Team 1 (Home)" : "Buffalo Sabres", "Team 2 (Away)" : "Carolina Hurricanes", "Team 1 Score" : 3, "Team 2 Score" : 2, "OT/SO?": True},
    {"Game Date dd/mm/yy" : "19/02/24", "Team 1 (Home)" : "Minnesota Wild", "Team 2 (Away)" : "Vancouver Canucks", "Team 1 Score" : 10, "Team 2 Score" : 7, "OT/SO?": False},
    {"Game Date dd/mm/yy" : "19/02/24", "Team 1 (Home)" : "Seattle Kraken", "Team 2 (Away)" : "Detroit Red Wings", "Team 1 Score" : 3, "Team 2 Score" : 4, "OT/SO?": True},
    {"Game Date dd/mm/yy" : "04/04/24", "Team 1 (Home)" : "Carolina Hurricanes", "Team 2 (Away)" : "Boston Bruins", "Team 1 Score" : 1, "Team 2 Score" : 4, "OT/SO?": False},
    {"Game Date dd/mm/yy" : "14/10/24", "Team 1 (Home)" : "Boston Bruins", "Team 2 (Away)" : "Florida Panthers", "Team 1 Score" : 3, "Team 2 Score" : 4, "OT/SO?": False},
    {"Game Date dd/mm/yy" : "14/10/24", "Team 1 (Home)" : "Ottawa Senators", "Team 2 (Away)" : "Los Angeles Kings", "Team 1 Score" : 8, "Team 2 Score" : 7, "OT/SO?": True},
    {"Game Date dd/mm/yy" : "15/10/24", "Team 1 (Home)" : "Dallas Stars", "Team 2 (Away)" : "San Jose Sharks", "Team 1 Score" : 3, "Team 2 Score" : 2, "OT/SO?": True},
    {"Game Date dd/mm/yy" : "15/10/24", "Team 1 (Home)" : "Edmonton Oilers", "Team 2 (Away)" : "Philadelphia Flyers", "Team 1 Score" : 4, "Team 2 Score" : 3, "OT/SO?": True},
    {"Game Date dd/mm/yy" : "07/04/26", "Team 1 (Home)" : "Boston Bruins", "Team 2 (Away)" : "Carolina Hurricanes", "Team 1 Score" : 5, "Team 2 Score" : 6, "OT/SO?": True}]

def clean_text(text):
    clean_text = str(text).replace('""', "") # Check with Mr Harding
    return clean_text
def match_history(database):
    tally = 1
    for game in database:
        print(f"{tally}. {clean_text(game)}")#when building game id counter talk about utility for remove function
        tally += 1
        
def team_statistics(database):
    found = False
    team = input("What is the name of the team you would like to see? ").strip().lower()
    for teams in database:
        if team == teams["Team 1 (Home)"].strip().lower():
            print(clean_text(teams))
            found = True
        elif team == teams["Team 2 (Away)"].strip().lower():
            print(clean_text(teams))
            found = True
    if not found:
        print("Sorry, the team cannot be found in the database.")

def add_match(database):
    date = input("Enter Date of Game (dd/mm/yy): ")
    home_team = input("Enter Name of Home Team: ")
    away_team = input("Enter Name of Away Team: ")
    extra_time_value = True
    try:
        home_score = int(input("Enter the Score of the Home Team: "))
        away_score = int(input("Enter the score of the Away Team: "))
    except ValueError:
        print("Invalid Input, Match Not Added.")
        return
    while True:
        extra_time = input("Did the game require extra time e.g OT or SO (Yes/No)").lower()
        if extra_time == "yes":
            extra_time_value == True
            break
        elif extra_time == "no":
            extra_time_value == False
            break
        else: 
            print("Invalid Option") 
    new_game = {"Game Date dd/mm/yy" : date, "Team 1 (Home)" : home_team, "Team 2 (Away)" : away_team, "Team 1 Score" : home_score, "Team 2 Score" : away_score, "OT/SO?": extra_time_value}
    database.append(new_game)
    print("Match has been added to the database.")

def remove_match(database):
    tally = 0
    match_history(database)
    if database == []:
        print("Match Database is empty, returning to main menu.")
    else:
        try: 
            choice = int(input("Which match would you like to remove 1,2,3... etc."))
            if choice not in range(1, tally + 1):
                print("Invalid Option, please input a positive integer corresponding to your desired choice.")
            else:
                database.pop(choice - 1)
                print("Item removed successfully.")
        except ValueError:
            print("Invalid Option, please input a positive integer corresponding to your desired choice.")



def menu_display():
    print("Welcome To The Ice Hockey Database!")
    print("1. View Ranks Of Teams") # ranks based off of Win = 3 pt, Loss = 0 pt, OTW = 2 pt, OTL = 1 pt
    print("2. Add A Match ")
    print("3. Remove A Match ")
    print("4. View Match History ")
    print("5. Exit Program ")
    print("6. View Team Statistics ")


def menu_function():
    while True:
        menu_display()
        while True:
            try:
                choice = float(input("What would you like to do? (1-6)"))
                choice = int(choice)  # Check with Mr Harding
                if choice == 6:
                    team_statistics(game_database)
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
                print("Invalid choice, please input the corresponding number to you choice from 1-6.")
                continue
menu_function()