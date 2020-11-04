import numpy as np
import bisect

def get_cosine_score(inv_ind, query_terms, doc_list):
    cosine_scores = []
    idf_vector = np.array([inv_ind[term][0] for term in query_terms])
    query_tf_vector = np.array([query_terms.count(term) for term in query_terms])
    query_weights = query_tf_vector * idf_vector
    for doc_id in doc_list:
        doc_tf_vector = []
        for term in query_terms:
            ind = bisect.bisect_left(inv_ind[term][1], (doc_id,))
            if ind != len(inv_ind[term][1]) and inv_ind[term][1][ind][0] == doc_id:
                doc_tf_vector.append(inv_ind[term][1][ind][2])
            else:
                doc_tf_vector.append(0)
        doc_tf_vector = np.array(doc_tf_vector)  
        doc_weights = doc_tf_vector * idf_vector
        doc_score = np.dot(doc_weights, query_weights)/(np.linalg.norm(doc_weights)*np.linalg.norm(query_weights))
        bisect.insort_right(cosine_scores, (doc_score, doc_id))
        
    return cosine_scores
