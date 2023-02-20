from flask import Blueprint,render_template
from . import db
from .models import News,Category
from news_recommendation.recommend import News_recommend
from text_preprocess.text_pre import Text_Preprocess
from extract_keywords.keywords import GetKeywords
from text_summary.summary import Text_Summary


views = Blueprint("views",__name__)

@views.route('/')
def home():
    try:
        # a = db.session.query(News).filter(News.id.in_([9,7,43,36,20,29]))
        # for i in a:
        #     print(i.title)
        sport = db.session.query(News, Category).join(Category).filter_by(category_title='sports')
        politics = db.session.query(News, Category).join(Category).filter_by(category_title='politics')
        business = db.session.query(News, Category).join(Category).filter_by(category_title='business')

        return render_template('home.html',sport=sport,politics=politics,business=business)
    except Exception as e:
        raise(e)

@views.route('/detail/<int:news_id>')
def article_detail(news_id):
    try:
        recommend = News_recommend()
        rec_news = recommend.avg_w2v_with_category(news_id,6,0.1,0.5)
        
        recommend = db.session.query(News).filter(News.id.in_(rec_news.tolist()))
    
        post = News.query.get_or_404(news_id)
        text_preprocess_text = Text_Preprocess()
        keywords = GetKeywords()
        summary = Text_Summary()

        clean_text = text_preprocess_text.text_preprocess(post.content)
        topic_keywords = keywords.get_tfidf_weighted_keyphrases(clean_text)

        article_summary = summary.text_summary(post.content)

        return render_template('detail.html',post=post,recommend=recommend,topic_keywords=topic_keywords,article_summary=article_summary)


    except Exception as e:
        raise(e)


