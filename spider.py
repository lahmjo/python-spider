import requests
import re
from bs4 import BeautifulSoup
#---------------------------------
link = 'http://www.github.com'
# headers = {}
# r = requests.get (link, headers = headers)
r = requests.get (link)
print (type(r))


print ("#------------------------------------------------")
print ("# This is the web content")
print ("#------------------------------------------------")
print ('web-encode: ', r.encoding)

print (r.text)


# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('h1', class_='post-title').a.text.strip ()
# print ("#------------------------------------------------")
# print ("# This is the title")
# print ("#------------------------------------------------")
# print (title)

with open ('spider.rpt', 'a+') as f:
    f.write (r.text)
    f.close

