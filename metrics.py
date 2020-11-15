import json
ES_URL_set = set()
our_URL_set = set()

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
	return fn

def send_ES_req(query):
	import os
	query = query.replace(" ", "+")
	url = "http://localhost:9200/bbcnews/_search?q="+ query+ "&pretty"
	cmd = 'curl -H "Content-Type: application/json" -XPOST '+url+ " > elastic_op.json"
	try:
		res = os.system(cmd)
	except Exception as e:
		print("Cannot send query to elastic search. ", e)
	# the results will be stored in a json file

def read_ES_json(file):
	import json
	try:
		f=open(file)
		ES_data = json.load(f)
		for el in ES_data['hits']['hits']:
			ES_URL_set.add(el["_source"]["URL"])
	except Exception as e:
		print("Cannot read elastic search results. ", e)
	
def read_our_json(file):
	try:
		import json
		f=open(file)
		data = json.load(f)
		for el in data:
			our_URL_set.add(el["URL"])
	except Exception as e:
		print("Cannot read our search engine's results. ", e)

def get_metrics(query):
	send_ES_req(query)
	read_ES_json("elastic_op.json")
	read_our_json("our_op.json")
	tp = get_tp(ES_URL_set, our_URL_set)
	fp = get_fp(ES_URL_set, our_URL_set)
	fn = get_fn(ES_URL_set, our_URL_set)
	try:
		prec = tp/(tp+fp)
		recall = tp/(tp+fn)
		f_score = (2.0*prec*recall)/(prec+recall)
		return (prec, recall, f_score)
	except Exception as e:
		print("Error: ",e)
		return (0,0,0)