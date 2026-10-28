import pandas as pd
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt

USER = "root"
PWD = "root"
SERVER = "localhost"
PORT = 3306
BD = "ecommerce"
connexion = create_engine(f"mysql+pymysql://{USER}:{PWD}@{SERVER}:{PORT}/{BD}")

req1 = text("""
    SELECT art.designation_article as designation, 
    count(id_article) as quantite, 
    count(client) as nbre_client
    FROM articles art, commandes cmd, clients clt
    WHERE  art.id_article = cmd.article
    AND clt.id_client = cmd.client
    group by art.designation_article
""")

req2 = text("""
    SELECT cmd.client as client, 
    count(client) as nbre_client
    FROM articles art, commandes cmd, clients clt
    WHERE  
    group by cmd.client
""")

df1 = pd.read_sql(req1, con=connexion)

designation = df1["designation"]
quantite = df1["quantite"]

img1, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(designation, quantite, marker='x', color="pink")
ax1.set_xlabel("Désignation des articles commandés")
ax1.set_ylabel("Quantités commandées des articles")
ax1.set_title("Image1: Quantité commandée par article")
ax1.legend(["quantité commandée"])
#plt.show()


print(df1)
print(designation)
print(quantite)