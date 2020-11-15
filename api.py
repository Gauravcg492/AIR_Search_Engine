import flask
from flask import jsonify
from search import Search
from index import Index

kgram_path = '../k_gram.json'
inv_ind_path = '../inv_index.json'

app = flask.Flask(__name__)
app.config["DEBUG"] = True
index = Index(inv_ind_path, kgram_path)
print("Done Indexing")

@app.route('/', methods=['GET'])
def search_engine():
	query = str(flask.request.args.get("q"))
	no_docs = 10
	print("Query:", query)
	engine = Search(index, no_docs)
	result = engine.search(query)
	return jsonify(result)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)	
	


