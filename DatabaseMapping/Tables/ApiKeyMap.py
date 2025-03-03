from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
#tabella dove sono memorizzate le API KEY per l'autenticazione dei softwares
class ApiKeyAuth(db.Model):
    __tablename__="api_key_auth"
    __table_args__ = {'schema': 'api'}
    Id: Mapped[int] = mapped_column(primary_key=True,name="id")
    AppName: Mapped[str] = mapped_column(unique=True,name="application_name")
    AppKey: Mapped[str] = mapped_column(unique=True,name="application_key")
    ExpirationDate: Mapped[str] = mapped_column(unique=True,name="expiration_date")

    
