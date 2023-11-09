from cleaners_model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(agent):
    if type(agent) is Garbage:
      if agent.isFull:
        portrayal = {"Shape": "rect",
                    "w": 1,
                    "h": 1,
                    "Filled": "true",
                    "Layer": 0,
                    "Color": "gray"}
      else:
         portrayal = {"Shape": "rect",
                    "w": 1,
                    "h": 1,
                    "Filled": "true",
                    "Layer": 0,
                    "Color": "white"}
    if type(agent) is Cleaner_Bot:
        portrayal = {"Shape": "circle",
                "r": 1,
                "Filled": "true",
                "Layer": 0,
                "Color": "blue"}
    return portrayal
    

ancho = 10
alto = 10
grid = CanvasGrid(agent_portrayal, ancho, alto,300,300)
server = ModularServer(Cleaners_Model,
                       [grid],
                       "Cleaners",
                       {"M":ancho,"N":alto,
                         "num_agents":20, "percentage_garbage":35,
                         "stepsMax":100})
server.port = 8521 # The default
server.launch()
