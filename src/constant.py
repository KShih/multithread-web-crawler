OUTPUT_FILE_NAME = "crawler_log.txt"

## Other package
GOOGLE_SEARCH_FREQ = 1.0
BEAUTIFUL_SOUP_PARSING_TYPE = 'lxml'
BEAUTIFUL_SOUP_SELECCT_TERM = 'a[href]'
REQUEST_TIMEOUT = 5

## Error msg
ERROR_SETTING_IMCOMPLETE = "[Critical] one of the important setting is not set. Please check all the set function and try again."
ERROR_OUTPUT_FILEPATH_NOT_FOUND = "[Critical] cannot find output file path: "

## Warning msg
WARNING_EXCEPTION_NOT_RECOGNIZED = "[Warning] unrecognized exception in robot_ex module: "

## Crawler blacklist
# postfix that should be trim and ignore
ignore_postfix = {"index.html", "index.htm", "index.jsp", "main.html"}

# file_end that should not be parse
blacklist_url_fileend = {"jpg", "pdf"}

# content in the url that should not be parse
blacklist_url_content = {"cgi"}

# acceptable url schemes
acceptable_url_scheme = {"http", "https"}