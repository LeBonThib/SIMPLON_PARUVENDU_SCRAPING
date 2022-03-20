import pandas as pd
from flaskerino import create_app
from flask_restful import Api, Resource, reqparse
from joblib import load

app = create_app()
api = Api(app)

def api_get_prediction(get_location, get_version, get_year, get_mileage, get_fuel_type, get_emission, get_transmission, get_door_nb, get_seat_nb, get_technical_power, get_actual_power, get_body_type):
    best_model = load('C:/Users/Pontiff/Desktop/testerino/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/best_GBR.sav')
    model_encoder = load('C:/Users/Pontiff/Desktop/testerino/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/model_encoder.sav') 

    feature_dict = dict(location = get_location, version = get_version, year = get_year, mileage = get_mileage, fuel_type = get_fuel_type, emission = get_emission, transmission = get_transmission, door_nb = get_door_nb, technical_power = get_technical_power, seat_nb = get_seat_nb, actual_power = get_actual_power, body_type = get_body_type)
    feature_data = pd.DataFrame(feature_dict, index=[0])

    encoded_feature_data = model_encoder.transform(feature_data)

    prediction = best_model.predict(encoded_feature_data) 
    
    predicted_price = prediction[0]
    return predicted_price

parser = reqparse.RequestParser()
parser.add_argument('get_location', type=int)
parser.add_argument('get_version', type=str)
parser.add_argument('get_year', type=int)
parser.add_argument('get_mileage', type=int)
parser.add_argument('get_fuel_type', type=str)
parser.add_argument('get_emission', type=int)
parser.add_argument('get_transmission', type=str)
parser.add_argument('get_door_nb', type=int)
parser.add_argument('get_seat_nb', type=int)
parser.add_argument('get_technical_power', type=int)
parser.add_argument('get_actual_power', type=int)
parser.add_argument('get_body_type', type=str)

class api_get_test(Resource):
    def get(self):
        args = parser.parse_args()
        get_location = args['get_location']
        get_version = args['get_version']
        get_year = args['get_year']
        get_mileage = args['get_mileage']
        get_fuel_type = args['get_fuel_type']
        get_emission = args['get_emission']
        get_transmission = args['get_transmission']
        get_door_nb = args['get_door_nb']
        get_seat_nb = args['get_seat_nb']
        get_technical_power = args['get_technical_power']
        get_actual_power = args['get_actual_power']
        get_body_type = args['get_body_type']
        
        get_price = api_get_prediction(get_location, get_version, get_year, get_mileage, get_fuel_type, get_emission, get_transmission, get_door_nb, get_seat_nb, get_technical_power, get_actual_power, get_body_type = get_body_type)
        return {"price": get_price}
        # return {"price": "Coucou"}

api.add_resource(api_get_test, "/api")
# ?get_location=&get_version=&get_year=&get_mileage=&get_fuel_type=&get_emission=&get_transmission=&get_door_nb=&get_seat_nb=&get_technical_power=&get_actual_power=

# enable debugging mode
app.config["DEBUG"] = True

if __name__ == '__main__': #prevents web server starting without running main.py (e.g: can't import it and run it from another file)
    app.run()

# http://127.0.0.1:5000/api?get_location=54&get_version=dacia/duster&get_year=2020&get_mileage=44000&get_fuel_type=essence&get_emission=123&get_transmission=manuelle&get_door_nb=4&get_seat_nb=5&get_technical_power=6&get_actual_power=107&get_body_type=4x4