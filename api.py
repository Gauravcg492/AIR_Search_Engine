import flask
from flask import jsonify
from search import Search
from index import Index
index = Index()
print("Done Indexing")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def search_engine():
	query = str(flask.request.args.get("q"))
	no_docs = 10
	print("Query:", query)
	search = Search(index, no_docs)
	result = search.search(query)
	with open("our_op.json", "w") as outfile:  
    	json.dump(result, outfile) 
	return jsonify(result)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)	
	


