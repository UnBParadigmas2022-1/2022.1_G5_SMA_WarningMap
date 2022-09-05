from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from agents import Police, Thief, Person
from scheduler import RandomActivationByType


class PoliceThief(Model):
    # Initial Values
    height = 30
    width = 30

    initial_thieves = 100
    initial_polices = 20

    description = "Model to create Police-Thief-Person relationship."

    def __init__(
        self,
        height=30,
        width=30,
        initial_thieves=100,
        initial_polices=20,
        initial_people=30,
    ):

        super().__init__()
        # Set parameters
        self.height = height
        self.width = width

        self.intial_thieves = initial_thieves
        self.initial_polices = initial_polices
        self.initial_people = initial_people

        self.schedule = RandomActivationByType(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.datacollector = DataCollector(
            {
                "Thief": lambda m: m.schedule.get_type_count(Thief),
                "Police": lambda m: m.schedule.get_type_count(Police),
                "Person": lambda m: m.schedule.get_type_count(Person),
            }
        )

        # Create thief:
        for i in range(self.intial_thieves):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            thief = Thief(self.next_id(), (x, y), self, True)
            self.grid.place_agent(thief, (x, y))
            self.schedule.add(thief)

        # Create police:
        for i in range(self.initial_polices):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            police = Police(self.next_id(), (x, y), self, True)
            self.grid.place_agent(police, (x, y))
            self.schedule.add(police)

        # Create person:
        for i in range(self.initial_people):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            person = Person(self.next_id(), (x, y), self, True)
            self.grid.place_agent(person, (x, y))
            self.schedule.add(person)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
