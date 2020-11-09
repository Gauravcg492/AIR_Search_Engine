import json
import pandas as pd

def get_inv_index():
	f = open("../inv_index.json")
	inv_index = json.load(f)
	return inv_index

def get_record(doc_id):
	dataset = "../dataset/TelevisionNews/"
	filename, row_no =doc_id.split("_")
	df = pd.read_csv(dataset+filename+".csv")
	record = dict(df.iloc[int(row_no)])
	return (filename+".csv", row_no, record)



