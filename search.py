import nltk
import string
from nltk.corpus import stopwords
# import lemmatize, tokenize and inverted_index_generator
from cosine_scoring import cosine_scoring
from inverted_index import token_gen
from intersect import intersect
from read_inv_index import get_record

class Search:
    def __init__(self, index, no_docs):
        # for preprocessing data
        # self.inv_ind = {}
        self.inv_ind = index.inv_ind
        # pass inv_ind to kgram
        self.kgram = index.kgram
        self.k = no_docs
    
    # Function which intersects the terms in query and then score the intersected documents
    def intersect_doc_list(self):
        doc_list = intersect.posinter_over_invindex(self.inv_ind, self.query_terms, self.wildcard_index)
        if(len(doc_list)<self.k):
            doc_list = intersect.posinter_over_invindex(self.inv_ind, self.query_terms, self.wildcard_index, False)
        #return cosine_scoring.get_cosine_score(self.inv_ind, self.wildcard_index, self.query_terms, doc_list[:20])
        return doc_list
    
    # Function which finds cosine score from champion list of the queries
    def union_doc_list(self):
        doc_list = intersect.merge_docs(self.inv_ind, self.query_terms, self.wildcard_index, champion_list=True)
        if len(doc_list) < self.k:
            doc_list = intersect.merge_docs(self.inv_ind, self.query_terms, self.wildcard_index, champion_list=False)
        #return cosine_scoring.get_cosine_score(self.inv_ind, self.wildcard_index, self.query_terms, doc_list[:20])
        return doc_list

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
        return intersect.kgramintersect(kdict,tquery,prefix)
        
    def merge_terms(self, wild_terms, term):
        if term not in self.wildcard_index:
            self.wildcard_index[term] = self.inv_ind[wild_terms[0]]
            for wild_term in wild_terms[1:]:
                self.wildcard_index[term] = intersect.merge_terms(self.wildcard_index[term], self.inv_ind[wild_term])

    def return_documents(self, scores):
        result = []
        temp = scores[::-1]
        for score in temp[:self.k]:
            result.append(get_record(score[1],score[0]))
        return result

    def search(self, query_text):
        query_terms = []
        #position = -1
        self.wildcard_index = {} #for wildcard query term
        for term in nltk.word_tokenize(query_text):
            term = token_gen.normalize(term)
            #position+=1
            if(term ==''):
                continue
            if('*' in term):
                wildcard_terms = self.get_wild_query(term) #get all terms for mon*
                self.merge_terms(wildcard_terms, term) #should give new idf, champion list, zones list for wildcard query(eg:- 'mon*')
            elif term not in self.inv_ind:
                term = self.spelling_correction(term)

            query_terms.append(term)

        self.query_terms = query_terms # Why was it query_term[1:] ?
        '''
        cosine_score1=self.intersect_score()
        if(len(cosine_score1)> self.k):
            result = self.return_documents(cosine_score1)
        else:
            cosine_score2 = self.cosine_score_all()
            total_cosine_score = sorted(set(cosine_score1 + cosine_score2))
            if len(total_cosine_score) > self.k:
                result = self.return_documents(total_cosine_score)
            else:
                cosine_score3 = self.cosine_score_all(champion=False)
                total_cosine_score = sorted(set(total_cosine_score + cosine_score3))
                result = self.return_documents(total_cosine_score)
        '''
        doc_list = self.intersect_doc_list()
        if len(doc_list) < self.k:
            doc_list = self.union_doc_list()
        cosine_scores = cosine_scoring.get_cosine_score(self.inv_ind, self.wildcard_index, self.query_terms, doc_list)
        result = self.return_documents(cosine_scores)
        return result
            
