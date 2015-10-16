#! /usr/bin/env python

from lxml import html
from twython import Twython
from io import BytesIO
import random, requests


APP_KEY = xxxxxxx
APP_SECRET = xxxxxxx
OAUTH_TOKEN = xxxxxxx
OAUTH_TOKEN_SECRET = xxxxxxx

api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_followers():
    """
    Automatically follows all new followers, and sends them a welcome message.
    """
    following = api.get_friends_ids(screen_name='endangeredbot')
    followers = api.get_followers_ids(screen_name='endangeredbot')

    not_following_back = []
    
    for f in followers['ids']:
        if f not in following['ids']:
                not_following_back.append(f)

    print not_following_back    

    for follower_id in not_following_back:
        try:
            api.create_friendship(user_id=follower_id)
            user = api.show_user(user_id=follower_id)
            api.update_status(status= '@' + user.get_screen_name() + ' Thanks for following. For more visit www.iucnredlist.org or www.arkive.org.')
        except Exception as e:
            print("error: %s" % (str(e)))
    
def post_update():
    """
    Posts status message to Twitter.
    """
    try:
        new_status = create_status()
        api.update_status_with_media(status=new_status['status'], media=BytesIO(new_status['image']))
    except Exception as e:
        print("error: %s" % (str(e)))
    #print create_status()

def create_status():
    """
    Grabs a random page from arkive.org, parses for species name, image and link.
    """
    page = requests.get('http://www.arkive.org/random-species')
    tree = html.fromstring(page.text)
    species_name = unicode(tree.xpath('//h1[@id="speciesName"]/text()')[0], 'utf-8')
    page_url = tree.xpath('//meta[@name="DC.Identifier"]/@content')
    image_url = tree.xpath('//span[@id="picture-large"]/@data-src')
    image = requests.get(url=image_url[0]).content
    status = str(species_name) + " " + str(page_url[0])
    return {'status':status, 'image':image}

def start():
    """
    Starts the program.
    """
    post_update()
    get_followers()
    
start()
