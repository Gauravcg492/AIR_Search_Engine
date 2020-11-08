import nltk
import csv
import string
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()

stop_words = stopwords.words('english').copy()
stop_words.extend(["'re", "n't"])
pos_counter = 0

dataset = "../../dataset/TelevisionNews/"
outfile = open("../../temp-data/term_doc_id_pos", "w") #intermediate

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
	token = token.lower() #convert to lowercase for uniformity
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
	return token

def driver():
	n = 0
	count= 0
	for file in os.listdir(dataset):
		# if(count==2):
		# 	break
		# count+=1
		n+=1
		row_no = -1
		zones=[] #URL, snippet...
		with open(dataset+file) as csv_file:
			print(n, "/418 files done")
			csv_reader = csv.reader(csv_file, delimiter=',')

			for row in csv_reader:
				row_no+=1
				if(row_no==0):
					zones = row[1:]
					continue
				else:
					curr_doc_id = file.strip('.csv')+ "_"+str(row_no)
					curr_doc_url= row.pop(0)
					for el in row:
						reset_pos()
						col_no = row.index(el)
						if(col_no==4):
							#print(el)
							# we won't be tokenizing "IAPreviewThumb" entries
							tokens = [el]
						else:
							tokens = nltk.word_tokenize(el)
						for token in tokens:
							token = normalize(token)
							if(token ==''):
								continue
							outfile.write(token +","+ str(curr_doc_id) + "," + str(pos_counter) + "," + zones[col_no].lower() + "\n")
							increment_pos()


if __name__ == "__main__": 
	driver()



