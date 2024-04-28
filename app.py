#rename file dont forget

#modules1
import sqlqueries
import neo4jqueries

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
                display_menu()
            except:
                if city_choice != sqlqueries.update_pop()
        elif (choice == 3):
            sqlqueries.add_new()
            display_menu()
        elif (choice == 4):
            sqlqueries.delete_per()
        elif (choice == 5):
            sqlqueries.country_by_pop()
        elif (choice == 6):
            neo4jqueries.twinned_city()
        elif (choice == 7):
            twdublin = input("Enter city ID: ")
            neo4jqueries.twin_with_dublin(twdublin)
        else:
            print("Please select a choice above or x to exit the app")
        


if __name__ == "__main__":
    main()