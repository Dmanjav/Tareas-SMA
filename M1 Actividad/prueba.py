"""
    Made by:
    Alan Alcántara Ávila
    Carlos Alberto Sánchez Calderón
    Diego Manjarrez Viveros
"""

from cleaners_model import Cleaners_Model
import matplotlib.pyplot as plt
import time
import seaborn as sns

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

# Create the chart
plt.figure(figsize=(15, 5))

initial_percentage_clean_cells = percentage_garbage
final_percentage_clean_cells = (1 - model.num_garbage / (ancho * alto)) * 100
plt.subplot(1, 3, 2)
plt.bar(['Initial', 'Final'], [initial_percentage_clean_cells, final_percentage_clean_cells])
plt.ylabel('Percentage of Clean Cells')
plt.title('Clean Cells at the Beginning and End of Simulation')

plt.show()

garbage = model.datacollector.get_model_vars_dataframe()
# Plot the Gini coefficient over time
g = sns.lineplot(data=garbage)
g.set(title="Garbage over Steps")
plt.show()
