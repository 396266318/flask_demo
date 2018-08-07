import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    test = 00000

#     OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
#     ]


