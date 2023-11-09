from limpieza_model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": 0.5}

    # if agent.live == 1: #Rojos grandes cuando están vivos
        # portrayal["Color"] = "red"
        # portrayal["Layer"] = 0
    # else:
    #     portrayal["Color"] = "grey" #Grises pequeños al morir
    #     portrayal["Layer"] = 1
    #     portrayal["r"] = 0.1

    return portrayal

ancho = 15
alto = 15
aspiradoras = 10
basura = 5
grid = CanvasGrid(agent_portrayal, ancho, alto, 500, 500)
server = ModularServer(LimpiezaModel,
                       [grid],
                       "Aspiradoras Model",
                       {"N": aspiradoras, "M": basura,"width":ancho, "height":alto})
server.port = 8522 # The default
server.launch()
