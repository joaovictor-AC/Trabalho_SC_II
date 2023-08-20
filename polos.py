import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 51.25, 426.609, 885.598]

H = control.tf(num, den)
print(H)

(p, z) = control.pzmap(H)

print(p)
print(z)

plt.scatter(p.real, p.imag, marker='x', color='red', label='Polos')
plt.scatter(z.real, z.imag, marker='o', color='blue', label='Zeros')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.legend()
plt.grid()
plt.show()
