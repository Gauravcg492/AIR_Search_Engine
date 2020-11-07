import flask
from search import search
search = search()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def search_engine():
	query=request.form.get("query")
	search.search(query)

	


