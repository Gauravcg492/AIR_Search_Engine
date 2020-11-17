# AIR_Search_Engine
Search Engine developed as part of Algorithm for Information Retrieval (UE17CS412) course.

# Steps:
Enter the directories in the order mentioned below and follow the commands in their README's
### 1. Construct inverted index:
 - If you want to generate inverted index from scratch [OPTIONAL]
 	- Download [Kaggle Dataset](https://www.kaggle.com/amritvirsinghx/environmental-news-nlp-dataset) and store it as per the directory structure in Notes
 	- ```cd AIR_Search_Engine/inverted-index```
 	- open the README and follow the instructions
 - Else, already generated inverted index can be downloaded from [here](https://drive.google.com/file/d/185c_fsIJvuBvvVWvKUgybYes_5xHkdQX/view?usp=sharing) 
 - Ensure that ```inv_index.json``` is outside the ```AIR_Search_Engine``` directory
 - This includes handling of stop words, lemmatization

### 2. Run Elastic Search
 - Follow 2. in Notes to setup Elastic Search and its indexing
 - You can skip this step if you do not wish to see metrics

### 3. Start the application:
 - ``` python3 api.py ```
 - wait until the "Done Indexing" message shows on your terminal

### 4. Pass the query
 - Open Postman and create a "GET" request with the URL ```127.0.0.1:8080?q=sunny+day```
 - Replace "sunny+day" with a query of your choice
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
- Edit the ```path``` in ```logstash.conf``` to the path where ```TelevisionNews``` is stored. 
- Move ```logstash.conf``` to ```/usr/share/logstash/bin ``` (directory where Logstash is installed)
- Run Elastic Search on a separate terminal ```./bin/elasticsearch``` (in the directory where Elastic Search is installed)
- In ```/usr/share/logstash/bin``` run ```sudo ./logstash -f logstash.conf```

