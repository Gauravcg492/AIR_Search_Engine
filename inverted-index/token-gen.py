import nltk
import json
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()

stop_words = stopwords.words('english').copy()
stop_words.extend(["'re", "n't"])
pos_counter = 0

dataset = "../../dataset/final.json"
file = open("../../temp-data/term_doc_id_pos", "w") #intermediate
mapper = open("../doc_id_url_mappings", "w") #required globally

def increment_pos():
	global pos_counter
	pos_counter+=1

def reset_pos():
	global pos_counter
	pos_counter =0

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

def normalize(token):
	token=token.replace('-','')
	token=token.replace(',', '')
	if(token.startswith("'")):
		token=token[1:]
	if(token=="'s" or (str(token) in string.punctuation)):
		#ignoring punctuation tokens
		return ''
	if (str(token) in stop_words):
		# removing stop words but retaining their position
		increment_pos()
		return ''
	token = lemmatize(token) 
	token = token.lower() #convert to lowercase for uniformity
	return token

def driver():
	count = 0 
	temp = 1
	for line in open(dataset):
		# TEST COMMENT BEGINS HERE
		# if(count==100):
		# 	break
		# count+=1
		# TEST COMMENT ENDS HERE

		record = json.loads(line) 
		curr_doc_url = record["\ufeffURL"]
		curr_doc_id = temp
		mapper.write(str(curr_doc_id)+','+str(curr_doc_url)+'\n')
		del record["\ufeffURL"]
		for el in record.keys():
			reset_pos()
			value = record[el]
			if(el=="IAPreviewThumb"):
				tokens = [value]
			else:
				tokens = nltk.word_tokenize(value)
			for token in tokens:
				token = normalize(token)
				if(token ==''):
					continue
				file.write(token +","+ str(curr_doc_id) + "," + str(pos_counter) + "," + str(el).lower() + "\n")
				increment_pos()

		temp+=1
		#file.write("\n")

if __name__ == "__main__": 
	driver()



