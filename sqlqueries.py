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
        except pymysql.Error as Error:
            print("MySQL Error:", Error)
            return None
        finally:
            conn.close


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
def deletePerson():
    if not conn:
        connect()
    
    try:
        with conn.cursor() as cursor:
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
def viewCountriesByPopulation():
    if not conn:
        connect()
    
    try:
        with conn.cursor() as cursor:
            operators = ['<', '>', '=']
            while True:
                #input operator to base the population on - greater than, less than, equal to
                operator = input("Enter the operator (<, >, or =): ")
                if operator not in operators:
                    print("Invalid operator. Please try again.")
                    continue
                #population input to look for with operator selected
                population = input("Enter the population number: ")
                try:
                    population = int(population)
                    if population < 0:
                        print("Population number must be non-negative. Please try again.")
                        continue
                except ValueError:
                    print("Invalid population number. Please try again.")
                    continue

                #countries selected based on operator input and population
                query = f"SELECT Code, Name, Continent, Population FROM country WHERE Population {operator} %s"
                cursor.execute(query, (population,))
                countries = cursor.fetchall()

                #results printed based on above if no error found
                if countries:
                    for country in countries:
                        print(f"Code: {country['Code']}")
                        print(f"Name: {country['Name']}")
                        print(f"Continent: {country['Continent']}")
                        print(f"Population: {country['Population']}")
                        print()
                else:
                    print("No countries match the population condition.")

                break #exit while loop after results
            
    except pymysql.Error as Error:
        print("MySQL Error:", Error)
        return None
    finally:
        conn.close 


if conn:
    conn.close()  #close database if exiting the application       
# Question 6 and 7 work with Neo4j databases and are located in the neo4jqueries.py file