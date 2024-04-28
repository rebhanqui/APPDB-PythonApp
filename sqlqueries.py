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
    
        sql = "SELECT city.ID, city.Name, city.CountryCode, city.Population, city.latitude, city.longitude FROM city; UPDATE city SET population = ? WHERE population = ?;"
        
        cursor.execute(sql, (city_choice))