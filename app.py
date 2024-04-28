#rename file dont forget

#modules1
import sqlqueries

#display menu 
def display_menu():
    print("""
=================================
            Main Menu
=================================

1 - View Cities by Country
2 - Update City Population
3 - Add New Person
4 - Delete Person
5 - View Countries by population
6 - Show Twinned Cities
7 - Twin with Dublin
x - Exit Application""")

def main():

    while True:
        display_menu()
        choice = input("Choice: ")
        
        if (choice == "x"):
            print("Quitting..")
            break
        elif (choice == 1):
            countryname = input("Enter country name: ")
            sqlqueries.get_countries(countryname)
            display_menu()
        elif (choice == 2):
            try:
                city_choice = input("Enter City ID: ")
                sqlqueries.update_pop(int(city_choice))
                display_menu
            except:
                if city_choice != sqlqueries.update_pop()
        elif (choice == 3):
            print("elif 3")
        elif (choice == 4):
            print("elif 4")
        elif (choice == 5):
            print("elif 5")
        elif (choice == 6):
            print("elif 6")
        elif (choice == 7):
            print("elif 2")
        else:
            print("Please select a choice above or x to exit the app")
        


if __name__ == "__main__":
    main()