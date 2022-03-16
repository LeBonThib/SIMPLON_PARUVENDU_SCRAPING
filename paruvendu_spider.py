import scrapy
from bs4 import BeautifulSoup
import json

class ParuvenduSpiderSpider(scrapy.Spider):
    name = 'paruvendu_spider'
    start_urls = []

    def __init__(self):
        with open('C:/Users/namor/OneDrive/Documents/simplon/Data IA/Projets/Projet 6/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/harvest1.json','r') as sample:
            for line in sample:
                self.start_urls.append(json.loads(line.strip())['url'])

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        specifications = soup.find_all('div', {'class':'cotea16-mes', 'id':'mes-ht'})
        dict_of_specifications = {}
        for index in range(2):
            for i in specifications[index].find_all('li'):
                keys = [i for i in i.text.strip().split('\n') if i][0]
                values = [i for i in i.text.strip().split('\n') if i][1]

                dict_of_specifications[keys] = values #{"Version": "Punto Evo 1.4 16v Turbo MultiAir 165", "Prix": "12 990 \u20ac", "Ann\u00e9e": "Mai 2011", "Kilom\u00e9trage": "66 100", "Energie": "Essence", "Emissions de CO2": "142", "Consommation mixte": "6.0", "Transmission": "Manuelle", "Nb de portes": "2 portes avec hayon", "Puissance fiscale": "9", "Nombre de places": "5"}

            yield dict_of_specifications