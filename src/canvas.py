from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter

from agents import Police, Thief, Person
from models import PoliceThief

def agentPortrayal(agent):
    if agent is None:
        return
  
    portrayal = {
        "Filled": "true", 
        "Layer": 0, 
        "w": 1, 
        "h": 1
    }
    
    if type(agent) is Person:
        if agent.isVictim:
            portrayal["Shape"] = "assets/victim.png"
        else:
            portrayal["Shape"] = "assets/person.png"
    elif type(agent) is Thief:
        portrayal["Shape"] = "assets/thief.jpg"
    elif type(agent) is  Police:
        portrayal["Shape"] = "assets/policeman.png"
    
    return portrayal

canvas_element = CanvasGrid(agentPortrayal, 20, 20, 500, 500)

model_params = {
    "initial_thieves": UserSettableParameter(
        "slider", "Quantidade inicial de ladrões", 100, 10, 300
    ),
    "initial_polices": UserSettableParameter(
        "slider", "Quantidade de policiais", 50, 10, 300
    ),
    "initial_people": UserSettableParameter(
        "slider", "Quantidade de civis", 50, 10, 300
    ),
}

server = ModularServer(PoliceThief, [canvas_element], "Warning Map", model_params)

server.port = 8000