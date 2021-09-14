from crawler import Crawler
from page import Page
from robot_ex_checker import RobotExChecker
import os

if __name__ == "__main__":
  crawler = Crawler()
  crawler.set_query_word("dog")
  crawler.set_seed_size(10)
  crawler.set_thread_pool_size(3)
  crawler.set_output_path(os.path.abspath("playground/output"))
  crawler.set_max_page(10000)

  try:
    crawler.run()
  except Exception as error:
    print('Catch error in run(): ' + repr(error))
