from sklearn.preprocessing import OneHotEncoder 
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

class News_recommend:
    def __init__(self):
        pass

    def read_df(self):
        df = pd.read_csv('final.csv')
        return df
    
    def load_np_data(self):
        X= np.load('data.npy')
        return X
    
    def one_hot_encode(self):
        news_articles_temp = self.read_df()
        category_onehot_encoded = OneHotEncoder().fit_transform(np.array(news_articles_temp["category_title"]).reshape(-1,1))
        return category_onehot_encoded

    def avg_w2v_with_category(self, row_index, num_similar_items, w1,w2): #headline_preference = True, category_preference = False):
        news_articles_temp = self.read_df()
        X = self.load_np_data()
        category_onehot_encoded = self.one_hot_encode()
        w2v_dist  = pairwise_distances(X, X[row_index].reshape(1,-1))
        category_dist = pairwise_distances(category_onehot_encoded, category_onehot_encoded[row_index]) + 1
        weighted_couple_dist   = (w1 * w2v_dist +  w2 * category_dist)/float(w1 + w2)
        indices = np.argsort(weighted_couple_dist.flatten())[0:num_similar_items].tolist()
        return news_articles_temp['id'][indices][1:].values
    
    


    
