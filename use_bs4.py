import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/'
try:
    response = requests.get( url )
    if response.status_code == 200 :
        print(f'success! response = {response.status_code}')
        # print(f'content = {response.text}')
        soup = BeautifulSoup (response.text, features="html.parser")
        print(f'Hasil pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'woops, ada kesalahan requests {response.status_code,}')
except Exception as e :
    print(f'there is an error{e}')
print('program ended')
