import nltk
import string
from nltk.corpus import stopwords
# import lemmatize, tokenize and inverted_index_generator
from kgram import Kgram
from cosine_scoring import cosine_scoring
from inverted_index import token_gen
from intersect import intersect
from read_inv_index import get_inv_index

class search:
    def __init__(self):
        # for preprocessing data
        # self.inv_ind = {}
        self.inv_ind = get_inv_index()
        # pass inv_ind to kgram
        self.kgram = Kgram(self.inv_ind)
        self.k =10
        self.mappings = get_mappings() #TODO: should return dict {doc_id = URL}
        pass
    
    # Function which intersects the terms in query and then score the intersected documents
    def intersect_score(self):
        doc_list = intersect.posinter_over_invindex(self.inv_ind, self.query, self.wildcard_index)
        if(doc_list<self.k):
            doc_list = intersect.posinter_over_invindex(self.inv_ind, self.query, self.wildcard_index, False)
        return cosine_scoring.get_cosine_score(self.inv_ind, self.query_terms, doc_list)
    
    # Function which finds cosine score from champion list of the queries

    def spelling_correction(self, term):
        term_bi_len = len(term)-1
        kgram_term = self.kgram.get_kgram_query(term, False)
        term_count = {}
        for bigram in kgram_term.keys():
            for t in kgram_term[bigram]:
                if t not in term_count:
                    term_count[t] = 0
                term_count[t] += 1
        max_term = ''
        max_jaccard = 0
        for t in term_count:
            union = len(t) - 1 + term_bi_len - term_count[t]
            jaccard = term_count[t]/union
            if jaccard > max_jaccard:
                max_jaccard = jaccard
                max_term = t
        return max_term

    def get_wild_query(self, term):
        prefix = True if term[-1] == '*' else False
        tquery = term.replace('*','')
        kdict = self.kgram.get_kgram_query(tquery)
        return intersect.kgramintersect(kdict,prefix)
        

    def search(self, query_text):
        query_terms = []
        position = -1
        wildcard_index = {} #for wildcard query term
        for term in nltk.word_tokenize(query_text):
            term = token_gen.normalize(term)
            position+=1
            if(term ==''):
                continue
            if term not in self.inv_ind:
                term = self.spelling_correction(term)
            if('*' in term):
                # TODO
                wildcard_terms = get_wild_query(term) #get all terms for mon*
                wildcard_index = merge_terms() #should give new idf, champion list, zones list for wildcard query(eg:- 'mon*')



            query_terms.append(term)

        self.wildcard_index = wildcard_index
        self.query_terms = query_terms
        self.query = ' '.join(query_terms)
        cosine_score1=self.intersect_score()
        if(len(cosine_score1)> k):
            for score in cosine_score1[::-1]:
                doc_id= score[1]
                url = self.mappings[doc_id]
                # TODO: snippet = 


            # TODO:
            # read doc 
