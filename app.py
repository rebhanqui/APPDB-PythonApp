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
                city_choice = input(int("Enter City ID: "))
                sqlqueries.update_pop(int(city_choice))
                display_menu()
            except:
                if city_choice != sqlqueries.update_pop():
                    print(f"ID not valid, try again\n {city_choice}")
            
                
        elif (choice == 3):
            addID = input(int("Enter Person ID: "))
            addName = input("Enter Person Name: ") 
            addAge = input(int("Enter Age: "))
            addSalary = input(int("Enter Salary: "))
            addCID = input(int("Enter City ID: "))
            sqlqueries.add_new([addID, addName, addAge, addSalary, addCID])
            display_menu()
        elif (choice == 4):
            deleteperson = input("Enter user ID to delete: ")
            sqlqueries.delete_per(deleteperson)
        elif (choice == 5):
            validpopNO = input("Enter population number: ")
            lessmoreeqaulTO = input("Select < OR > OR = : ")
            sqlqueries.country_by_pop(f"{lessmoreeqaulTO} + " " +{validpopNO}")
        elif (choice == 6):
            print(neo4jqueries.twinned_city())
        elif (choice == 7):
            twdublin = input("Enter city ID: ")
            neo4jqueries.twin_with_dublin(twdublin)
        else:
            print("Please select a choice above or x to exit the app")
        


if __name__ == "__main__":
    #modules1
    import sqlqueries
    import neo4jqueries
    import pymysql
    import pymysql.cursors
    db = pymysql.connect(host='localhost',
                        user='user',
                        password='passwd',
                        database='db',
                        cursorclass=pymysql.cursors.DictCursor)
    
    main()