import pymysql
import pymysql.cursors


conn = None

def connect():
        global conn 
        conn = pymysql.connect(
            host="localhost", 
            user="root", 
            password="root", 
            db="appDBproj_MySql.sql", 
            cursorclass=pymysql.cursors.DictCursor
            )

# Question 1
def viewCitiesByCountry():
    if (not conn):
        connect();

    sql = """SELECT country.Name AS Country, city.Name AS City Name, city.District AS District Name, city.Population 
    FROM country 
    INNER JOIN city 
    ORDER BY country.Name 
    WHERE country = %s"""

    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, (countryname))
        result = cursor.fetchall()
        print(result)

# Question 2           
def updateCityPopulation():
    if (not conn):
            connect();
    
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
    if (not conn):
            connect();
    
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
    if (not conn):
            connect();
    
    sql = "SELECT country.Code, country.Name, country.Continent, country.Population FROM country ORDER BY country.Code"
    
# Question 6 and 7 work with Neo4j databases and are located in the neo4jqueries.py file