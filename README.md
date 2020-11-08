# AIR_Search_Engine
Search Engine developed as part of Algorithm for Information Retrieval.
1. Assumed Directory Structure (for preprocessing and inverted index construction):
```
	Project
	|-- AIR_Search_Engine
	|-- temp-data
	|-- dataset
	    |-- TelevisionNews
```
2. Please use AIR.ipynb which has logic to find cosine similarity between a query with several docs,where first we do positional intersect algorithm only for query terms in the dictionary of posting list to get docIDs with high query term proximity. Here we assume(in terms of python lang) the posting list is a dictionary,where vocab terms are keys and values are dictionary containing only one key-value pair,where key is the docID and value is its positional posting list.Then we get tf-idf weight vectors for query and all documents in the determined list and perform scoring. 
Here just function call for positional intersect is done but implementation of the same is yet to be done.Wildcard query like "Algo*" is slightly been done.


# Steps:
Enter the directories in the order mentioned below and follow the commands in their README's
1. ```cd data-preprocessing```
 - Preprocessing Data: CSV -> JSON 
2. ```cd inverted-index```
 - Inverted Index Construction: includes handling of stop words, lemmatization
 - Already generated inverted index can be downloaded from [here](https://drive.google.com/file/d/185c_fsIJvuBvvVWvKUgybYes_5xHkdQX/view?usp=sharing)
 - Ensure that ```inv_index.json``` is stored in the ```Project``` directory
 
# Tasks List:
https://docs.google.com/document/d/1KEH00macDTNX73amR6YIomIsJDaQ_df0eBdU33pyeFY/edit
