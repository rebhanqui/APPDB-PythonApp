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

def get_countries():
    if (not conn):
        connect();

        sql = "SELECT country.Name AS Country, city.Name AS City Name, city.District AS District Name, city.Population FROM country INNER JOIN city ORDER BY country.Name"

    with conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
            
def update_pop():
    if (not conn):
            connect();
    
        sql = "SELECT city.ID, city.Name, city.CountryCode, city.Population, city.latitude, city.longitude FROM city; UPDATE city SET population = %s WHERE population = %s;"
        
        cursor.execute(sql, (city_choice))
        
def add_new():
    if (not conn):
            connect();
    
        sql = "INSERT INTO person VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql)

def delete_per():
    
    if (not conn):
            connect();
    
    #has visited do not delete
        sql = "SELECT * FROM hasvisitedcity WHERE personid = %s"
            
            sql = "DELETE FROM person WHERE person.personID = %s;"
            
def country_by_pop():
    if (not conn):
            connect();
    
    sql = "SELECT country.Code, country.Name, country.Continent, country.Population FROM country ORDER BY country.Code"