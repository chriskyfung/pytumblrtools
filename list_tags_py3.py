# -*- coding: utf-8 -*-

__author__ = 'chris'
import pytumblr
import urllib.request
import os
import sys
import csv
from urllib.parse import urlparse
from os.path import splitext, basename

BLOG = 'YOUR_BLOG.tumblr.com'
CLIENT = pytumblr.TumblrRestClient(
    'CONSUMER_KEY',
    'CONSUMER_SECRET',
    'OAUTH_TOKEN',
    'OAUTH_SECRET'
)

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

tagDict = {}
all_posts = export_posts(CLIENT, BLOG)
for post in all_posts:
    tags = post['tags']
    for tag in tags:
        if tag in tagDict:
            tagDict[tag] += 1
        else:
            tagDict[tag] = 1
sortedTags = sorted(tagDict.items(), key=lambda items: items[1], reverse=True)
print(sortedTags)

with open(BLOG + '_tag_count.csv', 'w', encoding='utf-8', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(['tags', 'num of post'])
    for tag in sortedTags:
        writer.writerow(tag)
        f.flush()