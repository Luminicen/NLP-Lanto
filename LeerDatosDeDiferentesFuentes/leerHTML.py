#pip install bs4
import urllib.request as urllib2
from bs4 import BeautifulSoup
response = urllib2.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html_doc = response.read()
#Parsing
soup = BeautifulSoup(html_doc, 'html.parser')
# Formating the parsed html file
strhtm = soup.prettify()
# Print few lines
#print (strhtm[:1000])
print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)
#text print
for x in soup.find_all('p'): print(x.text)