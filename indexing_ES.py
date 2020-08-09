from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch() #Elasticsearch object

# es.indices.create(index = 'homeware') #Creating index

# es.indices.delete(index='samplesites', ignore=[400, 404]) #Deleting index

with open('./Homeware/products/947_amazon.csv') as f: #Indexing documents
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='homeware', chunk_size=100)
