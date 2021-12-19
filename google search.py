
# google search

from googlesearch import search

def get_urls(title):
      for i in search(title, stop = 10):
            print(i)


title = input()
get_urls(title)
