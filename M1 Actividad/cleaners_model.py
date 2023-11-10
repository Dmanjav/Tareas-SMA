from typing import Any
import mesa

class Garbage(mesa.Agent):
    def __init__(self, unique_id,model):
        super().__init__(unique_id,model)
        self.isFull = True
    def step(self):
        ...

class Cleaner_Bot(mesa.Agent):
    def __init__(self, unique_id,model):
        super().__init__(unique_id,model)
        self.model = model
    def step(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for cellmate in cellmates:
            if type(cellmate) == Garbage:
                if cellmate.isFull == True:
                    cellmate.isFull = False
                    self.model.num_garbage -= 1
                    return
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True,
            include_center = False)
        new_position = self.random.choice(possible_steps)
                
        self.model.grid.move_agent(self, new_position)
        

class Cleaners_Model(mesa.Model):
    def __init__(self,M,N, num_agents, percentage_garbage,stepsMax):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(M,N,False)
        self.schedule = mesa.time.RandomActivation(self)
        self.num_garbage = int((percentage_garbage * M * N) / 100)
        self.steps_max = stepsMax
        n = 0
        for i in range(self.num_garbage):
            temp = Garbage(i, self)
            x = self.random.randrange(1,self.grid.width)
            y = self.random.randrange(1,self.grid.height)
            isEmpty = self.grid.is_cell_empty((x,y))
            while(isEmpty == False):
                x = self.random.randrange(1,self.grid.width)
                y = self.random.randrange(1,self.grid.height)
                isEmpty = self.grid.is_cell_empty((x,y))
                
            n += 1
            self.schedule.add(temp)
            self.grid.place_agent(temp,(x,y))
        for i in range(num_agents):
            temp = Cleaner_Bot(i + self.num_garbage,self)
            self.grid.place_agent(temp,(0,0))
            self.schedule.add(temp)


    def step(self):
        self.steps_max -= 1
        self.schedule.step()
