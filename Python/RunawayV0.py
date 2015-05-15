from bs4 import BeautifulSoup as BS
import urllib2
url ="mydomain.com"
usock = urllib2.urlopen(url)
data = usock.read()
usock.close()
soup = BS(data)
print soup.find('font', {'class':'big'}).text