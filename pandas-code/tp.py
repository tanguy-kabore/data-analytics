import pandas as pd

students = {
    'nom': ["KABORE","OUEDRAOGO","SAWADOGO","TRAORE"],
    'age': [35,20,16,None],
    'note':[20,15,10,15]
}

df = pd.DataFrame(students)
print("-----------------Utilitares------------------------")
print(df.tail(2))
#print(df)

breakpoint()
print("-----------------END------------------------")
print(df.loc[1:1,["nom","note"]])
print("-----------------------------------------")
print(df.loc[1])
print("-----------------------------------------")
print(df.iloc[0:2,0:2])
print("-----------------------------------------")
print(type((df["note"] > 10) & (df["note"] < 20)))
print(type((df["note"] > 10) & (df["age"] < 20)))
#print(pd.DataFrame((df["note"] > 10) & (df["age"] < 20)))
print(df.loc[(df["note"] > 10) & (df["age"] < 20), ["nom","note"]])
#df1 = pd.DataFrame()

#print(df.loc[df1.iloc[1]])
print("-----------------------------------------")

print(df.loc[(df["note"] > 10), "nom"])

print("-----------------------------------------")
df1 = df.set_index("note")
#print(df1.loc["KABORE", "age"])
print("-----------------------------------------")
print(df1.loc[15, "note"])



serie_nom = df["nom"]
serie_nom_note = df[["nom","note","age"]]


print(serie_nom_note)

print(df)
print(students)
print(type(students))


