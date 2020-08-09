import os
import csv
import glob
#homeware = ["947_amazon_marketplace.csv", "1261_johnlewis.csv", "1271", "1270", "1269", "1331", "1330", "1324", "1261", "944"]
files = glob.glob('./groundTruth/matches/matches/*.csv')
# files2 = glob.glob('./homeware/products/*.csv')
# tmp = [i.split('_')[0] for i in files2]
a = []
b = []
prod = input()
# path = './groundTruth/matches/matches/947_amazon_marketplace.csv'
# print(path)
# with open('./groundTruth/matches/matches/947_amazon_marketplace.csv') as f: #Indexing documents
#     csv_reader = csv.DictReader(f)
#     line_count = 0
#     for row in csv_reader:
#     	a.append(row["second_identifier"])
# f.close()
# # for f in files2:
# # 	b = files2[tmp.index(f.split('_')[0])]
# # path = './groundTruth/matches/matches/'+f
# # print(path)
# with open('./homeware/products/947_amazon.csv') as f: #Indexing documents
#     csv_reader = csv.DictReader(f)
#     line_count = 0
#     for row in csv_reader:
#     	b.append(row["identifier"])

# uncommon = set(a) - set(b)
# uncommon = list(dict.fromkeys(uncommon))
# print(len(uncommon))
# # print (uncommon)

for ff in files:
	with open(ff) as f:
		csv_reader = csv.DictReader(f)
		line_count = 0
		for row in csv_reader:
			if (row["first_identifier"] == prod):
				print(row["second_identifier"]+'  '+row["second_name"]+'  '+row["second_url"])