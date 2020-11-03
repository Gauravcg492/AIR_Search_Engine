import nltk
import json
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()

dataset = "../../dataset/final.json"
file = open("../../temp-data/term_doc_id_pos", "w") #intermediate
mapper = open("../doc_id_url_mappings", "w") #required globally
count = 0 
temp = 1

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize(token):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag([token])  
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, return word as is
            return word
        else:        
            #else use the tag to lemmatize the token
            lemmatized_word = lemmatizer.lemmatize(word, tag)
            return lemmatized_word

for line in open(dataset):
		# TEST COMMENT BEGINS HERE
		# if(count==3):
		# 	break
		# count+=1
		# TEST COMMENT ENDS HERE

		record = json.loads(line) 
		curr_doc_url = record["\ufeffURL"]
		curr_doc_id = temp
		mapper.write(str(curr_doc_id)+','+str(curr_doc_url)+'\n')
		del record["\ufeffURL"]
		for el in record.keys():
			pos_counter = 0
			value = record[el]
			tokens = nltk.word_tokenize(value)
			for token in tokens:
				# add code to ignore stop words here
				# handle pos_counter accordingly
				token=token.replace('-','')
				if(token=='' or token =="'s" or (str(token) in string.punctuation)):
					#ignoring punctuation tokens
					continue
				if (str(token) in stopwords.words('english')):
					# removing stop words but retaining their position
					pos_counter+=1
					continue
				token = lemmatize(token)
				file.write(token +","+ str(curr_doc_id) + "," + str(pos_counter) + "," + str(el) + "\n")
				pos_counter+=1

		temp+=1
		file.write("\n")

