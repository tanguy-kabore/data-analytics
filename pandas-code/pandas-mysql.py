import pandas as pd
from sqlalchemy import create_engine, text

USER = "root"
PWD = "root"
SERVER = "localhost"
PORT = 3306
BD = "ecommerce"
connexion = create_engine(f"mysql+pymysql://{USER}:{PWD}@{SERVER}:{PORT}/{BD}")
print(connexion)
req1 = text("SELECT * FROM clients")
#df1 = pd.read_sql(req1, con=connexion)
#print(df1)
#breakpoint
#df1.to_csv("clients.csv", sep=';',index=False )

req2 = text("""
    SELECT nom_client, prenom_client, date_naissance_client
    FROM clients
    WHERE YEAR(date_naissance_client) < '2000'
""")
""" df1 = pd.read_sql(req1, con=connexion)
df2 = pd.read_sql(req2, con=connexion)
print("----------------DF1-------------------")
print(df1)
df1.to_csv("clients.csv", sep=';',index=False )
print("----------------DF2-------------------")
print(df2) """

""" clt1 = {
    "nom_client": "SANON",
    "prenom_client": "Firmin",
    "date_naissance_client":"2006-10-20",
    "telephone_client":"+22655555555",
    "mot_de_passe":"12345678"
}

df_to_add = pd.DataFrame([clt1])
df_to_add.to_sql(name="clients", con=connexion, if_exists="append", index=False) """

print("----------------TEST-------------------")

req3 = text("""
    SELECT nom_client, prenom_client, date_naissance_client
    FROM clients
    WHERE YEAR(date_naissance_client) < '2000'
""")

















""" !pip install sqlalchemy pymysql

!pip show sqlalchemy
!pip show pymysql """