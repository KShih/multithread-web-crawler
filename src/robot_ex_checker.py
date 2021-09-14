from urllib.robotparser import RobotFileParser

class RobotExChecker:
  def __init__(self):
    self.cached = {}
    self.rp = RobotFileParser()

  def can_parse(self, url_obj):
    robot_url = self._get_robot_url(url_obj)
    request_url = url_obj.geturl()
    if request_url not in self.cached:
      self.rp.set_url(robot_url)
      self.rp.read()
      self.cached[request_url] = self.rp.can_fetch("*", request_url)
    return self.cached[request_url]
  
  def _get_robot_url(self, url_obj):
    return url_obj.scheme + "://" + url_obj.netloc + "/robots.txt"


if __name__ == "__main__":
  from urllib.parse import urlparse
  test1 = "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"
  test2 = "https://en.wikipedia.org/wiki/Dog"
  test3 = "http://www.musi-cal.com/wp-admin/search?city=San+Francisco"
  test1_o = urlparse(test1) # True
  test2_o = urlparse(test2) # True
  test3_o = urlparse(test3) # False

  rb = RobotExChecker()
  print(rb.can_parse(test1_o))
  print(rb.can_parse(test2_o))
  print(rb.can_parse(test3_o))
