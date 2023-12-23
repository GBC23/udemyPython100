from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding = 'UTF-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)

# print(soup.a)
# print(soup.li)
# print(soup.p)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags) 



for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get('href'))