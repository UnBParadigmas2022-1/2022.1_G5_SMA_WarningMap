from mesa import Agent
from entities import Entity

class Thief(Entity):
    def __init__(self, unique_id, pos, model, moore):
        super().__init__(unique_id, pos, model, moore=moore)

    def step(self):
        self.random_move()

        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        person = [obj for obj in this_cell if isinstance(obj, Person)][0]

        if not person.isVictim:
            person.isVictim = True


class Police(Entity):
    def __init__(self, unique_id, pos, model, moore):
        super().__init__(unique_id, pos, model, moore=moore)

    def step(self):
        self.random_move()

        x, y = self.pos
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        thief = [obj for obj in this_cell if isinstance(obj, Thief)]
        if len(thief) > 0:
            arrest_thief = self.model.choice(thief)
            self.model.grid.remove_agent(arrest_thief)


class Person(Entity):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.isVictim = False

    def step(self):
        self.random_move()
