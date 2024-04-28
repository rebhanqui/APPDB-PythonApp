# Question 6
def twinned_city(tx, module):
    sql = "MATCH (:City)<-[:TWINNED_WITH]->(c:City) RETURN c.name ORDER BY c.name ASC"
    results = tx.run(sql, test(module))

# Question 7
def twin_with_dublin(tx, module):
    try:
        #if does not exist create node
        sql = ""
    except:
        #if yhe city ID exists then the TWINNED relation is created
        sql = ""
    finally:
        #If city id entered is already twinned with dublin (130-Sydney) then nothing is done.
        sql = "MATCH (:City {cid: 1447})-[:TWINNED_WITH]->(c:City) RETURN c.cid, c.name"