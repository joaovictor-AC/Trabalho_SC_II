import control as ctl
A = 0
B = 0
C = 0

num = [1]
den = [1, 51.25, 426.609, 885.598]
G = ctl.tf(num, den)

print(G)
