import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

def hack():
    url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'

    r = requests.get(url)
    print("Status code:", r.status_code)

    response_dict = r.json()
    #print(response_dictkeys())
    print(response_dict)

def hn_sub():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url) 
    print("Status code:", r.status_code)
# Processa informações sobre cada artigo submetido v submission_ids =
    submission_ids = r.json() 
    submission_dicts = []
    for submission_id in submission_ids[:2]: # Cria uma chamada de API
        url = ('https://hacker-news.firebaseio.com/v0/item/' +str(submission_id) + '.json') 
        submission_r = requests.get(url)
        print(submission_r.status_code) 
        response_dict = submission_r.json()
        submission_dict = {'title': response_dict['title'], 'link':'http://news.ycombinator.com/item?id=' + str(submission_id),'comments': response_dict.get('descendants', 0) }
        submission_dicts.append(submission_dict)
        submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)
    for submission_dict in submission_dicts: 
        print("\nTitle:",submission_dict['title']) 
        print("Discussion link:",submission_dict['link']) 
        print("Comments:", submission_dict['comments'])

hn_sub()