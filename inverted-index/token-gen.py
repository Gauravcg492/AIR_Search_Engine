import nltk
import json
dataset = "final.json"
file = open("term_doc_id_pos", "w")
mapper = open("mappings", "w")
count = 0 
temp = 1
for line in open(dataset):
		# if(count==3):
		# 	break
		# count+=1
		# print(line)
		record = json.loads(line)
		# can we assign a numeric doc id to each record
		# need to store doc-id => URL mapping 
		curr_doc_url = record["\ufeffURL"]
		curr_doc_id = temp
		mapper.write(str(curr_doc_id)+','+str(curr_doc_url)+'\n')
		del record["\ufeffURL"]
		# for el in record.values():
		for el in record.keys():
			pos_counter = 0
			value = record[el]
			tokens = nltk.word_tokenize(value)
			for token in tokens:
				#print(tokens.index(token))
				file.write(token +","+ str(curr_doc_id) + "," + str(pos_counter) + "," + str(el) + "\n")
				pos_counter+=1
				# file.write(token +","+ str(curr_doc_id) + "," + str(tokens.index(token)) + "," + str(el) + "\n")
		temp+=1
		file.write("\n")

# For reference, here is the post-processing result for record #1
# 12/27/2010,1,0,MatchDateTime
# 19:20:53,1,1,MatchDateTime
# MSNBC,1,0,Station
# News,1,0,Show
# Nation,1,1,Show
# MSNBC_20101227_190000_News_Nation,1,0,IAShowID
# https,1,0,IAPreviewThumb
# :,1,1,IAPreviewThumb
# //archive.org/download/MSNBC_20101227_190000_News_Nation/MSNBC_20101227_190000_News_Nation.thumbs/MSNBC_20101227_190000_News_Nation_001225.jpg,1,2,IAPreviewThumb
# to,1,0,Snippet
# blame,1,1,Snippet
# .,1,2,Snippet
# with,1,3,Snippet
# me,1,4,Snippet
# is,1,5,Snippet
# a,1,6,Snippet
# doctor,1,7,Snippet
# from,1,8,Snippet
# the,1,9,Snippet
# pew,1,10,Snippet
# center,1,11,Snippet
# on,1,12,Snippet
# global,1,13,Snippet
# climate,1,14,Snippet
# change,1,15,Snippet
# .,1,16,Snippet
# you,1,17,Snippet
# look,1,18,Snippet
# at,1,19,Snippet
# tennessee,1,20,Snippet
# and,1,21,Snippet
# the,1,22,Snippet
# wicked,1,23,Snippet
# flooding,1,24,Snippet
# they,1,25,Snippet
# had,1,26,Snippet
# there,1,27,Snippet
# .,1,28,Snippet
# this,1,29,Snippet
# has,1,30,Snippet
# been,1,31,Snippet
# --,1,32,Snippet
# or,1,33,Snippet
# the,1,34,Snippet
# global,1,35,Snippet
# warming,1,36,Snippet
# system,1,37,Snippet
# .,1,38,Snippet