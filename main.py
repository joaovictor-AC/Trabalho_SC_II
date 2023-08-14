import control as ctl
A = 0
B = 0
C = 0

num = []
den = []
G = ctl.tf(num, den)

print(G)
