import argparse
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
 
argParser = argparse.ArgumentParser()
argParser.add_argument("website", choices=['https://www.britannica.com', 'https://www.wikipedia.org'], default='https://www.wikipedia.org', help="write the website to search (e.g. https://www.google.com)")
argParser.add_argument("searchword", help="write your web searchword here")
args = argParser.parse_args()
website = args.website
usrSearch = args.searchword

# detects any occurrences of the special characters in the searchword: 
if (len(set(usrSearch) & set(',;.:-_*^<>|!"@#£¤$%/{([)]=}?+\´`±§½$"')) > 0):
    raise ValueError("My Error: searchword contains special characters!")

# Fetch html doc:
# IMPORTANT: the url definition is vulnerable to malicious injection
# because the string is appended directly with user inputs!
if (website == 'https://www.britannica.com'):
    url = website + "/search?query=" + usrSearch
elif (website == 'https://www.wikipedia.org'):
    url = website + "/wiki/" + usrSearch
else:
    raise ValueError("My Error: invalid website input!")
print(f"Target URL:\n{url}")

#r = requests.get(url, timeout=30)
#r.raise_for_status()

# Since the Content-Type is text/html we can use the attribute text to
# display the HTML in the body. We can review the first 100 characters:
#html = r.text

# Parse downloaded html doc
#soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

#print(f"Response type: {r.headers['Content-Type']}")
#print(f"Status code: {r.status_code}")

# Error: Enable JavaScript and cookies to continue

# Plan B: Try using Selenium or Scrapy.
