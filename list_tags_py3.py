# -*- coding: utf-8 -*-

__author__ = 'chris'
import pytumblr
import urllib.request
import os
import sys
from urllib.parse import urlparse
from os.path import splitext, basename

BLOG = 'YOUR_BLOG.tumblr.com'
CLIENT = pytumblr.TumblrRestClient(
    'CONSUMER_KEY',
    'CONSUMER_SECRET',
    'OAUTH_TOKEN',
    'OAUTH_SECRET'
)

#pytumblr doesn't handle unicode well, convert to string
def encode_to_html(uni_str):
    return uni_str.encode('ascii', 'xmlcharrefreplace')


def get_filename(url):
    disassembled = urlparse(url)
    filename, file_ext = splitext(basename(disassembled.path))
    return filename + file_ext


def export_posts(client, from_blog):
    more = True
    offset = 0
    all_posts = []
    while more:
        new_posts = client.posts(from_blog, offset=offset)['posts']
        new_posts_len = len(new_posts)
        if new_posts_len > 0:
            offset += new_posts_len
            all_posts = all_posts + new_posts
        else:
            more = False
    return all_posts

tagDict = {};
all_posts = export_posts(CLIENT, BLOG)
for post in all_posts:
    tags = post['tags']
    for tag in tags:
        if tag in tagDict:
            tagDict[tag] += 1
        else:
            tagDict[tag] = 1
print(sorted(tagDict.items(), key=lambda items: items[1], reverse=True))