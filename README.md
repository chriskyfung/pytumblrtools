Tumblr Quick Tools
===

A set of python scripts for manuplateing Tumblr blogs, which are inspired by [ubien/transfertumblr](https://github.com/ubien/transfertumblr).

### Require
- pytumblr library

### How to Use
- Fill in the **API keys** of your register application from https://api.tumblr.com/console/calls/post/reblog
- Replace the `Blog Name`

* * *

## Functions

### transfer_tumblr
- Transfer Tumblr posts to a new account

### list_post_urls
- List the urls of all blog posts, and export as a CSV file to local storage

### list_tags
- List all tags with counts, and export as a CSV file to local storage (Can use `SPECTAG` to specify only lookup the posts contain this given tag.)

### replacestr_in_allposts_py
- Replace a string in the body and caption of all text and photo