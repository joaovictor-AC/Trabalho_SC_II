import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 51.25, 426.609, 885.598]

G = control.tf(num,den) #Funcao de transferencia
control.sisotool(G)
plt.show()
