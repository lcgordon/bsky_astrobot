# npm run build; npm run dev

import numpy as np 
import sys
import feedparser #https://feedparser.readthedocs.io/en/latest/common-atom-elements.html

print("MADE IT TO PYTHON")
hrefurl = "http://rss.arxiv.org/atom/astro-ph"
# hrefurl = "/Users/lindseygordon/Downloads/astro-ph"
feed = feedparser.parse(hrefurl)
nentries = len(feed['entries'])
print(nentries)
if nentries == 0:
    print("the arXiv RSS feed is down")
    sys.stdout.flush()
else: 
    # pull random entry until you get a viable skeet
    postable = False
    while postable == False: 
        i = np.random.randint(0, nentries)
        print(f"i = {i}")
        link = feed['entries'][i]['link']
        title = feed['entries'][i]['title']
        # trim long author list: 
        authorlist = feed['entries'][i]['author'].split(",")
        lenauthorlist = len(authorlist)
        # print(authorlist, lenauthorlist)
        # fix author list
        if lenauthorlist > 3: 
            authors = f"{authorlist[0]}+"
        else:
            authors = feed['entries'][i]['author']
        # generate initial skeet
        miniskeet = f"new on astro-ph:  by {authors}; {link}"
        if len(miniskeet) > 300: #if somehow still too big, continue on with a different paper
            continue
        
        skeet = f"new on astro-ph: {title} by {authors}; {link}"
        # if the skeet is too long, cut it down: 
        if len(skeet) >= 300: 
            # if title too long, cut it down
            miniskeet = f"new on astro-ph: {title} by {authors}; {feed['entries'][i]['link']}"
            counter = len(skeet) - len(miniskeet) # how many characters are left
            titlesplit = title.split(" ")
            print(titlesplit)
            title = ""
            # get the chunk that will fit: the first n words + n spaces that are smaller than counter
            titlelen = 0 
            h = 0
            while titlelen < (counter - 5): 
                titlelen += 1 + len(titlesplit[h])
                title += " " + titlesplit[h]
                h += 1

            title += "..."
        skeet = f"new on astro-ph: {title} by {authors}; {link}"
        postable = True


    # print(f"skeet length: {len(skeet)}")
    print(skeet)
    sys.stdout.flush()
