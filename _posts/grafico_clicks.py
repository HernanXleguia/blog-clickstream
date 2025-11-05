import matplotlib.pyplot as plt

# Datos de ejemplo
usuarios = ['U01', 'U02', 'U03', 'U04']
clicks = [120, 75, 180, 90]

# Crear gráfico de barras
plt.figure(figsize=(8,5))
plt.bar(usuarios, clicks, color='skyblue')
plt.xlabel('Usuarios')
plt.ylabel('Número de clics')
plt.title('Actividad de clics por usuario')
plt.savefig('clicks_por_usuario.png')  # Guardar imagen
plt.show()
