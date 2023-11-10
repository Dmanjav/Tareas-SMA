""" 
    Made by:
    Alan Alcántara Ávila
    Carlos Alberto Sánchez Calderón
    Diego Manjarrez Viveros
"""

from cleaners_model import Cleaners_Model
import seaborn as sns
import matplotlib.pyplot as plt
import time

ancho = 5
alto = 5
num_agents = 55
percentage_garbage = 55
stepsMax = 100
model = Cleaners_Model(ancho, alto, num_agents, percentage_garbage, stepsMax)
stepCounter = 0

inicio = time.time()
while model.num_garbage > 0 and stepCounter < stepsMax:
    model.step()
    stepCounter += 1
fin = time.time()
tiempo = fin - inicio

print("La simulación acabó en " + str("%.5f" % tiempo) + " segundos")
print("La simulación tiene: " + str(num_agents) + " aspiradoras, " +
      str(percentage_garbage) + "% de basura y tiene " + str(stepsMax) + " pasos.")
print("La simulacion acabo: framesTotales " + str(stepCounter) +
      ", basura restante: " + str(model.num_garbage))

time_needed = tiempo
percentage_clean_cells = (1 - model.num_garbage / (ancho * alto)) * 100
num_movements = stepCounter

# Create the charts
plt.figure(figsize=(15, 5))

# # Chart 1: Time needed
# plt.subplot(1, 3, 1)
# plt.bar(['Time'], [time_needed])
# plt.ylabel('Seconds')

# Chart 2: Percentage of clean cells
initial_percentage_clean_cells = percentage_garbage
final_percentage_clean_cells = (1 - model.num_garbage / (ancho * alto)) * 100
plt.subplot(1, 3, 2)
plt.bar(['Initial', 'Final'], [initial_percentage_clean_cells, final_percentage_clean_cells])
plt.ylabel('Percentage of Clean Cells')
plt.title('Clean Cells at the Beginning and End of Simulation')

# Chart 3: Number of movements
# plt.subplot(1, 3, 3)
# plt.bar(['Movements'], [num_movements])
# plt.ylabel('Number of Movements')

plt.show()
