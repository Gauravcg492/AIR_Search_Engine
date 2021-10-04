import flask
from flask import jsonify
from search import Search
from index import Index
import json
import time
import metrics

inv_ind_path = "../inv_index.json"
kgram_path = "../k_gram.json"
index = Index(inv_ind_path, kgram_path)
print("Done Indexing")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def search_engine():
	query = str(flask.request.args.get("q"))
	no_docs = 20
	print("Query:", query)

	start= time.time()
	search = Search(index, no_docs)
	result = search.search(query)
	stop = time.time()

	with open("our_op.json", "w") as outfile:  
		json.dump(result, outfile)

	metric_tuple= metrics.get_metrics(query)
	our_time = round((stop-start)*1000)
	es_time = metrics.get_ES_time()

	print("\n\n\n----------------------METRICS-------------------------")
	print("Precision, Recall, F-score = ", metric_tuple)
	print("Time taken by our SE (in ms): ", our_time)
	print("Time taken by Elastic Search (in ms):", es_time)
	print("-------------------------------------------------------------\n\n\n")

	#metrics.clean(["our_op.json", "elastic_op.json"])


	return jsonify(result)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)	
	
One
Two
	


