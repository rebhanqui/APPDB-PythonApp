# APPDB-PythonApp

## Modules and Installation

### PyMySQL

In command prompt: `cd` to location of folder then `python3 -m pip install PyMySQL`. 

## More

### Set up Neo4j and MySQL Databases

#### MySQL

Open Command Prompt.
`cd \Program Files\MySQL\MySQL Server 8.0\bin\` - ensure its is MySQL Server as when you tab through options the first one is different and can be missed.
To import the databases into MySQL server type: `mysql -u root -proot #no space after p < appDBProj.sql` (Drag and drop the file itself after "<")
Then open the MySQL Command Line and to check the database was imported type the following: `show databases;`. You should see appDBProj here.

#### Neo4j

`cd \Documents\neo4j\neo4j\bin\ neo4j.bat console`

Open a new command prompt
`type filepatHneo4j.db | cypher-shell.bat -u neo4j -p neo4jneo4j --format plain`
change conf file default db to db wanted and save
new command window
`cd \Documents\neo4j\neo4j\bin neo4j.bat console`
open `localhost` in browser TO SEE IF IMPORTED

## References

1. https://pymysql.readthedocs.io/en/latest/modules/index.html
2. https://stackoverflow.com/questions/41344171/handling-pymysql-exceptions-best-practices
3. https://stackoverflow.com/questions/35605332/partial-match-in-a-list-from-a-user-input
4. https://realpython.com/python-f-strings/
5. https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/
6. https://www.idtech.com/blog/what-is-n-in-python