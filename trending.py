from bs4 import BeautifulSoup
import requests
page = requests.get("https://github.com/trending/python?since=monthly")
soup = BeautifulSoup(page.content, 'html.parser')
repos_html = soup.select("ol.repo-list li")
for repo in repos_html:
    repo_link = repo.find('h3').find('a').attrs['href']
    description = repo.select('div.py-1 p')[0].text.strip()
    tab_width = int(round((40 - len(repo_link))/8.0 + .49))
    print('{}{}{}'.format(repo_link, ('\t'*tab_width), description[:120]))
