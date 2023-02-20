import itertools
from gensim import corpora, models
import nltk
stopwords = nltk.corpus.stopwords.words('english')
from operator import itemgetter

class GetKeywords():
    def __init__(self):
        pass

    def get_chunks(self, sentences, grammar = r'NP: {<DT>? <JJ>* <NN.*>+}', stopword_list=stopwords):
    
        all_chunks = []
        chunker = nltk.chunk.regexp.RegexpParser(grammar)
        
        for sentence in sentences:
            
            tagged_sents = [nltk.pos_tag(nltk.word_tokenize(sentence))]   
            
            chunks = [chunker.parse(tagged_sent) 
                        for tagged_sent in tagged_sents]
            
            wtc_sents = [nltk.chunk.tree2conlltags(chunk)
                            for chunk in chunks]    
            
            flattened_chunks = list(
                                itertools.chain.from_iterable(
                                    wtc_sent for wtc_sent in wtc_sents)
                            )
            
            valid_chunks_tagged = [(status, [wtc for wtc in chunk]) 
                                    for status, chunk 
                                        in itertools.groupby(flattened_chunks, 
                                                    lambda word_pos_chunk: word_pos_chunk[2] != 'O')]
            
            valid_chunks = [' '.join(word.lower() 
                                    for word, tag, chunk in wtc_group 
                                        if word.lower() not in stopword_list) 
                                            for status, wtc_group in valid_chunks_tagged
                                                if status]
                                                
            all_chunks.append(valid_chunks)
        
        return all_chunks




    def get_tfidf_weighted_keyphrases(self, sentences, 
                                    grammar=r'NP: {<DT>? <JJ>* <NN.*>+}',
                                    top_n=10):
        
        valid_chunks = self.get_chunks(sentences, grammar=grammar)
                                        
        dictionary = corpora.Dictionary(valid_chunks)
        corpus = [dictionary.doc2bow(chunk) for chunk in valid_chunks]
        
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        
        weighted_phrases = {dictionary.get(idx): value 
                            for doc in corpus_tfidf 
                                for idx, value in doc}
                                
        weighted_phrases = sorted(weighted_phrases.items(), 
                                key=itemgetter(1), reverse=True)
        weighted_phrases = [(term, round(wt, 3)) for term, wt in weighted_phrases]
        
        return weighted_phrases[:top_n]


