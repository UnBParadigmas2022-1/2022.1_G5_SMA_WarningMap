from mesa import Agent


class WalkerAgent(Agent):
    grid = None
    x = None
    y = None
    moore = True

    def __init__(self, unique_id, pos, model, moore=True):
        super().__init__(unique_id, model)
        self.pos = pos
        self.moore = moore

    def random_move(self):
        if self.pos is not None:
            next_moves = self.model.grid.get_neighborhood(
                self.pos, self.moore, True
            )
            next_move = self.random.choice(next_moves)
            self.model.grid.move_agent(self, next_move)
