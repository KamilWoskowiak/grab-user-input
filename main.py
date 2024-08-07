from bs4 import BeautifulSoup
import requests

url = "https://www.ratemyprofessors.com/professor/173343"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
data_html = soup.find_all('div', {'class': 'Rating__RatingInfo-sc-1rhvpxz-3 kEVEoU'})

output = []

for entry in data_html:
    courses = entry.find_all('div', 'RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS')


# soup = BeautifulSoup(page.content, 'html.parser')
# comments_html = soup.find_all('div', {'class': 'Comments__StyledComments-dzzyvm-0 gRjWel'})
# comments = [div.get_text(strip=True) for div in comments_html]
# dates_html = soup.find_all('div', {'class': 'TimeStamp__StyledTimeStamp-sc-9q2r30-0 bXQmMr RatingHeader__RatingTimeStamp-sc-1dlkqw1-4 iwwYJD'})
# dates = [div.get_text(strip=True) for div in dates_html]
# wta_html = soup.find_all('div', {'class': 'MetaItem__StyledMetaItem-y0ixml-0 LXClX'})
# meta = []
# for tag_div in wta_html:
#     spans = tag_div.find_all('span')
#     for span in spans:
#         meta.append(span.get_text(strip=True))
#
# tags_html = soup.find_all('div', {'class': 'TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW'})
# tags = []
# for tag_div in tags_html:
#     spans = tag_div.find_all('span', class_='Tag-bs9vf4-0 hHOVKF')
#     for span in spans:
#         tags.append(span.get_text(strip=True))
#
# print(tags) # Top Tags
# print(comments) # Comments
# print(dates)
# print(meta)
# print(len(meta))
#
# return_dicts = []
# for i in range(len(comments)):
#     print(i)
#     temp = {
#         'comment': comments[i],
#         'date': dates[i*2],
#         'wta': meta[i*4+1]
#     }
#     return_dicts.append(temp)
#
# print(return_dicts)