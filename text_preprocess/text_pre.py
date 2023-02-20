from clean_text_data.clean_text import CleanText

class Text_Preprocess(CleanText):
    def __init__(self):
        super().__init__()

    

    def text_preprocess(self,corpus,remove_punctuation=True,remove_html_tag=True,remove_url=True, remove_emoji=True,
    remove_abb=True,remove_special_characters=True,remove_whitespace=True,remove_stopwords=True,
    lemmatizations=True,text_lower_case=True,sent_tokenizes=True):
        normized_corpus = []
       
        if remove_punctuation:
            corpus = self.remove_punctuations(corpus)
        if remove_html_tag:
            corpus = self.remove_html_tag(corpus)
        if remove_url:
            corpus = self.remove_url(corpus)
        if remove_emoji:
            corpus = self.remove_emoji(corpus)
        if remove_abb:
            corpus = self.remove_abb(corpus)
        if remove_special_characters:
            corpus = self.remove_special_characters(corpus)
        if remove_whitespace:
            corpus = self.remove_whitespace(corpus)
        if remove_stopwords:
            corpus = self.remove_stopwords(corpus)
        if lemmatizations:
            corpus = self.lemmatization(corpus)
           
        if sent_tokenizes:
            corpus = self.sent_tokenizes(corpus)
            
        return corpus

        