import control
import matplotlib.pyplot as plt
import numpy

num = [1252]
den = [1, 51.25, 426.609, 885.598]

G = control.tf(num, den)
w = numpy.logspace(-1.5,4,10000)

control.bode(G, omega=w,
initial_phase=0, dB=True, Hz=False)
plt.show()
