# Tokenization
1. ```python3 token_gen.py``` 
	- generates tokens, removes stop words, does lemmatization and other normalization techniques. 
	- Creates (term, doc-id, pos, zone) quadruplets
	- takes long to execute
	- generates ```term_doc_id_pos``` in ```temp-data```
	
2. ```
	cd ../../temp-data
	sort --version-sort term_doc_id_pos > term_doc_id_pos_sorted
	``` 
	- sorts the (term, doc-id, pos, zone) quadruplets in that order.
3. ```cd ../AIR_Search_Engine/inverted_index``` 
	Run ```jupyter notebook inverted_index.ipynb``` in Jupyter Notebook and run all the cells
	- generates ``` inv_index.json ``` in ```Project```
	- takes long to execute
	- Format of inverted_index:
	```
	{ term : [
	 			idf, 
	 	 		[ (doc-id1, [positions1], tf1 ), (doc-id2, [positions2], tf2), ... ] - Postings list,  
	 	 		[ (docid,[positions],tf1) ] - champion list,
	 	 	 	[zones list]
	 	 	]
	 }
	```

# Assumed Directory Structure
```
Project
	|-- AIR_Search_Engine
	|-- temp-data
	|-- dataset
	    |-- TelevisionNews
```