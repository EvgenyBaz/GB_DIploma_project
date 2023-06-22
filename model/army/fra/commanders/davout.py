from model.army.basic_commander import BasicCommander
class Davout(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "Marshal Lois-Nicolas Davout"
        self.cost = 150
        self.special = {'Combat attack +2 Dice. Decisive. Command range of 24". If Davout gives an order to any unit\
        in another commandr\'s command than that commander has a staff rating two less than normal in their following\
         turn for all orders other than Rally on Me orders. SR 9'}