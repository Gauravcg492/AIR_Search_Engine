# AIR_Search_Engine
Search Engine developed as part of Algorithm for Information Retrievel.

Please use AIR.ipynb which has logic to find cosine similarity between a query with several docs,where first we do positional intersect algorithm only for query terms in the dictionary of posting list to get docIDs with high query term proximity.Here we assume(in terms of python lang) the posting list is a dictionary,where vocab terms are keys and values are dictionary containing only one key-value pair,where key is the docID and value is its positional posting list.Then we get tf-idf weight vectors for query and all documents in the determined list and perform scoring. 

Here just function call for positional intersect is done but implementation of the same is yet to be done.Wildcard query slight been done.
