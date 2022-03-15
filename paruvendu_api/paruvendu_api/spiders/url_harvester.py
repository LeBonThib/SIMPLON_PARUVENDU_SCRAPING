import scrapy
from bs4 import BeautifulSoup
from ..items import URLHarvesterItem
from tqdm import tqdm

class URLHarvesterSpider(scrapy.Spider):
    name = 'url_harvester'
    start_urls = []

    def __init__(self):
        brand_list = ['Abarth', 'Aiways', 'Aleko', 'Alfa Romeo', 'Alpina', 'Aro', 'Aston Martin', 'Audi', 'Austin', 'Autres', 'Auverland', 'BMW', 'Bentley', 'Bertone', 'Buggy', 'Buick', 'Cadillac', 'Caterham', 'Chevrolet', 'Chrysler', 'Citroën', 'Corvette', 'Cupra', 'DS', 'Dacia', 'Daewoo', 'Daihatsu', 'Daimler', 'Dangel', 'De la Chapelle', 'Dodge', 'Donkervoort', 'Ferrari', 'Fiat', 'Ford', 'GMC', 'Gac Gonow', 'Honda', 'Hummer', 'Hyundai', 'Infiniti', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Lada', 'Lamborghini', 'Lancia', 'Land-Rover', 'Landwin', 'Lexus', 'Lotus', 'MG', 'MPM Motos', 'Mahindra', 'Maruti', 'Maserati', 'Maybach', 'Mazda', 'Mega', 'Mercedes', 'Mini', 'Mitsubishi', 'Morgan', 'Nissan', 'Opel', 'PGO', 'Peugeot', 'Polski/FSO', 'Pontiac', 'Porsche', 'Proton', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Santana', 'Seat', 'Seres', 'Shuanghuan', 'Skoda', 'Smart', 'Ssangyong', 'Subaru', 'Suzuki', 'TVR', 'Talbot', 'Tata', 'Tesla', 'Toyota', 'Venturi', 'Volkswagen', 'Volvo', 'Wallys']
        for brand in brand_list:
            self.start_urls.append(f"https://www.paruvendu.fr/a/voiture-occasion/{brand.lower()}/")
            """ if brand == "Abarth":
                model_list = ['']
                for model in model_list:
                    self.start_urls.append(f"https://www.paruvendu.fr/a/voiture-occasion/{brand.lower()}/{model.lower()}/") """
            
    def parse(self, response):
        url_harvester_item = URLHarvesterItem()
        if response.status != 200:
            url_harvester_item['url'] = response.request.url
            url_harvester_item['status'] = response.status
            url_harvester_item['brand'] = "N/A"

            yield url_harvester_item

        if response.status == 200:
            html_page = response.text
            soup = BeautifulSoup(html_page, 'lxml')
            listings = soup.find_all('div',{'class':'lazyload_bloc ergov3-annonce ergov3-annonceauto'})
            for listing in listings:
                url = listing.find('a').get('href')
                
                url_harvester_item['url'] = url

                yield url_harvester_item

            next_page_partial = soup.find('div',{'class':'v2pv15-pagsuiv flol'})
            if next_page_partial is not None:
                next_page = next_page_partial.find('a').get('href')
                current_page_url = response.request.url
                current_page_url_split = current_page_url.split('?')
                next_page_url = current_page_url_split[0] + next_page
                yield scrapy.Request(next_page_url, callback=self.parse)
            else:
                print(f"Job's done.")

    class CarHarvesterSpider(scrapy.Spider):
        pass