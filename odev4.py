from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd


app = Flask(__name__)
api = Api(app)

class matVeri(Resource):
    def get(self):
        data = pd.read_csv('veri.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        taban = request.args['taban']
        yukseklik = request.args['yukseklik']
        kenar1 = request.args['kenar1']
        kenar2 = request.args['kenar2']

        data = pd.read_csv('veri.csv')

        new_data = pd.DataFrame({
            'taban'      : [taban],
            'yukseklik'  : [yukseklik],
            'kenar1'     : [kenar1],
            'kenar2'     : [kenar2],

        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('veri.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 200

    
class ucgeninAlani(Resource):
    
    def get(self):
       data = pd.read_csv('veri.csv')
       data = data.to_dict('records')
       alanlar=[]
       for i in range(0, len(data)):
           alan=(data[i]['taban']*data[i]['yukseklik'])/2
           alanlar.append(alan)
       return  {'alanlar' : alanlar},200

class ucgeninCevresi(Resource):

    def get(self):
       data = pd.read_csv('veri.csv')
       data = data.to_dict('records')
       cevreler=[]
       for i in range(0, len(data)):
           cevre=(data[i]['taban']+data[i]['kenar1']+data[i]['kenar2'])
           cevreler.append(cevre)
       return  {'cevreler' : cevreler},200   

api.add_resource(matVeri, '/veri')
api.add_resource(ucgeninAlani, '/ucgeninAlani')
api.add_resource(ucgeninCevresi, '/ucgeninCevresi')
if __name__ == '__main__':

    app.run()