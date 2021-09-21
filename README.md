# Multithread Web Crawler

- A web crawler which takes in a query word, and explore the internet by fetching all the urls in a fetched page by the order of the ranking function.

# Run
1. (optional) Create virtural environment
  - `virtualenv venv`
  - `.venv/bin/activate`
2. Install recuirements
  - `pip3 install -r requirements.txt`
3. Run the crawler by exmaple in main.py
  - `cd src; python3 main.py`

# Source code
1. main.py
  - the driver code to start the crawler
  - note: you must set all the params describing below
  - params:
    - `set_query_word(str)`
      - take the query word in string
    - `set_seed_size(int)`
      - take the amounts of seeds page in int
    - `set_thread_pool_size(int)`
      - take the amounts of threads in int
    - `set_output_path(str)`
      - take the folder name that the log go in string
    - `set_max_page(int)`
      - take the maximum of pages in int
    - `set_max_domain_cnt(int)`
      - take the numbers of the page to crawl from the same domain in int

2. crawler.py
  - the Crawler class which use for crawing the page

3. page.py
  - the Page class which contain relatead feature that the Crawler needs

4. robot_ex_checker.py
  - the robot exclusion class that deal with the robot exclusion

5. constant.py
  - the constant variable used in the programs, e.g.: `int request_timeout` 

# How it works

1. Take the query word and use the `googlesearch` to retrieve seeds page
2. Add the seeds page to priority queue (pq)
3. Start the multithread crawling process and run until crawled enough page
    a. Each idle thread will take the page that has the maximum scores from pq
    b. Update the total_score with the updated novel_score, and check if it’s still the best
    c. If yes go to step `d`, if not repeat `a` and `b`
    d. Crawling
        i. Retrieve the plain html
        ii. Parse the urls in this page, and deal with subpage by `urljoin`
        iii. Check if it’s a valid page by
            1. The postfix that should be ignore, e.g.: index.html, index.htm
            2. The blacklist of the file end, e.g.: jpg, pdf, mp3 ...etc.
            3. The blacklist of the subpage, e.g.: cgi
            4. The only acceptable html scheme e.g.: http, https
                1. Counter example: mailto, callto, javascript
        iv. Check if it’s not being visited before
            1. If yes go to step `v`
            2. If no, update the importance score
        v. Add page to pq by these steps
            1. Adding this url to visited
            2. Adding the count of this domain (use for calculate the novelty score)
            3. Adding this page to pq
    e. Write to the log file
        1. I put a TODO here since I think it would be more efficient to bulk write instead of writing the log page by page