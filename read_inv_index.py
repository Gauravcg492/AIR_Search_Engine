import json
import pandas as pd

def get_inv_index():
	f = open("../inv_index.json")
	inv_index = json.load(f)
	return inv_index

def get_record(doc_id, score):
	dataset = "../dataset/TelevisionNews/"
	filename, row_no =doc_id.split("_")
	df = pd.read_csv(dataset+filename+".csv")
	row_no = int(row_no)
	#print("in read_in_index")
	#print("doc id ", doc_id)
	#print("row no: ", row_no)
	real_row_no = row_no-1
	#print("real_row_no", real_row_no)
	#print("score ", score)
	record = dict(df.iloc[real_row_no])
	return (filename+".csv", row_no, score, record)



