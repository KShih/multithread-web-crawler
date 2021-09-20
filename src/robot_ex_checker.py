from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import urllib.error
import constant

class RobotExChecker:
  def __init__(self):
    self.robot_cached = {}

  def can_parse(self, url):
    url_obj = urlparse(url)
    robot_url = self._get_robot_url(url_obj)
    request_url = url_obj.geturl()
    if robot_url not in self.robot_cached:
      rp = RobotFileParser()
      rp.set_url(robot_url)
      try:
        rp.read() # TODO(better): default timeout is 60s, maybe too long
      except Exception as exception:
        if type(exception) not in {urllib.error.URLError, UnicodeDecodeError}:
          print(constant.WARNING_EXCEPTION_NOT_RECOGNIZED, exception)
          # TODO: better dealing strategy
        return True 
      self.robot_cached[robot_url] = rp
    return self.robot_cached[robot_url].can_fetch("*", request_url)

  def _get_robot_url(self, url_obj):
    return url_obj.scheme + "://" + url_obj.netloc + "/robots.txt"
