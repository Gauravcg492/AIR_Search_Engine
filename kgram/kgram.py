import nltk
import bisect

class Kgram:
    # Initializes the class with inverted index
    def __init__(self, inv_index):
        self.inv_ind = inv_index
        self.generate_kgram_inv_index()
    
    # Function to generate K-Gram Index from Inverted Index
    # Output {'kgram' : [term1, term2]}
    def generate_kgram_inv_index(self):
        kgram_ind = {}
        for term in self.inv_ind.keys():
            # add unigrams
            unigrams = list(term)
            for unigram in unigrams:
                if unigram not in kgram_ind:
                    kgram_ind[unigram] = []
                # Check if term is already added for this unigram
                ind = bisect.bisect_left(kgram_ind[unigram], term) 
                if ind == len(kgram_ind[unigram]) or kgram_ind[unigram][ind] != term:
                    # Add term in the right position
                    bisect.insort(kgram_ind[unigram], term)
            # add bigrams
            bigrams = list(nltk.bigrams(term))
            for bigram in bigrams:
                bi = ''.join(bigram)
                if bi not in kgram_ind:
                    kgram_ind[bi] = []
                # Check if term is already added for this bigram
                ind = bisect.bisect_left(kgram_ind[bi], term)
                if ind == len(kgram_ind[bi][ind]) or kgram_ind[unigram][ind] != term:
                    # Add term in the right position
                    bisect.insort(kgram_ind[bi], term)
        self.kgram_ind = kgram_ind
    
    # Function for getting kgram entries of the query_term provided
    # Input query_term Ex: 'apple'
    # Output dictionary of  kgram entries Ex: {'a':[term1, term2], 'ap': [term2, term3]}
    def get_kgram_query(self, query_term, get_unigram=True):
        kgram_query = {}
        if get_unigram:
            unigrams = list(query_term)
            for unigram in unigrams:
                if unigram not in kgram_query:
                    if unigram in self.kgram_ind:
                        kgram_query[unigram] = self.kgram_ind[unigram].copy()
                    else:
                        kgram_query[unigram] = []
        
        bigrams = list(nltk.bigrams(query_term))
        for bigram in bigrams:
            bi = ''.join(bigram)
            if bi not in kgram_query:
                if bi in self.kgram_ind:
                    kgram_query[bi] = self.kgram_ind[bi].copy()
                else:
                    kgram_query[bi] = []
        return kgram_query
