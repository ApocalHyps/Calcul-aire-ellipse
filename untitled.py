import numpy as np
import matplotlib.pyplot as plt

xlim = -5.7e9

xf, yf = -34e9,0
a,b = 115.4e9, 115.2e9

plt.plot([xf],[yf], 'o') # Soleil

T = np.linspace(0,2*np.pi, 100000)

# de Venus
plt.plot(xf + 108.20893e9*np.cos(T),yf + 108.20893e9*np.sin(T))

X,Y=a*np.cos(T),b*np.sin(T)

A=[]
for k in range(len(T)-1):
	h = np.sqrt((X[k+1]-X[k])**2+(Y[k+1]-Y[k])**2)
	base = np.sqrt((X[k]-xf)**2+(Y[k]-yf)**2)
	if X[k+1] < xlim: # Calcul de l'air jusqu'à que x < -5.7e10
		i=k
		break
	A.append(h*base/2)
print(sum(A), np.pi*a*b)
plt.plot(X,Y)
plt.plot([xlim],[Y[k+1]], 'o') #point
plt.show()