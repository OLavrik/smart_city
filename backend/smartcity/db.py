import pymongo
# Create the client
client = pymongo.MongoClient('localhost', 27017)

# Connect to our database
db = client['smartcity_deb']

# Fetch our series collection
region_stats_collection = db['region_stats']