import requests
from bs4 import BeautifulSoup

url = "https://sites.google.com/view/vestibular123"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
meta_tags = soup.find_all('meta', {'property': 'og:description'})

texto_salvar = meta_tags[0]['content']

print(texto_salvar)
