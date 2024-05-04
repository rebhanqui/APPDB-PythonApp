from neo4j import GraphDatabase

# Connect to Neo4j database
driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"))

# Question 6
def runCities(tx):
    query = (
        "MATCH (c:City)-[:TWINNED_WITH]->(d:City) "
        "RETURN c.name AS CityName, d.name AS TwinnedWith "
        "ORDER BY c.name"
    )
    results = tx.run(query)
    return [(record["CityName"], record["TwinnedWith"]) for record in results]

def getTwinnedCities():
    connect()
    with driver.session() as session:
        values = session.read_transaction(runCities)
        if not values:
            print("No twinned cities found.")
        else:
            print("Twinned Cities:")
            for city, twinnedWith in values:
                print(f"{city} twinned with {twinnedWith}")


#Question 7

def cityExists(cityID):
    with driver.session() as session:
        result = session.run(
            "MATCH (c:City {cid: $cityID}) RETURN count(c) AS count",
            cityID=cityID
        )
        record = result.single()
        return record["count"] > 0

def createCity(cityID, cityName):
    with driver.session() as session:
        session.run(
            "CREATE (c:City {cid: $cityID, name: $cityName})"
            "WITH c "
            "MATCH (d:City {name: 'Dublin'})"
            "CREATE (c)-[:TWINNED_WITH]->(d)",
            cityID=cityID,
            cityName=cityName
        )

def twinnedWithDublin():
    connect()
    cityID = input("Enter the ID of the city: ")

    with driver.session() as session:
        result = session.run(
            "MATCH (c:City {cid: $cityID}) "
            "RETURN count(c) AS count",
            cityID=cityID
        )
        record = result.single()
        if record["count"] == 0:
            # City does not exist, prompt user to enter the name of the city
            cityName = input("Enter the name of the city: ")
            # Create the city in the database
            createCity(cityID, cityName)
            print(f"City with ID {cityID} and name {cityName} created and twinned with Dublin.")
        else:
            # City exists, check if twinned with Dublin
            result = session.run(
                "MATCH (c:City {cid: $cityID})-[:TWINNED_WITH]->(:City {name: 'Dublin'}) "
                "RETURN count(c) AS count",
                cityID=cityID
            )
            record = result.single()
            if record["count"] == 0:
                # City is not twinned with Dublin, create the twinned relationship
                session.run(
                    "MATCH (c:City {cid: $cityID}), (d:City{name: 'Dublin'}) "
                    "MERGE (c)-[:TWINNED_WITH]->(d)",
                    cityID=cityID
                )
                print(f"City with ID {cityID} twinned with Dublin.")
            else:
                # City is already twinned with Dublin
                print(f"City with ID {cityID} is already twinned with Dublin.")

