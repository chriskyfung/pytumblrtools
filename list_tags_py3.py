# -*- coding: utf-8 -*-
#
# A python script to list and count all tags within a Tumblr blog,
# and export the data as a CSV file to local storage.
#
# Created on Oct 7, 2019; Updated on Oct 9, 2019
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
    return  all_posts

# Count and sort the number of tags, 
# args:
#     posts
#     DESC : True, for descending order
# return:
#     [(tag1, count1), (tag2, count2), ...]
def sortTagsByFeq(posts, DESC):
    tagDict = {}
    for post in posts:
        tags = post['tags']
        for tag in tags:
            if tag in tagDict:
                tagDict[tag] += 1
            else:
                tagDict[tag] = 1
    return sorted(tagDict.items(), key=lambda items: items[1], reverse=DESC)

# Save sortedTags data as a CSV file
# args:
#     from_blog : prefix of the output filename
#     tags: [(tag1, count1), (tag2, count2), ...]
# return:
#     filename : <from_blog> + '_tag_count.csv'
def writeTags2CSV(from_blog, tags):
    filename = from_blog + '_tag_count.csv'
    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(['tags', 'num of post'])
        for tag in tags:
            writer.writerow(tag)
            f.flush()
    return filename

all_posts = export_posts(CLIENT, BLOG)
sortedTags = sortTagsByFeq(all_posts, True)
writeTags2CSV(BLOG, sortedTags)