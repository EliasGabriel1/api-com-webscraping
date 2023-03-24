from flask import Flask
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/busca/<product>')
def hello(product):
    url = f"https://www.carrefour.com.ar/{product}/p"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_tag = soup.find('span', {'class': 'lyracons-carrefourarg-product-price-1-x-currencyInteger'}).text
    name_tag = soup.find('span', {
        'class': 'vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--quickview'}).text
    marca_tag = soup.find('span', {'class': 'vtex-store-components-3-x-productBrandName'}).text
    price = re.findall(r'\d+[\.,]?\d*', price_tag)[0].replace(',', '.')
    return f"O produto: {name_tag} da marca: {marca_tag} está: R${price}"

if __name__ == '__main__':
    app.run(debug=True)
