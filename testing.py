import requests
from bs4 import BeautifulSoup


url = 'https://scoringapp.signin.aws.amazon.com/console'

session = requests.session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': url
}



resp = session.get(url)
html = resp.text

soup = BeautifulSoup(html , 'lxml')


#payload = {
   
    
    
    
    #'vm.account':'scoringapp',
    #'vm.username':'pgscoringapp',
    #'vm.password':'q3Ra*II0ML9l'
#}



data = {}
form = soup.find('form', { 'name': 'vm.signin_form'})
for field in form.find_all('input'):
    try:
        data[field['name']] = field['value']
 
    except:
        pass
data[u'vm.account'] = 'scoringapp'
data[u'vm.email'] = 'pgscoringapp'
data[u'vm.password'] = 'q3Ra*II0ML9l'


post_resp = session.post('https://scoringapp.signin.aws.amazon.com/console', data = data)



penis_butthole = BeautifulSoup(post_resp.content, 'lxml')

if penis_butthole.find_all('title')[0].text == 'AWS Management Console':
    print('SUCCESS')
else:
    print('failed')




