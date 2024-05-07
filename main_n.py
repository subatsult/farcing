import requests
from bs4 import BeautifulSoup as BS
from openpyxl import Workbook

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')

    data = []

    for post in posts:
        prices = post.find('div', class_='flex gap-x-0.5x')
        price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        location = post.find('p',class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()  # Extract text from tag
        describe = post.find('p',class_='whitespace-nowrap truncate text-body_2').text.strip()
        data.append([price, price_m2, describe, location])  # Append text instead of tag
    # return data
    return data[:20]


# def save_in_txt(data,filename='test.txt'):
#     with open(filename,'w',encoding='utf-8') as file:
#         file.write('Price\tPrice per m2\tDescription\tLocation\n')
#         for item in data:
#             file.write('\t'.join(item) + '\n')
#     print(f'Data saved in file {filename}')


def save_in_excel(data,filename='data.xlsx'):
    wb = Workbook()
    ws = wb.active

    ws.append(['Price', 'Price per m2', 'Description', 'Location']) #  Write Titles

    for row in data: # Write data
        ws.append(row)
    wb.save(filename) # Saving data in file.xlsx
    print(f'Data saved in {filename}')

def main():
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    get_data(html)
    if html:
        data = get_data(html)
        save_in_excel(data)
    else:
        print('Did not save')

if __name__ == '__main__':
    main()

