import urllib2
import cookielib
import re
import mechanize

USERNAME = "YourUserName"
PASSWORD = "YourPassword"
URL = "http://ashutoshanand.com/"
response = urllib2.urlopen('http://ashutoshanand.com/')
a = response.geturl()

if a != URL:
	browser = mechanize.Browser()
	browser.set_handle_robots(False) # This line to disable robots.txt
	browser.set_handle_refresh(False) # This line to enable HTTPS
	browser.open(a, timeout=5.0)
	print browser.title()
	browser.select_form(nr = 0)
	browser.form['username'] = USERNAME
	browser.form['password'] = PASSWORD
	browser.submit()
	print "Logged In at ", str(browser.geturl())
