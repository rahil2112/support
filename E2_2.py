print('\n1. Lowercasing\n')
import pandas as pd
df=pd.read_csv('YouTube_Comments_Sentiment.csv')
print(df.head())
df['Comments']=df['Comments'].str.lower()
print(df.head())

print('\n2. Tokenization\n')
import nltk
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize

df['Comments']=df['Comments'].apply(lambda X: word_tokenize(X))
print(df.head())

print('\n3. Stopwords\n')
import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords
print(stopwords.words('english'))

def remove_stopwords(Comments):
    words = Comments.split()
    clean_words = [word for word in words if word.lower() not in stopwords.words('english')]
    clean_text = ' '.join(clean_words)
    return clean_text

print(df.head())

print('\n4. Remove Punctuation\n')
from nltk.tokenize import RegexpTokenizer

def remove_punct(text):
    tokenizer = RegexpTokenizer(r"\w+")
    lst=tokenizer.tokenize(' '.join(text))
    return lst

df['Comments'] = df['Comments'].apply(remove_punct)
print(df.head())
