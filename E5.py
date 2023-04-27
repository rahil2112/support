from textblob import TextBlob

def get_comment_sentiment(comment):
    analysis=TextBlob(comment)
    if analysis.sentiment.polarity>0:
        return "positive polarity"
    elif analysis.sentiment.polarity==0:
        return "Neutral polarity"
    else:
        return "negative"

comment_list=[]
sentiment_list=[]

for comment in comments:
    sentiment=get_comment_sentiment(comment)
    comment_list.append(comment)
    sentiment_list.append(sentiment)
    print(f"{comment}:{sentiment}")

import pandas as pd
dict = {'comments_list' : comment_list, 'Sentiments' : sentiment_list}
df = pd.DataFrame(dict)
df.to_csv('Comments Sentiments.csv')
df
df.to_csv("Data.csv")
