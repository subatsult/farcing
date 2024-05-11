import requests
from bs4 import BeautifulSoup as BS
import openpyxl

import asyncio
from aiogram import Bot, Dispatcher

TOKEN = '7156503289:AAESskGUjLMf3PW6-ZzvfoUESqbT0_UDME4'

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_links(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    links = []
    for post in posts:
        # prices = post.find('div', class_='flex gap-x-0.5x')
        # price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        # price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        # title = post.find('p', class_='whitespace-nowrap truncate text-body_2').text.strip()
        # location = post.find('p', class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()
        link = post.get('href')
        full_link = 'https://aqarmap.com.eg'+ link
        links.append(full_link)
    return links 



def get_posts(html):
    soup = BS(html,'html.parser')
    info = {}
    title = soup.find('div', class_ = 'flex-1')
    price = title.find('span', class_ = 'text-title_3').text.replace('EGP','').strip()+' EGP'
    name = title.find('h3', class_ = 'text-gray__dark_2 text-body_1').text.strip()
    
    param = soup.find('div', class_ = 'flex flex-col gap-y-x')
    address = param.find('p', class_ = 'text-gray__dark_2 whitespace-nowrap truncate text-body_2').text.strip()
    area = param.find('p', class_ = 'text-gray__dark_2 whitespace-nowrap truncate text-body_1').text.strip()
    listing_details = soup.find('section', class_ = 'flex flex-col gap-x w-full container-fluid')
    details = listing_details.find_all('div', class_ = 'group flex px-1.5x py-2x')
    
    for i in details:
        key = i.find('h4',class_='flex-[30%] xl:flex-[30%] lg:flex-[35%] whitespace-nowrap text-gray__dark_1 text-body_2')
        value = i.find('span',class_ = 'flex-[70%] xl:flex-[70%] lg:flex-[65%] text-start text-gray__dark_2 text-body_1')
        if key and value:
            info.update({key.text.strip(): value.text.strip()})
        
    listing_descriptions = soup.find('section',class_ ='gap-y-3x container-fluid grid grid-cols-12' )
    description = listing_descriptions.find('span').text.strip()
    
    
    data = {
        'title':name,
        'price':price,
        'address':address,
        'area':area,
        'description':description,
        # 'info':info
    }
    return data



    
async def main():   
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    data = []
    for i in range(1, 3):
        page_url = URL + f'?page={i}'
        html = get_html(page_url)
        links = get_links(html)

        for link in links:
            detail_html = get_html(url=link)

            # new
            post_data = get_posts(html=detail_html)
            data.append(post_data)
            message = f"New Post: \n\nTitle: {post_data['title']}\nPrice: {post_data['price']}\nAddress: {post_data['address']}\nArea: {post_data['area']}\nDescription: {post_data['description']}"
            # Отправляем сообщение напрямую
            await bot.send_message(chat_id='1782718756', text=message)


if __name__ == '__main__':
    asyncio.run(main())
