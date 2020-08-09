from elasticsearch import helpers, Elasticsearch
import csv
import json
from shutil import copyfile
from pathlib import Path
import glob
import os
from PIL import Image

files = glob.glob('./image_retrieval/data/train/*.jpg')
for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

files = glob.glob('./image_retrieval/data/test/*.jpg')
for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

web_id=input("web_id")
product_id=input("product_id")
ind = input("index")

destination = "./image_retrieval/data/train/" # destination for training images
destination_test = "./image_retrieval/data/test/" # destination for training images
source = './'+ind+'/images/' # source from which images are to be extracted
web = ["currys","did","harveynorman","powercity","expert_ireland", "amazon", "amazond", "argos", "currys2", "debenhams", "dunelm", "hartsofstur", "houseoffraser", "johnlewis", "lakeland"] # names of the wesites
webCode = ["1533","1459","2268","1460","1458", "947", "1310", "1271", "1270", "1269", "1331", "1330", "1324", "1261", "944"] # websites codes
elastic_client = Elasticsearch() # initializing Elasticsearch code

# Querying from Elasticsearch
path = './'+ind+'/products/'+web_id+'.csv'
print(path)
with open('./'+ind+'/products/'+web_id+'.csv') as f: #Indexing documents
    csv_reader = csv.DictReader(f)
    line_count = 0
    for row in csv_reader:
        if (row["identifier"]==product_id):
            my_query=row["name"]
            print(my_query)

# my_query=input()
result = elastic_client.search(
    index=ind,
    body={
        "query": {
            "match": {
            "name":my_query
            }
        }
    }
)

# Parsing through queried data
for row in result["hits"]["hits"]:
    print (source+web[webCode.index(str(row["_source"]["website_id"]))]+'/'+row["_source"]["website_id"]+'_'+row["_source"]["identifier"]+'.jpg')
    my_file = Path(source+web[webCode.index(str(row["_source"]["website_id"]))]+'/'+row["_source"]["website_id"]+'_'+row["_source"]["identifier"]+'.jpg')
    if my_file.is_file():
        try:
            im=Image.open(my_file)
            copyfile(source+web[webCode.index(str(row["_source"]["website_id"]))]+'/'+row["_source"]["website_id"]+'_'+row["_source"]["identifier"]+'.jpg', destination+row["_source"]["website_id"]+'_'+row["_source"]["identifier"]+'.jpg')
        except IOError:
            print('error')

my_file = Path(source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.jpg')
if my_file.is_file():
    print (source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.jpg')
    copyfile(source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.jpg', destination_test+web_id+'_'+product_id+'.jpg')

my_file = Path(source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.gif')
if my_file.is_file():
    print (source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.gif')
    copyfile(source+web[webCode.index(web_id)]+'/'+web_id+'_'+product_id+'.gif', destination_test+web_id+'_'+product_id+'.gif')
# print(json.dumps(result, indent=4))
# es.get(index="test-index", id=1)