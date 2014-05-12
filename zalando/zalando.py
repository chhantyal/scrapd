#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

BASE_URL = 'http://www.zalando.de'


def get_category(path):
    """
    Returns dict of articles for a particular category from a zalando.de with given path.
    """
    url = '{base_url}/{path}'.format(base_url=BASE_URL, path=path)
    r = requests.get(url=url)
    assert r.status_code == 200
    soup = BeautifulSoup(r.content)
    all_articles = soup.find('ul', class_='catalog').find_all('a', class_='productBox')

    articles_list = []

    for article in all_articles:
        article_dict = {}
        article_dict['brand'] = article.find('b').text
        article_dict['name'] = article.find('em').text
        article_dict['price'] = article.find('span', class_='price').text
        articles_list.append(article_dict)
    category_dict = {'name': path, 'url': url, 'articles': articles_list}
    return category_dict