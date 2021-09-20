from googlesearch import search

key_word = "dog"
links = []
for link in search(key_word, stop=20, pause=1.0):
  links.append(link)
print(links)
            