class WakeUp:
    def __init__(self) -> None:
        pass
    
    def woke_up(self, hour):
        return f'woke up at {hour}'

    def piss(self, amount):
        return f'i pissed {amount}'
    
    def eat(self, amount):
        return f'i ate {amount}'
    
    def left_house(self, time):
        return f'i left the house at {time}'
    

acordei = WakeUp()
print(acordei.woke_up('11'))
print(acordei.piss('a loot'))
print(acordei.eat('bread and cereal'))
print(acordei.left_house('at two P.M.'))