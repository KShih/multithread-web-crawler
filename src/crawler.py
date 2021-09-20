from googlesearch import search

import os
import heapq
from collections import defaultdict

import constant
from page import Page

class Crawler:
  def __init__(self):
    self.__url_page_map = dict()
    self.__domain_cnt_map = defaultdict(int)
    self.__pq = list()
    self.__thread_pool_size = None
    self.__query_word = None
    self.__seed_size = None
    self.__output_path = None
    self.__max_pages = None

  def set_seed_size(self, seed_size):
    self.__seed_size = seed_size

  def set_thread_pool_size(self, thread_pool_size):
    self.__thread_pool_size = thread_pool_size

  def set_query_word(self, query_word):
    self.__query_word = query_word

  def set_output_path(self, path):
    self.__output_path = os.path.join(path, constant.OUTPUT_FILE_NAME)

  def set_max_page(self, max_page):
    self.__max_pages = max_page

  def run(self):
    if not self.__seed_size or not self.__thread_pool_size or not self.__output_path or not self.__max_pages:
      raise ValueError(constant.ERROR_SETTING_IMCOMPLETE)

    pages = self.__get_seeds_page()
    self.__insert_seeds_page(pages)
    print("hi")

  def __get_seeds_page(self):
    pages = []
    for link in search(self.__query_word, stop=self.__seed_size, pause=constant.GOOGLE_SEARCH_FREQ):
      pages.append(Page(link, 0))
    return pages
  
  def __insert_seeds_page(self, pages):
    for page in pages:
      self.__url_page_map[page.url] = page
      self.__domain_cnt_map[page.domain] += 1
  def __check_url_scheme(self, url):
    return url.split(":")[0] in constant.acceptable_url_scheme

  def __check_url_file_end(self, url):
    return url.split(".")[-1] not in constant.blacklist_url_fileend

  def __check_url_content(self, url):
    for content in url.split("/"):
      if content in constant.blacklist_url_content:
        return False
    return True

