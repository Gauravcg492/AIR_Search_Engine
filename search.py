import nltk
import string
from nltk.corpus import stopwords
# import lemmatize, tokenize and inverted_index_generator
from kgram import Kgram
from cosine_scoring import cosine_scoring

class search:
    def __init__(self):
        # for preprocessing data
        self.inv_ind = {}
        # self.inv_ind = generate_inv_index()
        # pass inv_ind to kgram
        # self.kgram = Kgram(self.inv_ind)
        pass

    def search(self, query_text):
        query_terms = []
        position = 0
        do_correction = False
        for term in nltk.word_tokenize(query_text):
            term.replace('-', '')
            if term == '' or term == "'s" or (str(term) in string.punctuation):
                continue
            # TODO have a discussion regarding counting position of stopwords in inverted index
            if (str(term) in stopwords.words('english')):
                # removing stop words but retaining their position
                position += 1
                continue
            # term = lemmatize(term)
            if term not in self.inv_ind:
                do_correction = True
            query_terms.append(term)
        query = ' '.join(query_terms)
