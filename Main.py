
from flask import Flask, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
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


@app.route("/aziende")
def aziende_list():
    aziende = db.session.execute(db.select(Azienda).order_by(Azienda.Azienda)).scalars()
    aziende_list = [Azienda.toJson(azienda) for azienda in aziende]
    return jsonify(aziende_list)


if __name__ == '__main__':
    app.run(debug=True)
