"""This code is a user interface where fans and atheletes can track the rankings of teams in a league, as well as view match scores."""

def menu_display():
    print("Welcome To The Ice Hockey Database!")
    print("1.View Ranks Of Teams")
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
                    team_statistics()
                elif choice == 5:
                    print("Exiting Program.")
                    exit()
                elif choice == 4:
                    match_history()
                elif choice == 3:
                    remove_match()
                elif choice == 2:
                    add_match()
                elif choice == 1:
                    view_rank
                else:
                    print("Invalid Choice.")
                    continue
                break
            except ValueError:
                print("Invalid choice, please input the corresponding number to you choice from 1-6.")
                continue
