import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,label="Linea",color="blue")

plt.title("Mi primer grafico")
plt.xlabel("Eje de la x")
plt.ylabel("Eje de la y")

plt.legend()

plt.show()