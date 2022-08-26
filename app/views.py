from app import app
from flask import render_template
from .request import businessArticles, entArticles, get_news_source, publishedArticles, randomArticles, \
    scienceArticles, techArticles, topHeadlines
from app import Post
import random
from flask import request


@app.route('/')
def home():
    articles = publishedArticles()
    return render_template('home.html', articles=articles)


@app.route('/post/<post_id>')
def post(post_id):
    cookie_nek = request.cookies.get('clixtz')
    if cookie_nek is not None:
        return render_template('bestads.html')
    else:
        post_obj = Post.query.filter_by(id=post_id).first()
        if post_obj is not None:
            post = post_obj.convert_to_dict()
        else:
            post_list = Post.query.all()
            post_o = random.choice(post_list)
            post = post_o.convert_to_dict()
        return render_template('post.html', post=post)


@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return render_template('headlines.html', headlines=headlines)


@app.route('/articles')
def articles():
    random = randomArticles()

    return render_template('articles.html', random=random)


@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return render_template('sources.html', newsSource=newsSource)


@app.route('/category/business')
def business():
    sources = businessArticles()

    return render_template('business.html', sources=sources)


@app.route('/category/tech')
def tech():
    sources = techArticles()

    return render_template('tech.html', sources=sources)


@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return render_template('entertainment.html', sources=sources)


@app.route('/category/science')
def science():
    sources = scienceArticles()

    return render_template('science.html', sources=sources)
