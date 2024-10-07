import urllib2
from BeautifulSoup import BeautifulSoup

html_doc = urllib2.urlopen("http://www.gutorglyn.net/gutorglyn/poem/?poem-selection=006")

soup = BeautifulSoup(html_doc)
# title = title.renderContents()

# print(soup.getText(" "))
container_text = soup.find("div", { "class" : "container" })
container_words = BeautifulSoup(container_text)
print container_words