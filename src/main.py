index = []
count = 0

def record_user_click(index,keyword,url): #This method is to count the number of times a user a particular website
    for items in index:
        if items[0] == keyword:
            for links in items[1]:
                if url == links[0]:
                    links[1] += 1 #i.e. links[1] =links[1] + 1 , 0 = 0 + 1

def add_to_index(index,keyword,url): #This method is to store the data pertaining a keyword and the lists of url's that contain the keyword.
    if len(index) == 0:
        index = index.append([keyword, [[url, count]]])
    elif len(index) != 0:
        for items in index:
            if items[0] == keyword:
                items[1].append([url, count])
        else:
            index = index.append([keyword, [[url, count]]])

def get_page(url): #This method is to crawl through different pages using a url
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''
    #These are the pages in HTML form which will later be converted into words using the method split_string()
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""


def union(a, b): #This method is to check whether a page has been crawled, if yes then it is stored in an object called crawled, if no then it is stored in an object called to_crawl
    for e in b:
        if e not in a:
            a.append(e)


def get_next_target(page): #This method gets access to different url's by crawling an entire page
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page): # This method is used to get all links that are present in a particular page
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed): #This method is used to crawl through different pages using a seed page
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


def lookup(index, keyword): # This method is used to check the number of keywords that are stored and the url's related to those keywords
    # IF keyword is present in the dictionary as a key then return the values i.e. url's related to that keyword
    for items in index:
        if items[0] == keyword:
            return items[1]
    return []
#>>> ['http://udacity.com','http://npr.org']
# I have to learn to operate with lists and strings as well


def add_page_to_index(index,url,content):
    content = content.split()
    for word in content:
        add_to_index(index, word, url)


def split_string(source, splitlist): # This method is used to remove all the symbols that are present in the HTML pages.
    if splitlist == ',':
        return source.split(",") #This part if for the cases where there no other punctuation marks except ','.
    else:
        for item in splitlist:  #And this part is for any punctuation marks that are present between strings.
            for i in range(len(source)):
                find_pos = source.find(item)
                if find_pos != -1:
                    source = source.replace(item, " ")
        return source.split()


#Here is an example showing a sequence of interactions:
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print(lookup(index, 'good'))

record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print(lookup(index, 'good'))
