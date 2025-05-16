from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        hoteis = HotelModel.query.all()
        return {'hoteis': [hotel.json() for hotel in hoteis]}
    
class Hotel(Resource):
    argument = reqparse.RequestParser()
    argument.add_argument('nome', type=str, required=1, help="Field is not null")
    argument.add_argument('estrelas', tyoe=float, required=1, help="Field is not null")
    argument.add_argument('diaria')
    argument.add_argument('cidade')
    
    def get (self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        
        return {'message:': 'null, not found'}, 404 
    
    def post(self,hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': 'Hotel id "{}" already exists.'.format(hotel_id)}, 400 #bad request
        
        dados = Hotel.argument.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel() 
        except:
            return {'message': 'An error 404 is found, we suck'}, 500
        return hotel.json()
        #novo_hotel = novo_hotel_obj.json()
        
        #hoteis.append(novo_hotel)
        #return novo_hotel, 200
    
    def put(self,hotel_id):
        dados = Hotel.argument.parse_args()
        hotel_finded = HotelModel.find_hotel(hotel_id)
        if hotel_finded:
            hotel_finded.update_hotel(**dados)
            hotel_finded.save_hotel()
        try:
            hotel_finded.save_hotel()
        except:
            return {'message': 'An error 404 is found, we suck'}, 500
            
        return hotel_finded.json(),200 #ok 100%
        return hotel_finded.json(),201

        
    
    def delete(self,hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel :
            hotel.delete_hotel()
            return {'message' : 'Hotel deleted'}
        return {'message': 'Hotel not found'}, 404