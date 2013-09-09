import pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.gentoo.org")
c.setopt(pycurl.HTTPHEADER, ["Accept:"])
import StringIO
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.perform()
from bs4 import BeautifulSoup
import redis
souper = BeautifulSoup(b.getvalue())
'''for link in souper.find_all('a'):
    print(link.get('href'))'''
r = redis.Redis(host='localhost', port=6379, db=1)
for link in souper.find_all('a'):
        r.lpush('www.gentoo.org', link.get('href'))
