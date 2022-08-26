from .models import Articles
from .models import Sources
from newsapi import NewsApiClient
from .config import Config
import urllib.request, json
from app import Post, db

api_key = None
base_url = None
base_url_for_everything = None
base_url_top_headlines = None
base_source_list = None


def publishedArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    get_articles = newsapi.get_everything(
        sources='cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = get_articles['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())
        contents = zip(source, title, desc, author, img, p_date, url, post_id)
    return contents


def topHeadlines():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    top_headlines = newsapi.get_top_headlines(
        sources='cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_headlines = top_headlines['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_headlines) // 3):
        headline = all_headlines[i]

        source.append(headline['source'])
        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        Post.query.filter_by(url=headline['url']).delete()
        post = Post(url=headline['url'],
                    source=headline['source']['name'],
                    title=headline['title'],
                    description=headline['description'],
                    author=headline['author'],
                    urlToImage=headline['urlToImage'],
                    publishedAt=headline['publishedAt'],
                    content=headline['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=headline['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def randomArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    random_articles = newsapi.get_everything(sources='the-verge, gizmodo, the-next-web, recode, ars-technica')

    all_articles = random_articles['articles']

    articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def businessArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    business_articles = newsapi.get_top_headlines(category='business')

    all_articles = business_articles['articles']

    business_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        business_articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def techArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    tech_articles = newsapi.get_top_headlines(category='technology')

    all_articles = tech_articles['articles']

    tech_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        tech_articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def entArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    ent_articles = newsapi.get_top_headlines(category='entertainment')

    all_articles = ent_articles['articles']

    ent_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        ent_articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def scienceArticles():
    newsapi = NewsApiClient(api_key=Config.API_KEY)

    science_articles = newsapi.get_top_headlines(category='science')

    all_articles = science_articles['articles']

    science_articles_results = []

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    post_id = []

    for i in range(len(all_articles) // 3):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        science_articles_results.append(article_object)

        Post.query.filter_by(url=article['url']).delete()
        post = Post(url=article['url'],
                    source=article['source']['name'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    urlToImage=article['urlToImage'],
                    publishedAt=article['publishedAt'],
                    content=article['content'])
        db.session.add(post)
        db.session.commit()
        first_post = Post.query.filter_by(url=article['url']).first()
        post_id.append(first_post.get_id())

        contents = zip(source, title, desc, author, img, p_date, url, post_id)

    return contents


def get_news_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_source_url = 'https://newsapi.org/v2/sources?apiKey=' + Config.API_KEY
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_sources(news_source_results_list)

    return news_source_results


def process_sources(source_list):
    '''
    function that process the news articles and transform them to a list of objects
    '''
    news_source_result = []
    for news_source_item in source_list:
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')

        if name:
            news_source_object = Sources(name, description, url)
            news_source_result.append(news_source_object)
    return news_source_result
