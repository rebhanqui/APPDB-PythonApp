#rename file dont forget and connect to git!!!

#display menu 
def main():
    countryStr = "Enter country name: "
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if (choice == "x"):
            print("Quitting..")
            
        elif (choice == 1):
            country = cities_by_country(countryStr)
            print(country)
            
        elif (choice == 2):
            population = update_pop()
            print(population)
            break
        else:
            print("Please select a choice above or x to exit the app")
        

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

def cities_by_country(n):
    country = input(n)
    return country
    #mysql query
    
def update_pop():
    population = input()
    return population

if __name__ == "__main__":
    main()