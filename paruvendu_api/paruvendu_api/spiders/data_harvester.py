import scrapy
import pandas as pd
from bs4 import BeautifulSoup
from utils.data_loader import get_url_paruvendu
from ..items import DataHarvesterItem

class DataHarvesterSpider(scrapy.Spider):
    name = 'data_harvester'
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = get_url_paruvendu()
    # start_urls = ['https://www.paruvendu.fr/a/voiture-occasion/fiat/500/1260671363A1KVVOFI500']
    def parse(self, response):
        data_harvester_item = DataHarvesterItem()
        data_harvester_item['url'] = response.request.url
        data_harvester_item['status'] = response.status
        data_harvester_item['location'] = "N/A"
        data_harvester_item['version'] = "N/A"
        data_harvester_item['price'] = "N/A"
        data_harvester_item['year'] = "N/A"
        data_harvester_item['mileage'] = "N/A"
        data_harvester_item['fuel_type'] = "N/A"
        data_harvester_item['emission'] = "N/A"
        data_harvester_item['fuel_usage'] = "N/A"
        data_harvester_item['transmission'] = "N/A"
        data_harvester_item['door_nb'] = "N/A"
        data_harvester_item['technical_power'] = "N/A"
        data_harvester_item['seat_nb'] = "N/A"
        data_harvester_item['actual_power'] = "N/A"
        data_harvester_item['body_colour'] = "N/A"
        data_harvester_item['body_type'] = "N/A"
        data_harvester_item['warranty'] = "N/A"
        data_harvester_item['control'] = "N/A"
        
        if response.status == 200:
            data_harvester_item['url'] = response.request.url
        
            html_page = response.text
            soup = BeautifulSoup(html_page, 'lxml')

            location = soup.find('h2',{'id':'detail_loc'}).text.strip().replace("\n"," ").replace("\r"," ").replace("  "," ").lower()
            data_harvester_item['location'] = location
            
            base_car_information = soup.find('div',{'class':'cotea16-mes'})

            if base_car_information.find('li',{'class':'vers'}) is not None:
                data_harvester_item['version'] = base_car_information.find('li',{'class':'vers'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'px'}) is not None:    
                data_harvester_item['price'] = base_car_information.find('li',{'class':'px'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'ann'}) is not None:    
                data_harvester_item['year'] = base_car_information.find('li',{'class':'ann'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'kil'}) is not None:    
                data_harvester_item['mileage'] = base_car_information.find('li',{'class':'kil'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'en'}) is not None:    
                data_harvester_item['fuel_type'] = base_car_information.find('li',{'class':'en'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'emiss'}) is not None:    
                data_harvester_item['emission'] = base_car_information.find('li',{'class':'emiss'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'cons'}) is not None:    
                data_harvester_item['fuel_usage'] = base_car_information.find('li',{'class':'cons'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'vit'}) is not None:    
                data_harvester_item['transmission'] = base_car_information.find('li',{'class':'vit'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'carro'}) is not None:    
                data_harvester_item['door_nb'] = base_car_information.find('li',{'class':'carro'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'puiss'}) is not None:    
                data_harvester_item['technical_power'] = base_car_information.find('li',{'class':'puiss'}).text.strip().replace("\n"," ").replace("  "," ").lower()
            if base_car_information.find('li',{'class':'por'}) is not None:    
                data_harvester_item['door_nb'] = base_car_information.find('li',{'class':'por'}).text.strip().replace("\n"," ").replace("  "," ").lower()

            complement = soup.find_all("li",{"class":"nologo"})
            for info in complement:
                info_txt = info.text.strip().replace("\n"," ").replace("  "," ").lower()
                if "couleur" in info_txt:
                    if not "intérieur" in info_txt:
                        info_txt_splitted = info_txt.split()
                        couleur_list = info_txt_splitted[1:]
                        couleur = ""
                        for word in couleur_list:
                            couleur += " " + word
                        couleur = couleur.strip()
                        data_harvester_item['body_colour'] = couleur
                        
                elif "puissance réelle" in info_txt:
                    info_txt_splitted = info_txt.split()
                    puissance_reelle = info_txt_splitted[2]
                    data_harvester_item['actual_power'] = puissance_reelle

                elif "carrosserie" in info_txt:
                    if not "type" in info_txt:
                        info_txt_splitted = info_txt.split()
                        carrosserie = info_txt_splitted[1]
                        data_harvester_item['body_type'] = carrosserie

        yield data_harvester_item
        print(f"Job's done for {response.request.url}")