from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Azienda(db.Model):
    __tablename__="AUTO_dim_azienda"
    __table_args__ = {'schema': 'bi'}
    Id: Mapped[int] = mapped_column(primary_key=True,name="dim_azienda")
    Azienda: Mapped[str] = mapped_column(unique=False)


    def toJson(azienda):
        return {
            'Id': azienda.Id,
            'Azienda': azienda.Azienda,
        }