from cleaners_model import Cleaners_Model

ancho = 5
alto = 5
num_agents = 0
percentage_garbage = 35
stepsMax = 100
model = Cleaners_Model(ancho,alto,num_agents,percentage_garbage,stepsMax)
stepCounter = 0
while model.num_garbage > 0 and stepCounter < stepsMax:
    model.step()
    stepCounter += 1
print("La simulacion acabo: framesTotales " + str(stepCounter) + ", basura restante: " + str(model.num_garbage))
