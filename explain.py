# import requests
# from bs4 import BeautifulSoup as BS

# file = open('explain_html.html', encoding='utf-8')

# html = file.read()

# soup = BS(html, 'html.parser')
# # print(soup)

# main_div = soup.find('div', class_='container')
# # print(main_div)

# navigaton = main_div.find('div', class_='navigation')
# # print(navigaton)

# ul = navigaton.find('ul',class_='info')
# # print(ul)

# li_list = ul.find_all('li')
# # print(li_list)

# # for i in li_list:
# #     print(i.text)

# content = main_div.find('div', class_='content')
# # print(content)

# post = content.find_all('div' ,class_='post')
# # print(post)

# # for a in post:
# #     print(a.text)

# footer = main_div.find('div', class_='footer')
# footer_box = footer.find_all('div',class_='footer box')
# for b in footer_box:
#     box = b.find('p').text
#     print(box)

# file.close



