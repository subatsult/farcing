import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    # data = []
    links = []
    for post in posts:
        # prices = post.find('div', class_='flex gap-x-0.5x')
        # price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        # price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        # location = post.find('p',class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()  # Extract text from tag
        # describe = post.find('p',class_='whitespace-nowrap truncate text-body_2').text.strip()
        # data.append([price, price_m2, describe, location])  # Append text instead of tag
        link = post.get('href')
        full_link = 'https://aqarmap.com.eg' + link
        links.append(full_link)
    return links



def get_posts(html):
    soup = BS(html,'html.parser')
    info = {}
    title = soup.find('div', class_='flex-1')
    price = title.find('span', class_='text-title_3').text.replace('EGP','').strip() + ' EGP'
    name = title.find('h3',class_='text-gray__dark_2 text-body_1').text.strip()
    param = soup.find('div',class_='flex flex-col gap-y-x')
    address = param.find('p',class_='text-gray__dark_2 whitespace-nowrap truncate text-body_2').text.strip()
    area = param.find('p', class_='text-gray__dark_2 whitespace-nowrap truncate text-body_1').text.strip()
    listing_details = soup.find('section',class_='flex flex-col gap-x w-full container-fluid')
    details = listing_details.find_all('span',class_='flex-[70%] xl:flex-[70%] lg:flex-[65%] text-start text-gray__dark_2 text-body_1')
    detail = []
    for _ in details:
        detail += _
    listing_descr = soup.find('section',class_='gap-y-3x container-fluid grid grid-cols-12')
    descr = listing_descr.find('div',class_='col-span-9 flex flex-col gap-x')
    descrip = descr.find_all('span')
    description = []
    for _ in descrip:
        description += _.text.strip()
    print(detail,description)
    









# def save_in_txt(data,filename='test.txt'):
#     with open(filename,'w',encoding='utf-8') as file:
#         file.write('Price\tPrice per m2\tDescription\tLocation\n')
#         for item in data:
#             file.write('\t'.join(item) + '\n')
#     print(f'Data saved in file {filename}')


def main():
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    
    for i in range(1, 4):
        page_url = URL + f'?page={i}'
        html = get_html(page_url)
        links = get_links(html)
        for link in links:
            detail_html = get_html(url=link)
            get_posts(html=detail_html)

    # if html:
    #     data = get_data(html)
    #     save_in_txt(data)
    # else:
    #     print('Did not save')

if __name__ == '__main__':
    main()

