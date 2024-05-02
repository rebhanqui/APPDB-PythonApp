from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
auth = ("neo4j", "neo4jneo4j")

with GraphDatabase.driver(uri, auth=auth) as driver:
    driver.verify_connectivity()

# Question 6
def getTwinnedCities():
    sql = """MATCH (:City)<-[:TWINNED_WITH]->(c:City) 
    RETURN c.name 
    ORDER BY c.name ASC"""
    results = tx.run(sql, test(module))

# Question 7
def twinnedWithDublin():
    try:
        #if does not exist create node
        sql = ""
    except:
        #if yhe city ID exists then the TWINNED relation is created
        sql = ""
    finally:
        #If city id entered is already twinned with dublin (130-Sydney) then nothing is done.
        sql = """MATCH (:City {cid: 1447})-[:TWINNED_WITH]->(c:City) 
        RETURN c.cid, c.name"""