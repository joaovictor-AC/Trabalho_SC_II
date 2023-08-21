import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 51.25, 426.609, 885.598]

sys = control.tf(num, den)

control.nichols(sys, omega=None, grid=True)
plt.grid(True)
plt.title('Nichols')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()
