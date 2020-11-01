import pandas as pd
import csv
import json
import glob
import os
import ndjson

#change as per system
path = "../../dataset/TelevisionNews/"
path2 = "../../dataset/TelevisionNewsJSON/"

for file in os.listdir(path):
	#creating name for (yet to be generated) JSON file
	jsonfile= path2 +  file.strip(".csv").replace(" ", "_")+".json"

	#reading contents of a single csv 
	with open(path+file) as f:
		reader = csv.DictReader(f)
		rows = list(reader)

	#dump into json
	with open(jsonfile, 'w') as f:
		ndjson.dump(rows, f)
