# npm run build; npm run dev

import numpy as np 
import sys
# import urllib.request as libreq
# hrefurl = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=2'
# with libreq.urlopen(hrefurl) as url:
#     r = url.read()
# # print(r)

import feedparser
hrefurl = "http://rss.arxiv.org/atom/astro-ph"
feed = feedparser.parse(hrefurl)

# print(feed, "\n\n")
# print(feed['feed'], "\n\n")
nentries = len(feed['entries'])
rando = np.random.randint(4)
for i in range(1):
    # print(feed['entries'][i]['link'])
    # print(f"THIS IS ANOTHER TEST BUT BETTER???")
    # print(feed['entries'][i]['title'])
    # print(feed['entries'][i]['author'], "\n\n")
    print(f"new on astro-ph: {feed['entries'][i]['title']} by {feed['entries'][i]['author']}; {feed['entries'][i]['link']}")

# print(nentries)
# print(dataToSendBack)
sys.stdout.flush()
