import scrapy
from bs4 import BeautifulSoup
from utils.data_loader import get_url_paruvendu
from ..items import DataHarvesterItem

url_list = get_url_paruvendu()

class DataHarvesterSpider1(scrapy.Spider):
    name = 'data_harvester1'
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest1.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[0:9999]
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
        print(f"Job's done for {response.request.url} from {self.name}")

class DataHarvesterSpider2(DataHarvesterSpider1):
    name = 'data_harvester2'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest2.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[10000:19999]

class DataHarvesterSpider3(DataHarvesterSpider1):
    name = 'data_harvester3'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest3.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[20000:29999]

class DataHarvesterSpider4(DataHarvesterSpider1):
    name = 'data_harvester4'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest4.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[30000:39999]

class DataHarvesterSpider5(DataHarvesterSpider1):
    name = 'data_harvester5'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest5.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[40000:49999]

class DataHarvesterSpider6(DataHarvesterSpider1):
    name = 'data_harvester6'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest6.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[50000:59999]

class DataHarvesterSpider7(DataHarvesterSpider1):
    name = 'data_harvester7'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest7.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[60000:69999]

class DataHarvesterSpider8(DataHarvesterSpider1):
    name = 'data_harvester8'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest8.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[70000:79999]

class DataHarvesterSpider9(DataHarvesterSpider1):
    name = 'data_harvester9'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest9.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[80000:89999]

class DataHarvesterSpider10(DataHarvesterSpider1):
    name = 'data_harvester10'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest10.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[90000:99999]

class DataHarvesterSpider11(DataHarvesterSpider1):
    name = 'data_harvester11'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest11.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[100000:109999]

class DataHarvesterSpider12(DataHarvesterSpider1):
    name = 'data_harvester12'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest12.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[110000:119999]

class DataHarvesterSpider13(DataHarvesterSpider1):
    name = 'data_harvester13'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest13.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[120000:129999]

class DataHarvesterSpider14(DataHarvesterSpider1):
    name = 'data_harvester14'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest14.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[130000:139999]

class DataHarvesterSpider15(DataHarvesterSpider1):
    name = 'data_harvester15'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest15.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[140000:149999]

class DataHarvesterSpider16(DataHarvesterSpider1):
    name = 'data_harvester16'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest16.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[150000:159999]

class DataHarvesterSpider17(DataHarvesterSpider1):
    name = 'data_harvester17'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest17.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[160000:169999]

class DataHarvesterSpider18(DataHarvesterSpider1):
    name = 'data_harvester18'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest18.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[170000:179999]

class DataHarvesterSpider19(DataHarvesterSpider1):
    name = 'data_harvester19'   
    custom_settings = {
        "FEEDS": {"./paruvendu_api/outputs/data_harvest19.json":{"format":"jsonlines"}}
        # "FEED_EXPORT_ENCODING": {"utf-8"}
    }
    start_urls = url_list[180000:182757]