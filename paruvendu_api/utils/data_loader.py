import pandas as pd

def get_url_paruvendu():
    with open('./paruvendu_api/outputs/url_harvest.txt', 'r') as file:
        return file.readlines()