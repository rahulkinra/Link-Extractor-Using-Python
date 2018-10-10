import urllib.request #importing the request library

"""
Creating a function to read the url using request library.
Also decoding it to be easily useable.
"""
def get_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode()
            return html
    except Exception as e:
                return e

"""
Creating a function to extract the links from the recieved data.
"""

def get_next_target(s):
    start_link=s.find('<a href="htt')
    if start_link == -1:
        return None,0
    start_quote=s.find('"',start_link)
    end_quote=s.find('"',start_quote+1)
    url=s[start_quote+1:end_quote]
    return url,end_quote
"""
Creating a function to print the extracted links from the requested web page.
"""
def print_all_links(page):
    while True:
        url,endpos = get_next_target(page)
        if url:
            print (url)
            page=page[endpos:]
        else:
            break

print_all_links(get_page('https://en.wikipedia.org/wiki/Abraham_Lincoln'))

