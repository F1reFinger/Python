import numpy as np

# a EDO
def f(x,y):
    return y*np.cos(x)

#pvi
x0 = 0
y0 = 1

#intervalo
a = 
b = 
N = 

#calculando h
h = (b - a)/N

#Vetores que irão acumular os pontos gerados
xi = [x0]
yi = [y0]

#iterando com método

for i in range(N):
    k1 = f(x0, y0)
    k2 = f(x0+ h, y0+h*k1)
    yk = y0 + 0.5*(k1 + k2) * h
    x0 = x0 + h
    y0 = yk
    print(f"({round(x0,2)} , {round(y0,2)})")
    #Adicionando os pontos nos vetores
    xi.append(round(x0,2))
    yi.append(round(yk,2))

print()
print(xi)
print(yi)