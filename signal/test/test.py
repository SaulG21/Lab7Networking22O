#script para graficar una señal senoidal.
import matplotlib.pyplot as pl
from numpy import arange, sin, pi

amplitud = 1
frecuencia = 1
fase = 1


x=arange(0.0, 2*pi+0.01, 0.01)
y = amplitud*sin(2*pi*frecuencia*x + fase)

pl.plot(x,y)
pl.grid("true")
pl.title("Señal senoidal")
pl.ylabel("Amplitud")
pl.xlabel("tiempo")
pl.show()