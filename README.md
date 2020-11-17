# AIR_Search_Engine
Search Engine developed as part of Algorithm for Information Retrieval (UE17CS412) course.

# Steps:
### 1. Construct inverted index:
- Download [Kaggle Dataset](https://www.kaggle.com/amritvirsinghx/environmental-news-nlp-dataset) and store it as per the directory structure in Notes
- ```cd AIR_Search_Engine/inverted-index```
 	- open the README and follow the instructions
 - Ensure that ```inv_index.json``` is outside the ```AIR_Search_Engine``` directory
 - This includes handling of stop words, lemmatization

### 2. Run Elastic Search
 - Setup Elastic Search and Logstash as per the instructions in Notes
 - You can skip this step if you do not wish to see metrics

### 3. Start the application:
 - ``` python3 api.py ```
 - wait until the "Done Indexing" message shows on your terminal

### 4. Pass the query
 - Open Postman and create a "GET" request with the URL ```127.0.0.1:8080?q=sunny+day```
 - Replace "sunny+day" with a query of your choice. Replace " " with "+" in your query terms
 - Wildcard queries and spelling correction is also supported

# Dependencies
1. ```nltk```
2. ```flask ```

# Notes
### 1. Directory Structure
(for inverted index construction)
```
	Project
	|-- AIR_Search_Engine
	|-- temp-data
	|-- dataset
	    |-- TelevisionNews
```

### 2. Metrics calculation (setup instructions)
- To calculate precision and accuracy, our search engine uses Elastic Search as a benchmark. 
- To enable this feature you have to install [Elastic Search](https://www.elastic.co/downloads/elasticsearch) and [Logstash](https://www.elastic.co/downloads/logstash). 
- Open ```logstash.conf``` and edit the ```path``` variable to the path where ```TelevisionNews/``` is stored. 
- Move ```logstash.conf``` to ```/usr/share/logstash/bin ``` (directory where Logstash is installed)
- Run Elastic Search on a separate terminal ```./bin/elasticsearch``` (in the directory where Elastic Search is installed)
- Open another terminal and run ```cd /usr/share/logstash/bin && sudo ./logstash -f logstash.conf```
 - This only needs to be run the first time you setup this search engine

