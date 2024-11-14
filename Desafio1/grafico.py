import matplotlib.pyplot as plt
import numpy as np

# Datos
x = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
y = [2.5, 3.5, 4.2, 4.5, 4.6, 4.6, 4.4, 3.6, 2.6, 2.4, 2.5, 3.0, 3.9, 5.0, 5.6, 6.0, 6.2, 6.3, 6.2]

# Crear el gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos')
plt.title('Gráfico de Línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.legend()

# Configurar los ticks en los ejes
plt.xticks(np.arange(1.0, 10.5, 0.5))  # Eje X con intervalos de 0.5
plt.yticks(np.arange(2.0, 7.0, 0.5))    # Eje Y con intervalos de 0.5

# Mostrar el gráfico
plt.show()