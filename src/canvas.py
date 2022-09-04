from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter

from agents import Police, Thief, Person

def agentPortrayal(agent):
    portrayal = {
        "Filled": "true", 
        "Layer": 0, 
        "w": 0.75, 
        "h": 0.75
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

canvas_element = CanvasGrid(agentPortrayal, 20, 20, 500, 500)

#TO-DO: Criar model params e atualizar no server 
server = ModularServer(, [canvas_element], "Warning Map", )

server.port = 8000