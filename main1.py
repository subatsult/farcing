import requests
from bs4 import BeautifulSoup as BS

file = open('index.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

div_container = soup.find('div', class_='container')
# nav_ = div_container.find('nav', class_='navbar navbar-expand-lg bg-body-tertiary')
# div_cont_fluid = nav_.find('div',class_='container-fluid')
# it_acad = div_cont_fluid.find('a',class_='navbar-brand')
# # print(it_acad.text)
# div_navbar_collapse = div_cont_fluid.find('div',class_='collapse navbar-collapse')
# a_l = div_navbar_collapse.find_all('a',class_='nav-link')
# # for _ in a_l:
# #     print(_.text)
# u_l = div_navbar_collapse.find('ul',class_='dropdown-menu')
# print(u_l)
# i_l = u_l.find_all('li', class_='ropdown-item')
# for _ in i_l:
#     box = _.find('a').text
#     print(box)

cards = div_container.find_all('div',class_='card')
cards = soup.find_all('div', class_='card')

for card in cards:
  title = card.find('h5', class_='card-title').text.strip()
  text = card.find('p', class_='card-text').text
  img = card.find('img')['src']

  print("Описание: ", title)
  print("Текст: ", text)
  print("Картинка: ", img + '\n')