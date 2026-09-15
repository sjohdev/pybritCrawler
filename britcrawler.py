
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# user input: searchstring
usrString = 'Churchill'

# Fetch html doc: 
url = 'https://www.britannica.com/search?query=' + usrString
r = requests.get(url, timeout=30)
#r.raise_for_status()

# Since the Content-Type is text/html we can use the attribute text to
# display the HTML in the body. We can review the first 100 characters:
html = r.text

# Parse downloaded html doc
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

print(f"Response type: {r.headers['Content-Type']}")
print(f"Status code: {r.status_code}")

# Error: Enable JavaScript and cookies to continue

# Plan B: Try using Selenium or Scrapy.
