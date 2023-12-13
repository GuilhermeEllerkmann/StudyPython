class WakeUp:
    def __init__(self, hour):
        self.hour = hour

    def piss(self, amount):
        return f'i pissed {amount}'
    
    def eat(self, amount):
        return f'i ate {amount}'
    
    def left_house(self, time):
        return f'i left the house at {time}'
    

acordei = WakeUp('11')
print(f'I woke up at {acordei.hour}')
print(acordei.piss('a loot'))
print(acordei.eat('bread and cereal'))
print(acordei.left_house('at two P.M.'))