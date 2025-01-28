class Config:
    #SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:!HineAuto243!@10.250.10.150/DBA_IntergeaNE?driver=ODBC+Driver+17+for+SQL+Server"
    DEBUG = True