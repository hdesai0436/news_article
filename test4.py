import pandas as pd
import sqlite3
import sqlalchemy as db
from sqlalchemy import create_engine
from website .models import News
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import *
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics import pairwise_distances
import numpy as np
import gensim
from gensim.utils import simple_preprocess
from sklearn.preprocessing import OneHotEncoder 
stop_words = set(stopwords.words('english'))

db_uri="C:/Users/hardi/Documents/news/instance/database.db"
cnx = sqlite3.connect(db_uri)

news_df = pd.read_sql_query(
    "SELECT * FROM News",
    cnx
)

category = pd.read_sql_query(
    "SELECT * FROM Category",
    cnx
)



news_df.to_csv('data_new.csv',index=False)
category.to_csv('data_category.csv',index=False)

# tokenizer=ToktokTokenizer()
# #Setting English stopwords
# stopword_list=nltk.corpus.stopwords.words('english')


# df = pd.read_csv('data.csv')


# df1 = pd.read_csv('data_new.csv')
# df2 = pd.read_csv('data_category.csv')

# df2.drop('id',inplace=True,axis=1)


# df3 = pd.merge(df1, df2, left_on='id', right_on='new_id')

# df3.to_csv('final.csv', index=False)

# news_articles_temp = df3.copy()


# for i in range(len(news_articles_temp["content"])):
#     string = ""
#     for word in news_articles_temp["content"][i].split():
#         word = ("".join(e for e in word if e.isalnum()))
#         word = word.lower()
#         if not word in stop_words:
#           string += word + " "  
#     if(i%1000==0):
#       print(i)           # To track number of records processed
#     news_articles_temp.at[i,"content"] = string.strip()

# lemmatizer = WordNetLemmatizer()

# for i in range(len(news_articles_temp["content"])):
#     string = ""
#     for w in word_tokenize(news_articles_temp["content"][i]):
#         string += lemmatizer.lemmatize(w,pos = "v") + " "
#     news_articles_temp.at[i, "content"] = string.strip()
#     if(i%1000==0):
#         print(i)    


# words=[]
# for sent in news_articles_temp["content"]:
#     sent_token=sent_tokenize(sent)
#     for sent in sent_token:
#         words.append(simple_preprocess(sent))

# model=gensim.models.Word2Vec(words,window=5,min_count=2)

# model.build_vocab(words)

# def document_vector(doc):
#     # remove out-of-vocabulary words
#     doc = [word for word in doc if word in model.wv.index_to_key]
#     return np.mean(model.wv[doc], axis=0)

# X=[]
# for i in range(len(words)):
#     print("Hello",i)
#     X.append(document_vector(words[i]))

# X = np.array(X)
# X= np.load('data.npy')
# category_onehot_encoded = OneHotEncoder().fit_transform(np.array(news_articles_temp["category_title"]).reshape(-1,1))

# def avg_w2v_with_category(row_index, num_similar_items, w1,w2): #headline_preference = True, category_preference = False):
#     w2v_dist  = pairwise_distances(X, X[row_index].reshape(1,-1))
#     category_dist = pairwise_distances(category_onehot_encoded, category_onehot_encoded[row_index]) + 1
#     weighted_couple_dist   = (w1 * w2v_dist +  w2 * category_dist)/float(w1 + w2)
#     indices = np.argsort(weighted_couple_dist.flatten())[0:num_similar_items].tolist()
#     return df1['title'][indices][1:].values



