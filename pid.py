import control
import matplotlib.pyplot as plt

num = [1252]
den = [1, 51.25, 426.609, 885.598]

G = control.tf(num,den) #Funcao de transferencia
control.rootlocus_pid_designer(G,Kp0=1,Ki0=0.01,Kd0=0.05)

plt.show()
