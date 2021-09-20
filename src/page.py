from urllib.parse import urlparse

class Page:
  def __init__(self, url, depth):
    self.novel_score = None
    self.importance_score = 1.0
    self.total_score = None

    url_o = urlparse(url)
    self.url = url_o.geturl()
    self.domain = url_o.scheme + "://" + url_o.hostname
    self.size = None
    self.depth = depth
    self.download_time = None

  def __lt__(self, other):
    return self.total_score < other.total_score

  def set_download_time(self, time):
    self.download_time = time
  
  def set_page_size(self, page_size):
    self.size = page_size

  def update_importance_score(self):
    self.importance_score += 1.0
    self.update_total_score()

  def update_novel_score(self, domain_cnt):
    self.novel_score = 1 / domain_cnt
    self.update_total_score()

  def update_total_score(self):
    self.total_score = - (self.novel_score + self.importance_score) # make minHeap works as maxHeap
