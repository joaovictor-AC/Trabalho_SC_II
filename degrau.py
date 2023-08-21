import control
import matplotlib.pyplot as plt
import numpy


num = [1252]
den = [1, 51.25, 426.609, 885.598]
H = control.tf(num, den)
print(H)


t=numpy.arange(0,3,0.01)
r=1*numpy.ones(t.shape[0])

(t , c) = control.forced_response(H,t,r,X0=0)

plt.plot(t, r)
plt.plot(t, c)
plt.legend(['Entrada','Saída'])
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau unitário')
plt.grid()
plt.show()

