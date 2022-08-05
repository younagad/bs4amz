import requests
from bs4 import BeautifulSoup

url = 'https://scoringapp.signin.aws.amazon.com/console'

session = requests.session()

payload = {
    'vm.account':'scoringapp',
    'vm.username':'pgscoringapp',
    'vm.password':'q3Ra*II0ML9l'
}


session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': url
}

page = session.post(url, data=payload)

soup = BeautifulSoup(page.content, 'lxml')
print(soup.prettify())
print(page.status_code)
