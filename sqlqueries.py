#modules to import
import pymysql

conn = None

def connect():
    global conn 
    try:
        conn = pymysql.connect(
            host="localhost", 
            user="root", 
            password="root", 
            db="appDBproj", 
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    #returns error and detail if connection fails
    #https://stackoverflow.com/questions/41344171/handling-pymysql-exceptions-best-practices
    except pymysql.Error as Error:
        print("Error connecting to the database:", Error)
        return None

# Question 1
def viewCitiesByCountry():
    if not conn:
        connect()

    try:
        with conn.cursor() as cursor:
            countryName = input("Enter the name of a country: ")
            query = """SELECT country.Name, city.Name, city.District, city.Population, city.latitude, city.longitude 
                    FROM country 
                    JOIN city ON country.Code = city.CountryCode 
                    WHERE country.Name LIKE %s"""
            cursor.execute(query, (countryName,))
            cities = cursor.fetchall()

#if cities are found in database under country name then code iterates through results of sql query
#results then display unless none found and else prints this            
            if cities:
                chosenCountry = None
                for city in cities:
                    if chosenCountry != city['Name']:
                        chosenCountry = city['Name']
                        print(f"Country: {chosenCountry}")
                    print(f"City: {city['Name']}")
                    print(f"District: {city['District']}")
                    print(f"Population: {city['Population']}")
                    print()
            else:
                print(f"No cities found for {countryName}")
#https://realpython.com/python-f-strings/
    except pymysql.Error as Error:
        print("MySQL Error:", Error)
        return None
    finally:
        conn.close
#https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/

# Question 2           
def updateCityPopulation():
    if not conn:
        connect()
    
    try:
        while True:
            #first inpur query for city ID 
            cityID = input("Enter the ID of the city: ")
            with conn.cursor() as cursor:
                query = "SELECT * FROM city WHERE ID = %s"
                cursor.execute(query, (cityID,))
                city = cursor.fetchone()
                #city information is then printed if the city id exists
                if city:
                    print("City details:")
                    print(f"ID: {city['ID']}")
                    print(f"Name: {city['Name']}")
                    print(f"CountryCode: {city['CountryCode']}")
                    print(f"Population: {city['Population']}")
                    print(f"Latitude: {city['latitude']}")
                    print(f"Longitude: {city['longitude']}")

                    #if exists then user is asked if they want to increase or decrease pop no, input is made lowercase.
                    change = input("Do you want to increase or decrease the population? (Enter 'I' for increase, 'D' for decrease): ").lower()
                    if change == 'i':
                        updatePopulation = int(input("Enter the amount to increase the population: "))
                    elif change == 'd':
                        updatePopulation = -int(input("Enter the amount to decrease the population: "))
                    else:
                        #if input invalid user notified and returned to mainmenu
                        print("Invalid choice.")
                        return

                    #if all input is valid then sql query updates pop and notifys user
                    query = "UPDATE city SET Population = Population + %s WHERE ID = %s"
                    cursor.execute(query, (updatePopulation, cityID))
                    conn.commit()
                    print("Population updated successfully.")
                    #asks if user wishes to continue or return to main menu
                    choice = input("Do you want to continue updating population or return to the main menu? (Enter 'C' to continue, 'M' for main menu): ").lower
                    if choice == "m":
                        break
                else:
                    print("Invalid city ID. Please try again.")
    
    except pymysql.Error as Error:
        print("MySQL Error:", Error)
        return None
    finally:
        conn.close

# Question 3         
def addPerson():
    if not conn:
        connect()

    try:
        with conn.cursor() as cursor:
            personID = input("Enter person ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            salary = input("Enter salary: ")
            cityID = input("Enter cityID: ")
        
        #Check if personid exists
            query = "SELECT * FROM person WHERE personID = %s"
            cursor.execute(query, (personID,))
            personExists = cursor.fetchone()
            
            if personExists:
                print("This person already exists in the database")
                return
            
        #Check city ID exists
            query = "SELECT * FROM city WHERE ID = %s"
            cursor.execute(query, (cityID,))
            cityExists = cursor.fetchone()
            if not cityExists:
                print("City ID does not exist in the database")
                return
        
        #if all information is valid then add to database
            query = "INSERT INTO person (personID, personname, age, salary, city) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (personID, name, age, salary, cityID))
            #commits to db
            conn.commit()
            print(f"""The following person was added:\n
                ID: {personID}\n
                Name: {name}\n
                Age: {age}\n
                Salary: {salary}\n
                City ID: {cityID}\n""")

    except pymysql.Error as Error:
        print("MySQL Error:", Error)
        return None
    finally:
        conn.close   

        
# Question 4
def viewCountriesByPopulation():
    if not conn:
        connect()
    
    try:
        with conn.cursor as cursor:
            personID = input("Enter the ID of the person to delete: ")

            # Check if the person exists
            personExists = "SELECT * FROM person WHERE personID = %s"
            cursor.execute(personExists, (personID,))
            person = cursor.fetchone()
            
            if not person:
                print("No person exists with this ID")
                return

            #has person visited cities check and no deletion
            visitedCities = "SELECT * FROM hasvisitedcity WHERE personID = %s"
            cursor.execute(visitedCities, (personID,))
            visitedCities = cursor.fetchall()
            
            if visitedCities:
                print("This person has visited cities and cannot be removed")
                
            #if person has not visited cities then delete them from database
            deletePerson = "DELETE FROM person WHERE personID = %s"
            cursor.execute(deletePerson, (personID,))
            conn.commit()
            print("Person deleted")
        
    except pymysql.Error as Error:
        print("MySQL Error:", Error)
        return None
    finally:
        conn.close 
    

# Question 5            
def getTwinnedCities():
    connect()
    
    sql = "SELECT country.Code, country.Name, country.Continent, country.Population FROM country ORDER BY country.Code"
    
# Question 6 and 7 work with Neo4j databases and are located in the neo4jqueries.py file