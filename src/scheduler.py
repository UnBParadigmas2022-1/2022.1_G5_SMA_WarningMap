from collections import defaultdict
from mesa.time import RandomActivation


class RandomActivationByType(RandomActivation):
    def __init__(self, model):
        super().__init__(model)
        self.agents_by_type = defaultdict(dict)

    def add(self, agent):
        self._agents[agent.unique_id] = agent
        agent_class = type(agent)
        self.agents_by_type[agent_class][agent.unique_id] = agent

    def remove(self, agent):
        del self._agents[agent.unique_id]
        agent_class = type(agent)
        del self.agents_by_type[agent_class][agent.unique_id]

    def step(self, by_type=True):
        if by_type:
            for agent_class in self.agents_by_type:
                self.step_type(agent_class)
            self.steps += 1
            self.time += 1
        else:
            super().step()

    def step_type(self, type):
        agent_keys = list(self.agents_by_type[type].keys())
        self.model.random.shuffle(agent_keys)
        for agent_key in agent_keys:
            self.agents_by_type[type][agent_key].step()

    def get_type_count(self, type_class):
        return len(self.agents_by_type[type_class].values())
