import requests
import bs4

result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")

# TASK: Get the names of all the authors on the first page.
authors = set()

for text in soup.select(".author"):
    authors.add(text.text)

print(authors)

# TASK: Create a list of all the quotes on the first page.
quotes = []

for text in soup.select(".text"):
    quotes += [text.text]

print(quotes)

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text 
# shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
tags = []

for text in soup.select(".tag-item .tag"):
    tags += [text.text]

print(tags)

# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/.
# Use what you know about for loops and string concatenation to loop through all the pages and get all the 
# unique authors on the website.
there_is_next = True
count = 1
unique_authors = set()

while there_is_next:
    result = requests.get("http://quotes.toscrape.com/page/" + str(count))
    soup = bs4.BeautifulSoup(result.text, "lxml")

    for a in soup.select(".author"):
        unique_authors.add(a.text)

    count += 1
    if not soup.select(".next"):
        there_is_next = False

print(unique_authors)
