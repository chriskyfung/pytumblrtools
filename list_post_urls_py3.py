#
# A python script to list all post urls within a Tumblr blog,
# and export the data as a CSV file to local storage.
#
# Created on Oct 6, 2019; Updated on Oct 9, 2019
#
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

all_posts = export_posts(CLIENT, BLOG)

# print and save all post URLs as a CSV file
filename = BLOG + '_post_urls.csv'
with open(filename, 'w', encoding='utf-8', newline='\n') as f:
    writer = csv.writer(f)
    for post in all_posts:
        writer.writerow([post['post_url']])
        f.flush()
        print(post['post_url'])