import pandas as pd 
import snscrape.modules.twitter as snstwitter 
from google.colab import files 
import os 
os.system("snscrape --jsonl --max-results 5000 --since 2023-01-31 twitter-search 'Budget 2023 until:2023-02-07' > output.json") 
tweets_df = pd.read_json('output.json', lines=True) 
tweets_df.to_csv() 
# Save the file to the Colab environment 
tweets_df.to_csv('output.csv', index=False) 

# Download the file to your local machine 
files.download('output.csv') 
