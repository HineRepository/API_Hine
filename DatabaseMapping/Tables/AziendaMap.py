from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Azienda(db.Model):
    __tablename__="Aziende"
    Id: Mapped[int] = mapped_column(primary_key=True,)
    IdAzienda: Mapped[str] = mapped_column(unique=False)
    Azienda: Mapped[str]

    def toJson(azienda):
        return {
            'Id': azienda.Id,
            'IdAzienda': azienda.IdAzienda,
            'Azienda': azienda.Azienda,
        }