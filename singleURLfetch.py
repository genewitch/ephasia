foosite = 'http://www.gentoo.org'

import pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, foosite)
c.setopt(pycurl.HTTPHEADER, ["Accept:"])

import StringIO
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.perform()

from bs4 import BeautifulSoup

import redis

souper = BeautifulSoup(b.getvalue(), 'lxml')
'''for link in souper.find_all('a'):
    print(link.get('href'))'''

r = redis.Redis(host='localhost', port=6379, db=2)

for link in souper.find_all('a'):

        resolve = link.get('href')
        try:
                if resolve.partition('//')[1] == '':
                        if resolve.rfind('/') <= 1:
                                print ("bad http URL found", foosite, resolve)
                        else:
                                r.lpush(foosite, foosite + resolve)
                else:
                        r.lpush(foosite, resolve)
        except:
                print('error in resolve', foosite, resolve)
                break

print(r.lrange(foosite, 0, -1))
r.delete(foosite)
