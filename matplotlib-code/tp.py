import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [90000, 150000, 1000000, 10000000, 20000]
sales1 = [80000, 250000, 5000000, 50000000, 30000]
Vente , axis1 = plt.subplots(1,3,figsize=(8,4))
axis1[0].plot(months,sales,color="red")
axis1[0].plot(months,sales1,color="blue")
axis1[1].plot(months,sales)
axis1

#plt.show()
print(axis1)
""" print(Vente)
print(Vente)
print(axis1)
print(type(axis1))
print(len(Vente.axes))
print(axis1.name)
plt.show() """

print(len(axis1))
print(dir(axis1))
print(len(dir(axis1[0])))
print(axis1.size)