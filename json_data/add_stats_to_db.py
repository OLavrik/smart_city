import json
import os

import pymongo
# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['smartcity_deb']
region_stats_collection = db['region_stats']

root_dir =os.path.join(os.path.dirname(os.path.abspath(__file__)))
files = os.listdir(root_dir)
for filename in files:
    if not filename.endswith('.json'):
        continue
    print("Processing", filename)
    with open(os.path.join(root_dir,filename), 'rt', encoding='utf-8') as f:
        data = json.load(f)
        if 'tag' not in data:
            print('--- tag field is MISSNG')
            continue
        if region_stats_collection.find_one({"tag":data["tag"]}):
            print(f'--- Already exists with tag {data["tag"]}')
            continue
        region_stats_collection.insert_one(data)
