from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel
from sql_alchemy import banco  # Importe o 'banco' aqui

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
api = Api(app)



api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    banco.init_app(app) # Inicialize o banco com o app
    with app.app_context(): # Crie um contexto de aplicação
        banco.create_all() # Crie as tabelas dentro do contexto
    app.run(debug=True)