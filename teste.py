import numpy as np
import matplotlib.pyplot as plt

# Gerar uma matriz 10x10 de números aleatórios inteiros entre -255 e 255
random_matrix = np.random.randint(-255, 256, (183, 275))

import numpy as np
import matplotlib.pyplot as plt

# Gerar uma matriz 183x275 de números aleatórios inteiros entre -255 e 255
random_matrix = np.random.randint(-255, 256, (183, 275))

# Criar o boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(random_matrix)
plt.title('Boxplot da matriz 183x275 de números aleatórios')
plt.xlabel('Valores')
plt.ylabel('Índices das linhas')
plt.show()

################################################################

# plt.hist(random_matrix, bins=10, edgecolor='black')

# # Adicionar título e rótulos aos eixos
# plt.title('Histograma de Exemplo')
# plt.xlabel('Valor')
# plt.ylabel('Frequência')

# # Mostrar o histograma
# plt.show()


# # Criar o colormap com a faixa de valores de -255 a 255
# plt.imshow(random_matrix, cmap='seismic', vmin=-255, vmax=255)
# plt.colorbar()
# plt.title('Matriz de Números Aleatórios entre -255 e 255')
# plt.show()