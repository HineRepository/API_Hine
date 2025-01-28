'''
from flask import Flask, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:!HineAuto243!@10.250.10.150/BI_Hine?driver=ODBC+Driver+17+for+SQL+Server"
# initialize the app with the extension
db.init_app(app)




class Aziende(db.Model):
    Id: Mapped[int] = mapped_column(primary_key=True,)
    IdAzienda: Mapped[str] = mapped_column(unique=False)
    Azienda: Mapped[str]

    def azienda_to_dict(azienda):
        return {
            'Id': azienda.Id,
            'IdAzienda': azienda.IdAzienda,
            'Azienda': azienda.Azienda,
        }


@app.route("/aziende")
def aziende_list():
    aziende = db.session.execute(db.select(Aziende).order_by(Aziende.Id)).scalars()
    # Converte il risultato della query in una lista di dizionari
    aziende_list = [Aziende.azienda_to_dict(azienda) for azienda in aziende]
    return jsonify(aziende_list)


if __name__ == '__main__':
    app.run(debug=True)
'''