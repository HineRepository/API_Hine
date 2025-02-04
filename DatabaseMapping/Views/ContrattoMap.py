from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Contratto(Base):
    __tablename__ = 'api_contratti'
    __table_args__ = {'schema': 'api'}
    dim_contratto: Mapped[str] = mapped_column(primary_key=True)
    dim_veicolo: Mapped[int] = mapped_column()
    targa_contratto: Mapped[str] = mapped_column()
    telaio_contratto: Mapped[str] = mapped_column()
    id_gestionale_veicolo_contratto: Mapped[str] = mapped_column()
    nuovo_usato_contratto: Mapped[str] = mapped_column()
    numero_contratto: Mapped[str] = mapped_column()
    tipo_contratto: Mapped[str] = mapped_column()
    dim_cliente: Mapped[int] = mapped_column()
    cliente_contratto: Mapped[str] = mapped_column()
    sede_contratto: Mapped[str] = mapped_column()
    dim_venditore: Mapped[int] = mapped_column()
    venditore_contratto: Mapped[str] = mapped_column()
    dt_apertura_contratto: Mapped[date] = mapped_column()
    dt_chiusura_contratto: Mapped[date] = mapped_column()
    has_assicurazione_contratto: Mapped[bool] = mapped_column()
    has_finanziamento_contratto: Mapped[bool] = mapped_column()
    count_permute_contratto: Mapped[int] = mapped_column()
    status_contratto: Mapped[str] = mapped_column()

    def toJson(self):
            return {
                "id_contratto": self.dim_contratto,
                "id_veicolo": self.dim_veicolo,
                "targa": self.targa_contratto,
                "telaio": self.telaio_contratto,
                "id_veicolo_gestionale": self.id_gestionale_veicolo_contratto,
                "nuovo_usato": 'Usato' if self.nuovo_usato_contratto == 'U' else 'Nuovo',
                "numero_contratto": self.numero_contratto,
                "tipo_contratto": self.tipo_contratto,
                "id_cliente": self.dim_cliente,
                "cliente": self.cliente_contratto,
                "sede_contratto": self.sede_contratto,
                "id_venditore": self.dim_venditore,
                "venditore": self.venditore_contratto,
                "data_apertura_contratto": self.dt_apertura_contratto.isoformat() if self.dt_apertura_contratto else None,
                "data_chiusura_contratto": self.dt_chiusura_contratto.isoformat() if self.dt_chiusura_contratto else None,
                "presenza_assicurazione": self.has_assicurazione_contratto,
                "presenza_finanziamento": self.has_finanziamento_contratto,
                "conteggio_permute": self.count_permute_contratto,
                "status": self.status_contratto
            }
