import urllib.robotparser

url = "http://www.musi-cal.com/"
url_o = urlparse
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()