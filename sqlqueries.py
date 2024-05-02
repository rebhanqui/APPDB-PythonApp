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
    
    sql = """SELECT city.ID, city.Name, city.CountryCode, city.Population, city.latitude, city.longitude 
    FROM city; 
    
    UPDATE city 
    SET population = %s 
    WHERE population = %s;"""
        
    with conn:
        cursor = conn.cursor()    
        cursor.execute(sql, city_choice("%s"))
        result = cursor.fetchall()
        print(result)

# Question 3         
def addPerson():
    connect()
    
    sql = "INSERT INTO person VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(sql)
        
# Question 4
def viewCountriesByPopulation():
    
    if (not conn):
            connect();
    
    #has visited do not delete
    sql = """SELECT * 
    FROM hasvisitedcity 
    WHERE personid = %s"""
            
    sql = """DELETE FROM person 
    WHERE person.personID = %s;"""

# Question 5            
def getTwinnedCities():
    connect()
    
    sql = "SELECT country.Code, country.Name, country.Continent, country.Population FROM country ORDER BY country.Code"
    
# Question 6 and 7 work with Neo4j databases and are located in the neo4jqueries.py file