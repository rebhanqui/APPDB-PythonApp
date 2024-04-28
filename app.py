#rename file dont forget and connect to git!!!

#display menu 
def main():
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if (choice == "x"):
            print("Quitting..")
            break
        elif (choice == 1):
            print(1)
        elif (choice == 2):
            print(2)
        elif (choice == 3):
            print(3)
        elif (choice == 4):
            print(4)
        elif (choice == 5):
            print(5)
        elif (choice == 6):
            print(6)
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



if __name__ == "__main__":
    main()