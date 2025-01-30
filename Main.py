
from flask import Flask, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from DatabaseMapping.Views.VeicoloMap import Veicolo
from DatabaseMapping.Views.AziendaMap import Azienda
from Config import Config

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.config.from_object(Config)

# initialize the app with the extension
db.init_app(app)
'''
#==================================================AZIENDA===============================================
# esempio chiamata
#http://127.0.0.1:5000/aziende
@app.route("/aziende", methods=['GET'])
def aziende_list():
    aziende = db.session.execute(db.select(Azienda).order_by(Azienda.Azienda)).scalars()
    aziende_list = [Azienda.toJson(azienda) for azienda in aziende]
    return jsonify(aziende_list)

# esempio chiamata
#http://127.0.0.1:5000/aziende/id/AT
@app.route('/aziende/id/<string:azienda_id>', methods=['GET'])
def azienda_By_Id(azienda_id):
    aziende = db.session.execute(db.select(Azienda).where(Azienda.Id == azienda_id)).scalars() 
    aziende_list = [Azienda.toJson(azienda) for azienda in aziende]
    return jsonify(aziende_list)

'''


#==================================================VEICOLO===============================================
# esempio chiamata
#http://127.0.0.1:5000/veicoli/vin/ZFA16900001091537
@app.route('/veicoli/vin/<string:vin>', methods=['GET'])
def veicolo_By_Vin(vin):
    result = db.session.execute(db.select(Veicolo).where(Veicolo.telaio_veicolo == vin)).scalars() 
    resultToJson = [Veicolo.toJson(item) for item in result]
    return jsonify(resultToJson)

# esempio chiamata
#http://127.0.0.1:5000/veicoli/targa/EX858RN
@app.route('/veicoli/targa/<string:targa>', methods=['GET'])
def veicolo_By_targa(targa):
    result = db.session.execute(db.select(Veicolo).where(Veicolo.targa_veicolo == targa)).scalars() 
    resultToJson = [Veicolo.toJson(item) for item in result]
    return jsonify(resultToJson)




if __name__ == '__main__':
    app.run(debug=True)
