import numpy as np
import matplotlib.pyplot as plt

# Gerar uma matriz 10x10 de números aleatórios inteiros entre -255 e 255
random_matrix = np.random.randint(-255, 256, (183, 275))

# Criar o colormap com a faixa de valores de -255 a 255
plt.imshow(random_matrix, cmap='seismic', vmin=-255, vmax=255)
plt.colorbar()
plt.title('Matriz de Números Aleatórios entre -255 e 255')
plt.show()