def get_tp(benchmark_set, results_set):
	#retrieved and relevant
	tp  = len(benchmark_set.intersection(results_set))
	return tp

def get_fp(benchmark_set, results_set):
	#retrieved, but not relevant
	fp = len(results_set.difference(benchmark_set))
	return fp

def get_fn(benchmark_set, results_set):
	#not retrieved, but relevant
	fn = len(benchmark_set.difference(results_set))

def send_ES_req(query):
	import os
	query = query.replace(" ", "+")
	url = "http://localhost:9200/bbcnews/_search?q="+ query+ "&pretty"
	cmd = 'curl -H "Content-Type: application/json" -XPOST '+url+ " > elastic_op.json"
	res = os.system(cmd)
	# the query will be stored in a json file

def read_ES_json(file):
	import json
	f=open(file)
	ES_data = json.load(f)
	ES_URL_set = set()
	for el in ES_data['hits']['hits']:
		ES_URL_set.add(el["_source"]["URL"])
	return ES_URL_set

def read_our_json(file):
	import json
	f=open(file)
	data = json.load(f)
	

def 