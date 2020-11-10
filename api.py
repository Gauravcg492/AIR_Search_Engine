import flask
from search import Search
from index import Index
index = Index()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def search_engine():
	query = flask.request.form.get("query")
	no_docs = 10
	search = Search(index, no_docs)
	result = search.search(query)

	


