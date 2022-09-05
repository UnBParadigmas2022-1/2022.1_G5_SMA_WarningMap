import os

import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from settings import PORT
from agents import Person, Police, Thief
from models import PoliceThief


def agentPortrayal(agent):
    if agent is None:
        return

    portrayal = {"Filled": "true", "Layer": 0, "w": 1, "h": 1}
    base_path = os.path.dirname(__file__)
    if type(agent) is Person:
        if agent.isVictim:
            portrayal["Shape"] = f"{base_path}/assets/victim.png"
        else:
            portrayal["Shape"] = f"{base_path}/assets/person.png"
    elif type(agent) is Thief:
        portrayal["Shape"] = f"{base_path}/assets/thief.jpg"
    elif type(agent) is Police:
        portrayal["Shape"] = f"{base_path}/assets/policeman.png"

    return portrayal


canvas_element = CanvasGrid(agentPortrayal, 30, 30, 500, 500)

model_params = {
    "initial_thieves": mesa.visualization.Slider(
        "Quantidade de ladrões", 100, 10, 300
    ),
    "initial_polices": mesa.visualization.Slider(
        "Quantidade de policiais", 50, 10, 300
    ),
    "initial_people": mesa.visualization.Slider(
        "Quantidade de civis", 50, 10, 300
    ),
}

server = ModularServer(
    PoliceThief, [canvas_element], "Warning Map", model_params
)

server.port = PORT
