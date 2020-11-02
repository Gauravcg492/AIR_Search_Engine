import nltk
import json
dataset = "../../dataset/final.json"
file = open("term_doc_id_pos", "w+")
count =0 
for line in open(dataset):
		if(count==3):
			break
		count+=1
		#print(line)
		record = json.loads(line)
		# can we assign a numeric doc id to each record
		# need to store doc-id => URL mapping 
		curr_doc_id = record["\ufeffURL"]
		del record["\ufeffURL"]
		for el in record.values():
			tokens= nltk.word_tokenize(el)
			for token in tokens:
				#print(tokens.index(token))
				file.write(token +","+ curr_doc_id + "," + str(tokens.index(token)) + "\n")
		