from bs4 import BeautifulSoup
import requests

url = "https://www.ratemyprofessors.com/professor/173343"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

tags_html = soup.find_all('div', {'class': 'TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW'})
tags = []
for tag_div in tags_html:
    spans = tag_div.find_all('span', class_='Tag-bs9vf4-0 hHOVKF')
    for span in spans:
        tags.append(span.get_text(strip=True))

cards = soup.find_all(class_='Rating__RatingInfo-sc-1rhvpxz-3 kEVEoU')
userCards = []
for card in cards[:]:
    cardData = {}
    course = card.find('div', class_='RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS')
    if course:
        cardData['course'] = course.get_text(strip=True)
    else:
        cardData['course'] = "N/A"

    date = card.find('div', class_='TimeStamp__StyledTimeStamp-sc-9q2r30-0 bXQmMr RatingHeader__RatingTimeStamp-sc-1dlkqw1-4 iwwYJD')
    if date:
        cardData['date'] = date.get_text(strip=True)
    else:
        cardData['date'] = "N/A"

    comment = card.find('div', class_='Comments__StyledComments-dzzyvm-0 gRjWel')
    if comment:
        cardData['comment'] = comment.get_text(strip=True)
    else:
        cardData['comment'] = "N/A"

    wtaList = card.find_all('div', class_='MetaItem__StyledMetaItem-y0ixml-0 LXClX')
    for wta in wtaList:
        span = wta.find('span')
        if 'Would Take Again' in wta.get_text() and span:
            cardData['wta'] = span.get_text(strip=True)
    if 'wta' not in cardData:
        cardData['wta'] = "N/A"
    userCards.append(cardData)

numRatings_html = soup.find(class_='RatingValue__NumRatings-qw8sqy-0 jMkisx')
ahref = numRatings_html.find('a')
numRatingsTxt = ahref.get_text(strip=True)
numRatings = ''.join(filter(str.isdigit, numRatingsTxt))

print(tags)
print(userCards)
print(numRatings)