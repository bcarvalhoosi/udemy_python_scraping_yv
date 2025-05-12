import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = []
links = []
scores = []

# Find all news items
news_items = soup.select("tr.athing")
for item in news_items:
    # Find the title and score tags
    title_tag = item.select_one(".titleline a")
    score_tag = item.find_next_sibling("tr").select_one(".score")
    # Check if the title and score tags exist
    if title_tag and score_tag:
        title = title_tag.getText()
        link = title_tag.get("href")
        score = score_tag.getText()
        titles.append(title)
        links.append(link)
        scores.append(int(score.split(" ")[0]))

# Find the index of the maximum score
max_score = scores.index(max(scores))
print(f"Title: {titles[max_score]}")
print(f"Link: {links[max_score]}")
print(f"Score: {scores[max_score]}")


























