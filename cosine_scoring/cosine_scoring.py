import numpy as np
import bisect
import math

# Function returns the cosine scores of the documents provided as a parameter(doc_list)
# Input: Inverted Index, list of query terms, list of documents
# Ouput: List of tuples in sorted order of the cosine scores in the form [(score, docId)]
def get_cosine_score(inv_ind, wildcard_index, query_terms, doc_list):
    cosine_scores = []
    query_set = list(set(query_terms))
    idf_vector = np.array([inv_ind[term][0] if '*' not in term else wildcard_index[term][0] for term in query_set])
    query_tf_vector = np.array([1+math.log(query_terms.count(term), 10) for term in query_set])
    query_weights = query_tf_vector * idf_vector
    for doc_id in doc_list:
        doc_tf_vector = []
        for term in query_set:
            index = inv_ind
            if '*' in term:
                index = wildcard_index
            ind = bisect.bisect_left(index[term][1], [doc_id,])
            if ind != len(index[term][1]) and index[term][1][ind][0] == doc_id:
                doc_tf_vector.append(index[term][1][ind][2])
            else:
                doc_tf_vector.append(0)
        doc_tf_vector = np.array(doc_tf_vector)  
        doc_weights = doc_tf_vector * idf_vector
        doc_score = np.dot(doc_weights, query_weights)/(np.linalg.norm(doc_weights)*np.linalg.norm(query_weights))
        bisect.insort_right(cosine_scores, (doc_score, doc_id))
        
    return cosine_scores
