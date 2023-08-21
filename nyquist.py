import control
import matplotlib.pyplot as plt

num = [1252]
den = [1, 51.25, 426.609, 885.598]

sys = control.tf(num, den)

control.nyquist_plot(sys)
plt.grid(True)
plt.title('Nyquist')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()