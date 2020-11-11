# AIR_Search_Engine
Search Engine developed as part of Algorithm for Information Retrieval (UE17CS412) course.

## Steps:
Enter the directories in the order mentioned below and follow the commands in their README's
1. Construct inverted index:
 - If you want to generate inverted index from scratch [OPTIONAL]
 	- Download [Kaggle Dataset](https://www.kaggle.com/amritvirsinghx/environmental-news-nlp-dataset) and store it as per the directory structure in Notes
 	- ```cd AIR_Search_Engine/inverted-index```
 	- open the README and follow the instructions
 - Else, already generated inverted index can be downloaded from [here](https://drive.google.com/file/d/185c_fsIJvuBvvVWvKUgybYes_5xHkdQX/view?usp=sharing) 
 - Ensure that ```inv_index.json``` outside the ```AIR_Search_Engine``` directory
 - This includes handling of stop words, lemmatization

3. Start the application:
 - ``` python3 api.py ```
 - wait until the "Done Indexing" message shows on your terminal

4. Pass the query
 - Open Postman and create a "GET" request with the URL ```127.0.0.1:8080?q="climate change"```
 - Replace "climate change" with a query/ wildcard query of your choice

# Dependencies
1. ```nltk```
2. ```flask ```

# Notes
1. Directory Structure
(for inverted index construction)
```
	Project
	|-- AIR_Search_Engine
	|-- temp-data
	|-- dataset
	    |-- TelevisionNews
```

2. Please use AIR.ipynb which has logic to find cosine similarity between a query with several docs,where first we do positional intersect algorithm only for query terms in the dictionary of posting list to get docIDs with high query term proximity. Here we assume(in terms of python lang) the posting list is a dictionary,where vocab terms are keys and values are dictionary containing only one key-value pair,where key is the docID and value is its positional posting list.Then we get tf-idf weight vectors for query and all documents in the determined list and perform scoring. 
Here just function call for positional intersect is done but implementation of the same is yet to be done.Wildcard query like "Algo*" is slightly been done.
 
# Tasks List:
https://docs.google.com/document/d/1KEH00macDTNX73amR6YIomIsJDaQ_df0eBdU33pyeFY/edit
