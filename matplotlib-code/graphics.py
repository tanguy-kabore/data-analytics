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
    SELECT cmd.date_commande as date, 
    count(cmd.date_commande) as nombre 
    FROM commandes cmd
    group by cmd.date_commande
""")

df1 = pd.read_sql(req1, con=connexion)
df2 = pd.read_sql(req2, con=connexion)
print(df2)
designation = df1["designation"]
#designation = list(designation)
#designation.append("Voiture")
print(designation)
quantite = df1["quantite"]
client = [2, 4, 1, 7, 11, 9]

img1, ax1= plt.subplots(2,2,figsize=(12,6))
ax1[0][0].plot(designation, quantite, marker='x', color="pink")
ax1[0][0].set_xlabel("Désignation des articles commandés")
ax1[0][0].set_ylabel("Quantités commandées des articles")
ax1[0][0].set_title("Image1: Quantité commandée par article")

ax1[0][0].plot(designation, client, marker='o', color="blue", linestyle="--")

ax1[0][0].legend(["quantité commandée","Client"])


ax1[0][1].bar(designation, quantite)

ax1[1][0].hist(quantite)

date = df2["date"]
nombre = df2["nombre"]

ax1[1][1].scatter(date, nombre)

plt.show()


print(df1)
print(designation)
print(quantite)