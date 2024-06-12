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

# row_1 = NBAStats.row_values(1)
# row_2 = NBAStats.row_values(2)
# row_3 = NBAStats.row_values(3)
# row_4 = NBAStats.row_values(4)
# row_5 = NBAStats.row_values(5)
# row_6 = NBAStats.row_values(6)
# row_7 = NBAStats.row_values(7)
# row_8 = NBAStats.row_values(8)
# row_9 = NBAStats.row_values(9)
# row_10 = NBAStats.row_values(10)
# row_11 = NBAStats.row_values(11)
# row_12 = NBAStats.row_values(12)
# row_13 = NBAStats.row_values(13)
# row_14 = NBAStats.row_values(14)
# row_15 = NBAStats.row_values(15)
# row_16 = NBAStats.row_values(16)
# row_17 = NBAStats.row_values(17)
# row_18 = NBAStats.row_values(18)
# row_19 = NBAStats.row_values(19)
# row_20 = NBAStats.row_values(20)

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
    print(all_stats)
     
    while True:
        user_input = input('Please select a number between 1 - 4\n')
        
        if user_input == '1':
            print("List of 20 Hall Of Fame Players and their career total stats:")
            for i in range(1, 21):
                print(f"Row {i}: {NBAStats.row_values(i)}")
        elif user_input == '2':
            Name = input("Enter the player's name: ")
            for i in range(1, 21):
                if NBAStats.row_values(i)[0] == Name:
                    print(f"{Name}'s career stats: {NBAStats.row_values(i)}")
                    break
            else:
                print("Player not found.")
        elif user_input == '3':
            player_name = input("Enter the player's name: ")
            induct_year = int(input("Enter the player's induction year: "))
            games_played = int(input("Enter the player's total games played: "))
            points = int(input("Enter the player's total points: "))
            rebounds = int(input("Enter the player's total rebounds: "))
            assists = int(input("Enter the player's total assists: "))
            steals = int(input("Enter the player's total steals: "))
            blocks = int(input("Enter the player's total blocks: "))
            print("Adding a new Hall of Famer's stats to the list.")

           

            update_NBAStats_sheet([player_name, induct_year, games_played, points, rebounds, assists, steals, blocks])
        elif user_input == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

start_menu()