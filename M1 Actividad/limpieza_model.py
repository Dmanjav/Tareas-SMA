import mesa
from mesa.model import Model
import numpy as np


class AspiradoraAgent(mesa.Agent):
    """"Aspiradora que se va a mover de en un espacio determinado"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.position = [1, 1]
        
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        
    def aspira(self):
        cellmates = self.model.grid.get_neighbors(
            self.pos,
            moore=True,
            include_center=False)
        
        for mate in cellmates:
            if type(mate) == BasuraAgent:
                Multigrid.remove_agent(mate)
            

    def step(self):
        self.move()
        self.aspira()
        
class BasuraAgent(mesa.Agent):
    """Basura que va a ser removida por una aspiradora"""
    
    def __init__(self, unique_id, model) -> None:
        super().__init__(unique_id, model)
        self.live = np.random.choice([0,1])
            
class LimpiezaModel(mesa.Model):
    
    def __init__(self, N, M, width, height) -> None:
        self.num_aspiradoras = N
        self.num_basuras = M
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True #Para la visualizacion usando navegador
        
        cont = 0
        
        for i in range(self.num_aspiradoras):
            a = AspiradoraAgent(cont, self)
            self.schedule.add(a)
            cont += 1
            
        for i in range(self.num_basuras):
            b = BasuraAgent(cont, self)
            self.schedule.add(b)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b, (x, y))
            cont += 1
        
    def step(self):
        self.schedule.step()
