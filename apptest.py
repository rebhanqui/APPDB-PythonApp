# 1 - View Cities by Country
def cities_by_country(tx, module):
    query = "MATCH(c:City{city:Dublin})<-[t:TWINNED_WITH]-(c:City) RETURN c.name"
    results = tx.run(query, test(module))
    tests = []
    for result in results:
        tests.append(results["c.name"])
    return tests
# 2 - Update City Population

# 3 - Add New Person - SQL
def add_person(tx, person):
    query = "CREATE(p:person{name:Tralee, cid:2345}) RETURN p"
    result = tx.run(query, name= person["name"], id=person["id"])

# 4 - Delete Person - SQL

# 5 - View Countries by population

# 6 - Show Twinned Cities

# 7 - Twinned with Dublin - Neo4j
def dublin_twinned(tx, module):
    query = "MATCH(c:City{city:Dublin})<-[t:TWINNED_WITH]-(c:City) RETURN c.name"
    results = tx.run(query, test(module))
    tests = []
    for result in results:
        tests.append(results["c.name"])
    return tests

# x - Exit Application
    

with neo4jDriver.session() as session:
    tests = session.write_transaction(get_city, "testing")
    for test in tests:
            print(test)

#readtransaction
with neo4jDriver.session() as session:
    tests = session.read_transaction(get_city, "testing")
    for test in tests:
            print(test)
            
with neo4jDriver.session() as session:
    try:
        session.write_transaction(add_city, {"name": "Tralee", "cid": "2345"})
        print("City Added")
    except exceptions.ConstraintError as e:
        print("ERROR: ", e.message)


