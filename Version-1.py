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
    for game in database:
        print(clean_text(game))#when building game id counter talk about utility for remove function
        
def team_statistics(database):
    found = False
    team = input("What is the name of the team you would like to see? ")
    for teams in database:
        if team == teams["Team 1 (Home)"]:
            print(clean_text(teams))
            found = True
            break
        elif team == teams["Team 2 (Away)"]:
            print(clean_text(teams))
            found = True
            break #talk about how breaks so that does not print all games.
    if not found:
        print("Sorry, the team cannot be found in the database.")

    

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