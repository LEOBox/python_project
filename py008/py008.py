from bs4 import BeautifulSoup
import requests

url = 'https://github.com/Show-Me-the-Code/show-me-the-code'
html = requests.get(url)

bsp = BeautifulSoup(html.text, "html.parser")
print(bsp.body.text)