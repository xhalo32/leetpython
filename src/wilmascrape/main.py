import cookielib
import urllib
import urllib2

# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
#opener.addheaders = []
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://wilma.espoo.fi'

# Input parameters we are going to send
payload = {
        "username":"kana",
        "password":"kissa"
  }

# Use urllib to encode the payload
data = urllib.urlencode(payload)

# Build our Request object (supplying 'data' makes it a POST)
req = urllib2.Request(authentication_url, data)

# Make the request and read the response
resp = urllib2.urlopen(req)

from bs4 import BeautifulSoup

soup=BeautifulSoup(resp,'html.parser')

print soup
