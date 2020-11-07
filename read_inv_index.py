import json
def get_term(record):
	return record.keys()[0]

def get_idf(record):
	return record[get_term(record)][0]

def get_postings_list(record):
	return record[get_term(record)][1]

def get_champ_list(record):
	return record[get_term(record)][2]

def get_zones_list(record):
	return record[get_term(record)][2]

'''
DRIVER CODE:	
for line in open("../inv_index.json"):
	record = json.loads(line)
	any-of-above-functions(record)

NOTE:
- record is a dictionary
- record has only one key(term) with its corresponding value (idf, postings list, champion list)

'''