from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Veicolo(db.Model):
    __tablename__ = 'api_veicoli'
    __table_args__ = {'schema': 'api'}

    dim_veicolo: Mapped[str] = mapped_column(primary_key=True)
    azienda_veicolo: Mapped[str] = mapped_column()
    id_gesionale_veicolo: Mapped[int] = mapped_column()
    telaio_veicolo: Mapped[str] = mapped_column()
    targa_veicolo: Mapped[str] = mapped_column()
    dt_immatricolazione_veicolo: Mapped[date] = mapped_column()
    dt_arrivo_veicolo: Mapped[date] = mapped_column()
    dt_uscita_veicolo: Mapped[date] = mapped_column()
    gruppo_marca_veicolo: Mapped[str] = mapped_column()
    modello_veicolo: Mapped[str] = mapped_column()
    veicolo: Mapped[str] = mapped_column()
    gruppo_tipo_veicolo: Mapped[str] = mapped_column()
    alimentazione_veicolo: Mapped[str] = mapped_column()
    nuovo_usato_veicolo: Mapped[str] = mapped_column()
    status_veicolo: Mapped[str] = mapped_column()
    ubicazione_attuale_veicolo: Mapped[str] = mapped_column()
    km_percorsi_veicolo: Mapped[int] = mapped_column()
    linea_veicolo: Mapped[str] = mapped_column()

    def toJson(self):
        return {"id_veicolo": self.dim_veicolo,
            "azienda": self.azienda_veicolo,
            "id_veicolo_gestionale": self.id_gesionale_veicolo,
            "vin": self.telaio_veicolo,
            "targa": self.targa_veicolo,
            "data_immatricolazione": self.dt_immatricolazione_veicolo.isoformat() if self.dt_immatricolazione_veicolo else None,
            "data_arrivo": self.dt_arrivo_veicolo.isoformat() if self.dt_arrivo_veicolo else None,
            "data_uscita": self.dt_uscita_veicolo.isoformat() if self.dt_uscita_veicolo else None,
            "marca": self.gruppo_marca_veicolo,
            "modello": self.modello_veicolo,
            "veicolo": self.veicolo,
            "tipo_veicolo": self.gruppo_tipo_veicolo,
            "alimentazione": self.alimentazione_veicolo,
            "nuovo_usato": self.nuovo_usato_veicolo,
            "status": self.status_veicolo,
            "ubicazione_ultima": self.ubicazione_attuale_veicolo,
            "km_percorsi": self.km_percorsi_veicolo,
            "linea": self.linea_veicolo
        }