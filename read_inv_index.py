import json
def get_inv_index():
	f = open("../inv_index.json"):
	inv_index = json.load(f)
	return inv_index

'''def get_idf(term):
	return record[get_term(record)][0]

def get_postings_list(record):
	return record[get_term(record)][1]

def get_champ_list(record):
	return record[get_term(record)][2]

def get_zones_list(record):
	return record[get_term(record)][2]
'''

'''
DRIVER CODE:	
for line in open("../inv_index.json"):
	record = json.loads(line)
	any-of-above-functions(record)

NOTE:
- record is a dictionary
- record has only one key(term) with its corresponding value (idf, postings list, champion list)

'''