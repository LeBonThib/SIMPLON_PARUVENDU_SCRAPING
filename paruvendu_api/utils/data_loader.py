def get_url_paruvendu():
    with open('./paruvendu_api/outputs/url_harvest.txt', 'r') as file:
        return file.readlines()
        # SIMPLON_PARUVENDU_API\paruvendu_api\paruvendu_api\outputs\url_harvest.txt