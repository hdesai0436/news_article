import nltk
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds
stop_words = nltk.corpus.stopwords.words('english')

class Text_Summary:
    def ___init__():
        pass
    
    def sent_token(self,data):
        sentences = nltk.sent_tokenize(data)
        return sentences


    def normalize_document(self, doc):
        # lower case and remove special characters\whitespaces
        doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
        doc = doc.lower()
        doc = doc.strip()
        # tokenize document
        tokens = nltk.word_tokenize(doc)
        # filter stopwords out of document
        filtered_tokens = [token for token in tokens if token not in stop_words]
        # re-create document from filtered tokens
        doc = ' '.join(filtered_tokens)
        return doc

    def normalization(self,sent_token):
        normalize_corpus = np.vectorize(self.normalize_document)
        norm_sentences = normalize_corpus(sent_token)
        return norm_sentences

    def text_representation(self,norm_sentences):
        tv = TfidfVectorizer(min_df=0., max_df=1., use_idf=True)
        dt_matrix = tv.fit_transform(norm_sentences)
        dt_matrix = dt_matrix.toarray()
        td_matrix = dt_matrix.T
        return td_matrix
    
    def low_rank_svd(self,matrix, singular_count=2):
        u, s, vt = svds(matrix, k=singular_count)
        return u, s, vt
    
    def text_summary(self,data):
        
        sentences = self.sent_token(data)
        normalization = self.normalization(sentences)
        text_representation = self.text_representation(normalization)

        u, s, vt = self.low_rank_svd(text_representation, singular_count=3)  

        term_topic_mat, singular_values, topic_document_mat = u, s, vt

        # remove singular values below threshold                                         
        sv_threshold = 0.5
        min_sigma_value = max(singular_values) * sv_threshold
        singular_values[singular_values < min_sigma_value] = 0

        salience_scores = np.sqrt(np.dot(np.square(singular_values), 
                                        np.square(topic_document_mat)))


        top_sentence_indices = (-salience_scores).argsort()[:8]
        top_sentence_indices.sort()
        return ' '.join(np.array(sentences)[top_sentence_indices])

    


    
    
    



    
    
    
    






    