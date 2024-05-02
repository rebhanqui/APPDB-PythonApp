#rename file dont forget



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
5 - View Countries by Population
6 - Show Twinned Cities
7 - Twin with Dublin
x - Exit Application""")

def main():

    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == "1":
            sqlqueries.viewCitiesByCountry()
        elif choice == "2":
            sqlqueries.updateCityPopulation()
        elif choice == "3":
            sqlqueries.addPerson()
        elif choice == "4":
            sqlqueries.deletePerson()
        elif choice == "5":
            sqlqueries.viewCountriesByPopulation()
        elif choice == "6":
            neo4jqueries.getTwinnedCities()
        elif choice == "7":
            neo4jqueries.twinnedWithDublin()
        else:
            print("Quitting...")
            break


if __name__ == "__main__":
    #importing additional files that contain sql and neo4j queries
    #to make troubleshooting easier
    import sqlqueries
    import neo4jqueries

    main()