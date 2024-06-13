import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('nbastats')

NBAStats = SHEET.worksheet('NBAStats')

all_stats = NBAStats.get_all_values()


def update_NBAStats_sheet(stats):
    number = len(all_stats) + 1
    stats.insert(0 , number) 
                
    NBAStats.append_row(stats)
    print("Player Stats added successfully!")


def start_menu():
    print('Welcome to this NBA Hall Of Fame Statistics, where you can action the following: \n')
    print('1. View a list of 20 Hall Of Fame Players and their career total stats \n')
    print('2. View an invidual players career stats \n')
    print("3. Add a Hall of Famer's stats into the list \n")
    print('4. Exit \n')

    while True:
        user_input = input('Please select a number between 1 - 4\n')
        
        if user_input == '1':
            print("List of 20 Hall Of Fame Players and their career total stats:")
            headers = ["Player ID", "Name", "Induction Year", "Games Played", "Points", "Rebounds", "Assists", "Steals", "Blocks"]
            print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<15} {headers[3]:<15} {headers[4]:<10} {headers[5]:<10} {headers[6]:<10} {headers[7]:<10} {headers[8]:<10}")

            for i in range(2, len(all_stats) + 1):
                row = NBAStats.row_values(i)
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<10} {row[5]:<10} {row[6]:<10} {row[7]:<10} {row[8]:<10}")
        elif user_input == '2':
            name = input("Enter the player's name: ").strip()
            player_found = False
            for i in range(2, len(all_stats) + 1):  
                row = NBAStats.row_values(i)
                if row[1].strip().lower() == name.lower(): 
                    player_found = True
                    print(f"\n{name}'s career stats:")
                    headers = ["Player ID", "Name", "Induction Year", "Games Played", "Points", "Rebounds", "Assists", "Steals", "Blocks"]
                    print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<15} {headers[3]:<15} {headers[4]:<10} {headers[5]:<10} {headers[6]:<10} {headers[7]:<10} {headers[8]:<10}")
                    print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<10} {row[5]:<10} {row[6]:<10} {row[7]:<10} {row[8]:<10}")
                    break
            if not player_found:
                print("Player not found.")
        elif user_input == '3':
            new_row = get_player_stats()

            update_NBAStats_sheet(new_row)
        elif user_input == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


def get_validated_input(prompt, input_type=int, validation=lambda x: x >= 0, error_message="Invalid input. Please try again."):
    while True:
        try:
            value = input_type(input(prompt).strip())
            if validation(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)

def get_player_stats():
    while True:
        player_name = input("Enter the player's name: ").strip()
        if player_name:
            break
        else:
            print("Player's name cannot be empty. Please enter a valid name.")
    
    induct_year = get_validated_input(
        "Enter the player's induction year: ",
        int,
        lambda x: 1900 <= x <= 2100,
        "Please enter a valid induction year between 1900 and 2100."
    )
    
    games_played = get_validated_input(
        "Enter the player's total games played: ",
        int,
        lambda x: x >= 0,
        "Games played cannot be negative. Please enter a valid number."
    )

    points = get_validated_input(
        "Enter the player's total points: ",
        int,
        lambda x: x >= 0,
        "Points cannot be negative and must be a number. Please enter a valid number."
    )

    rebounds = get_validated_input(
        "Enter the player's total rebounds: ",
        int,
        lambda x: x >= 0,
        "Rebounds cannot be negative and must be a number. Please enter a valid number."
    )

    assists = get_validated_input(
        "Enter the player's total assists: ",
        int,
        lambda x: x >= 0,
        "Assists cannot be negative and must be a number. Please enter a valid number."
    )

    steals = get_validated_input(
        "Enter the player's total steals: ",
        int,
        lambda x: x >= 0,
        "Steals cannot be negative and must be a number. Please enter a valid number."
    )

    blocks = get_validated_input(
        "Enter the player's total blocks: ",
        int,
        lambda x: x >= 0,
        "Blocks cannot be negative and must be a number. Please enter a valid number."
    )

    return [player_name, induct_year, games_played, points, rebounds, assists, steals, blocks]


start_menu()