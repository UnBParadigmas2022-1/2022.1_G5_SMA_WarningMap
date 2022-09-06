from entities import WalkerAgent


class Thief(WalkerAgent):
    def __init__(self, unique_id, pos, model, moore):
        super().__init__(unique_id, pos, model, moore=moore)

    def step(self):
        self.random_move()
        if self.pos is not None:
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            if any(isinstance(obj, Person) for obj in this_cell):
                person = [obj for obj in this_cell if isinstance(obj, Person)][
                    0
                ]
                if not person.isVictim:
                    person.isVictim = True


class Police(WalkerAgent):
    def __init__(self, unique_id, pos, model, moore):
        super().__init__(unique_id, pos, model, moore=moore)

    def step(self):
        self.random_move()

        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        thief = [obj for obj in this_cell if isinstance(obj, Thief)]
        if len(thief) > 0:
            arrest_thief = self.random.choice(thief)
            self.model.grid.remove_agent(arrest_thief)


class Person(WalkerAgent):
    def __init__(self, unique_id, pos, model, moore):
        super().__init__(unique_id, pos, model, moore=moore)
        self.isVictim = False
        self.movements = 0

    def step(self):
        self.random_move()
        self.movements += 1
