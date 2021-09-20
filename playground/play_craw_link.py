import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

# postfix that should be trim and ignore
ignore_postfix = {"index.html", "index.htm", "index.jsp", "main.html"}

# file_end that should not be parse
blacklist_url_fileend = {"jpg", "pdf"}

# content in the url that should not be parse
blacklist_url_content = {"cgi"}

pages_visit = set()

def parse_link(src):
  url_o = urlparse(src)
  str_html = requests.get(src)
  
  soup = BeautifulSoup(str_html.text,'lxml')
  hrefs_o = soup.select('a[href]')

  site_url = url_o.hostname
  download_time = str_html.elapsed
  
  for href_o in hrefs_o:
    new_url = urljoin(url_o.geturl(), str(href_o["href"]))
    if check_url_content(new_url) and check_url_file_end(new_url):
      # f1.write(new_url+"\n")
      print("add")

  # f1.close()
  # print((cnt1, cnt2))

def trim_url_end(url):
  pass

def check_url_file_end(url):
  return url.split(".")[-1] not in blacklist_url_fileend

def check_url_content(url):
  for content in url.split("/"):
    if content in blacklist_url_content:
      return False
  return True

# test
# # base_path = os.path.abspath("playground/output")
# # f1 = open(base_path+"/a-href.txt", "w")
link = "https://en.wikipedia.org/wiki/Dog"
parse_link(link)