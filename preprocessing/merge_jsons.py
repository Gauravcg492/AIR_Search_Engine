import sys
import json
import glob
import os
import ndjson
path2 = "TelevisionNewsJSON/"

result = []
#add files to be merged in a new folder called "to_merge"
for file in os.listdir(path2):
	for line in open(path2+file):
		#print(line)
		line = json.loads(line)
		result.append(line)

outfile = open("final.json", "w")

json.dump(result, outfile)
outfile.close()