import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 51.25, 426.609, 885.598]

G = control.tf(num,den) #Funcao de transferencia

control.rlocus(G) #LGR

#Plotar a linha de \zeta
zeta = 0.625
#fator de amortecimento
px = 20     #ponto em x no terceiro quadrante onde finaliza a reta
M = px/zeta
w = (M**2-px**2)**0.5
plt.plot([0, -px],[0, w],linewidth=2)
#Rotina para plotar a reta do fator de amortecimento

plt.show()
