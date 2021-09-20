from crawler import Crawler
import os
import time

if __name__ == "__main__":
  crawler = Crawler()
  crawler.set_query_word("cats")
  crawler.set_seed_size(10)
  crawler.set_thread_pool_size(20)
  crawler.set_output_path("playground/output")
  crawler.set_max_page(100)

  start = time.time()
  try:
    crawler.run()
  except Exception as error:
    print('Catch error in run(): ' + repr(error))
  finally:
    crawler.stop()
  print(time.time() - start)