from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'
    hotel_id = banco.Column(banco.String, primary_key=True) # Corrigido para String
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float) #mudado para float
    cidade = banco.Column(banco.String(40))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id, # Adicionado hotel_id
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        return cls.query.filter_by(hotel_id=hotel_id).first()

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
    
    def update_hotel(self, nome, estrelas, diaria, cidade): #metodo update
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def update_hotel(self,nome,estrelas,diaria,cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
