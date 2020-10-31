import pandas as pd
import csv
import json
import glob
import os

path = "TelevisionNews/"
path2 = "TelevisionNewsJSON/"

for file in os.listdir(path):
	jsonfile= path2 +  file.strip(".csv").replace(" ", "_")+".json"
	with open(path+file) as f:
		reader = csv.DictReader(f)
		rows = list(reader)

	with open(jsonfile, 'w') as f:
		json.dump(rows, f)
