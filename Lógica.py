import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" En este proyecto final, aplicaremos conceptos de lógica binaria para filtrar
datos de una base de datos de encuestas en formato binario, donde cada
respuesta se representa como “sí” (1) o “no” (0).El propósito del proyecto es implementar
operadores lógicos como AND, OR y NOT para seleccionar, excluir o
combinar registros que cumplan ciertas condiciones, demostrando la
utilidad de la lógica binaria en la manipulación de datos."""
#Eso es un poco de la consigna que trabajamos para el proyecto de Lógica, y aplicamos en código solo el Filtro AND a modo de ejemplo. 

np.random.seed(0)
num_respuestas = 10
encuesta = {
    'ID': range(1, num_respuestas + 1),
    '¿El servicio al cliente fue satisfactorio?': np.random.choice(['Sí', 'No'], num_respuestas),
    '¿Fue fácil realizar la compra?': np.random.choice(['Sí', 'No'], num_respuestas),
    '¿La calidad del producto fue buena?': np.random.choice(['Sí', 'No'], num_respuestas),
    '¿Recomendaría este producto a alguien más?': np.random.choice(['Sí', 'No'], num_respuestas),
    '¿Volvería a comprar con nosotros?': np.random.choice(['Sí', 'No'], num_respuestas)
}
df = pd.DataFrame(encuesta)
df_binary = df.replace({'Sí': 1, 'No': 0})

#Filtro AND
filtro_and = df_binary[
    (df_binary['¿El servicio al cliente fue satisfactorio?'] == 0) & 
    (df_binary['¿Volvería a comprar con nosotros?'] == 0)
]
print("Clientes que respondieron 'No' en las preguntas 1 y 5:")
print(filtro_and)
pregunta_uno = df_binary[df_binary['¿El servicio al cliente fue satisfactorio?'] == 0].shape[0]
pregunta_cinco = df_binary[df_binary['¿Volvería a comprar con nosotros?'] == 0].shape[0]
print(f"Número de clientes insatisfechos con el servicio: {pregunta_uno}")
print(f"Número de clientes que no volverían a comprar: {pregunta_cinco}")

counts = df[['¿El servicio al cliente fue satisfactorio?', 
              '¿Fue fácil realizar la compra?', 
              '¿La calidad del producto fue buena?', 
              '¿Recomendaría este producto a alguien más?', 
              '¿Volvería a comprar con nosotros?']].apply(pd.Series.value_counts)

counts.plot(kind='bar')
plt.title('Distribución de Respuestas')
plt.ylabel('Número de Respuestas')
plt.xticks(rotation=0)
plt.show()