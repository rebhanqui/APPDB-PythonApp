# APPDB-PythonApp

## Modules and Installation

### PyMySQL

In command prompt: `cd` to location of folder then `python3 -m pip install PyMySQL`.

### Neo4j

In command prompt: `pip install neo4j`

## More Information

### Set up Neo4j and MySQL Databases

#### MySQL Initialization

Open Command Prompt.
`cd \Program Files\MySQL\MySQL Server 8.0\bin\` - ensure its is MySQL Server as when you tab through options the first one is different and can be missed.
To import the databases into MySQL server type: `mysql -u root -proot #no space after p < appDBProj.sql` (Drag and drop the file itself after "<")
Then open the MySQL Command Line and to check the database was imported type the following: `show databases;`. You should see appDBProj here.

#### Neo4j Initialization

`cd \Documents\neo4j\neo4j\bin\ neo4j.bat console`

Open a new command prompt
`type filepatHneo4j.db | cypher-shell.bat -u neo4j -p neo4jneo4j --format plain`
change conf file default db to db wanted and save
new command window
`cd \Documents\neo4j\neo4j\bin neo4j.bat console`
open `localhost` in browser TO SEE IF IMPORTED

## References

1. [PyMySQL - API Reference](https://pymysql.readthedocs.io/en/latest/modules/index.html)
2. [Handling PyMySQL exceptions - Stack Overflow](https://stackoverflow.com/questions/41344171/handling-pymysql-exceptions-best-practices)
3. [Partial Match from User Input](https://stackoverflow.com/questions/35605332/partial-match-in-a-list-from-a-user-input)
4. [Python F Strings](https://realpython.com/python-f-strings/)
5. [Try, Except, else and Finally in Python](https://www.geeksforgeeks.org/try-except-else-and-finally-in-python)
6. [New Lines - Python](https://www.idtech.com/blog/what-is-n-in-python)
7. [Multi-Line printing in Python](https://www.geeksforgeeks.org/multi-line-printing-in-python/)
8. [Import Another Python File as a Module](https://csatlas.com/python-import-file-module/)
9. [if __name__ == "__main__" - Python](https://realpython.com/if-name-main-python/)
10. [PyMySQL 1.1.0](https://pypi.org/project/pymysql/)
11. [MySQL cheatsheet](https://devhints.io/mysql)
12. [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/5/auradb-enterprise/)
13. [Python Driver](https://neo4j.com/docs/python-manual/current/)
14. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)