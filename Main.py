


import datetime
import os
import sys
from flask import Flask, Response, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, and_
from sqlalchemy.orm import Mapped, mapped_column
from DatabaseMapping.Views.VeicoloMap import Veicolo
from DatabaseMapping.Views.ContrattoMap import Contratto
from DatabaseMapping.Tables.ApiKeyMap import ApiKeyAuth
from Config import Config
from apiflask import APIFlask, HTTPTokenAuth
currentDirectory =  os.path.dirname(os.path.realpath(__file__))
hineUtilsPath=os.path.abspath(os.path.join(currentDirectory, os.pardir))+"\\HineUtils"
sys.path.append(hineUtilsPath)
from HineSharePointHandler import SharepointHandler



#---------Logging---Inizio----------------
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter


currentDirectory =  os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger("API_Hine")
handler = TimedRotatingFileHandler(filename=currentDirectory+'\\API_Hine.log', when='D', interval=2, backupCount=5, encoding='utf-8', delay=False)
formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
# -------  Logging---Fine--------------------

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = APIFlask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

app.config.from_object(Config)
# initialize the app with the extension
db.init_app(app)


@auth.verify_token
def verify_token(token):
    validApiKey = db.session.execute(db.select(ApiKeyAuth.AppKey).where(and_(
                ApiKeyAuth.AppKey == token,
                ApiKeyAuth.ExpirationDate >= datetime.datetime.now()
            ))).scalars().all()
    
    if validApiKey != None and len(validApiKey) > 0:
        if token == validApiKey[0]:
            return True
    
    return False

#==================================================VEICOLO===============================================
# esempio chiamata
#http://127.0.0.1:5000/veicoli/vin/ZFA16900001091537
@app.route('/veicoli/vin/<string:vin>', methods=['GET'])
@auth.login_required
def veicoli_By_Vin(vin):
    logger.info(f"veicoli_By_Vin - {vin}")
    result = db.session.execute(db.select(Veicolo).where(Veicolo.telaio_veicolo == vin)).scalars() 
    resultToJson = [Veicolo.toJson(item) for item in result]
    return jsonify(resultToJson)

# esempio chiamata
#http://127.0.0.1:5000/veicoli/targa/EX858RN
@app.route('/veicoli/targa/<string:targa>', methods=['GET'])
@auth.login_required
def veicoli_By_Targa(targa):
    logger.info(f"veicoli_By_Targa - {targa}")
    result = db.session.execute(db.select(Veicolo).where(Veicolo.targa_veicolo == targa)).scalars() 
    resultToJson = [Veicolo.toJson(item) for item in result]
    return jsonify(resultToJson)




#==================================================CONTRATTO===============================================
# esempio chiamata
#http://127.0.0.1:5000/contratti/vin/ZFA16900001091537
@app.route('/contratti/vin/<string:vin>', methods=['GET'])
@auth.login_required
def contratti_By_Vin(vin):
    logger.info(f"contratti_By_Vin - {vin}")
    result = db.session.execute(db.select(Contratto).where(Contratto.telaio_contratto == vin)).scalars() 
    resultToJson = [Contratto.toJson(item) for item in result]
    return jsonify(resultToJson)

# esempio chiamata
#http://127.0.0.1:5000/contratti/targa/EX858RN
@app.route('/contratti/targa/<string:targa>', methods=['GET'])
@auth.login_required
def contratti_By_Targa(targa):
    logger.info(f"contratti_By_Targa - {targa}")
    result = db.session.execute(db.select(Contratto).where(Contratto.targa_contratto == targa)).scalars() 
    resultToJson = [Contratto.toJson(item) for item in result]
    return jsonify(resultToJson)

# esempio chiamata
#http://127.0.0.1:5000/contratti/cliente/ragionesociale
@app.route('/contratti/cliente/<string:ragionesociale>', methods=['GET'])
@auth.login_required
def contratti_By_Cliente(ragionesociale):
    logger.info(f"contratti_By_Cliente - {ragionesociale}")
    result = db.session.execute(db.select(Contratto).where(Contratto.cliente_contratto.contains(ragionesociale))).scalars() 
    resultToJson = [Contratto.toJson(item) for item in result]
    return jsonify(resultToJson)

# esempio chiamata
#http://127.0.0.1:5000/contratti/id/idContratto
@app.route('/contratti/id/<string:idContratto>', methods=['GET'])
@auth.login_required
def contratto_By_Id(idContratto):
    logger.info(f"contratto_By_Id - {idContratto}")
    result = db.session.execute(db.select(Contratto).where(Contratto.dim_contratto == idContratto)).scalars() 
    resultToJson = [Contratto.toJson(item) for item in result]
    return jsonify(resultToJson)


#TODO aggiungere azienda a lista, duplicare liste e attuare controllo su altre aziende
# esempio chiamata
#http://127.0.0.1:5000/veicoli_aziendali/targa/FF785GZ
@app.route('/veicoli_aziendali/targa/<string:targa>', methods=['GET'])
@auth.login_required
def veicoli_aziendali_By_Targa(targa):
    logger.info(f"veicoli_aziendali_By_Targa - {targa}")    
    sharepointHandler = SharepointHandler()

    listaJson = []
    result = sharepointHandler.GetVeicoliUsoAziendaleByTarga('Vetture uso aziendale - Autoteam',targa)
    listaJson.append(json.loads(result))

    result = sharepointHandler.GetVeicoliUsoAziendaleByTarga('Vetture uso aziendale - Autoteam9',targa)
    listaJson.append(json.loads(result))

    result = sharepointHandler.GetVeicoliUsoAziendaleByTarga('Vetture uso aziendale - Gruppo Ferrari',targa)
    listaJson.append(json.loads(result))

    print(json.dumps(listaJson, indent=4, sort_keys=True, ensure_ascii=False))
    
    return jsonify(json.dumps(listaJson, indent=4, sort_keys=True, ensure_ascii=False))
    







if __name__ == '__main__':
    app.run(debug=Config.DEBUG)





