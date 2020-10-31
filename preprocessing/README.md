# Preprocessing 
- For compatibility with Elastic Search, we convert the [multiple csv files](https://www.kaggle.com/amritvirsinghx/environmental-news-nlp-dataset) to a single json file.
- First create a folder to store the converted files ```mkdir TelevisionNewsJSON ```
- Run ```python3 csv-to-json.py``` to convert multiple csv to json files
- Run ```merge_jsons.py``` to merge the multiple jsons into a single file ```final.json```
