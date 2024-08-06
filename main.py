from bs4 import BeautifulSoup
import requests

url = "https://www.ratemyprofessors.com/professor/173343"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
comments_html = soup.find_all('div', {'class': 'Comments__StyledComments-dzzyvm-0 gRjWel'})
comments = [div.get_text(strip=True) for div in comments_html]

tags_html = soup.find_all('div', {'class': 'TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW'})
tags = []
for tag_div in tags_html:
    spans = tag_div.find_all('span', class_='Tag-bs9vf4-0 hHOVKF')
    for span in spans:
        tags.append(span.get_text(strip=True))

print(tags)
print(comments)