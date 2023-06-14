
class Airplane:
    def __init__(self):
        self._speed = 0

    def setSpeed(self, speed):
        self._speed = speed
    
    def getSpeed(self):
        return self._speed
    

class Jet(Airplane):

    def __init__(self):
        self.multiplier = 2

    def setSpeed(self, speed):
        super().setSpeed(speed * self.multiplier)

    def accelerate(self):
        current_speed = super().getSpeed()
        super().setSpeed(current_speed * self.multiplier)

biplane = Airplane()
biplane.setSpeed(212)
print(biplane.getSpeed())

boeing = Jet()
boeing.setSpeed(422)
print(boeing.getSpeed())

x = 0
while x < 4:
    boeing.accelerate()
    print(boeing.getSpeed())
    if boeing.getSpeed() > 5000:
        biplane.setSpeed(biplane.getSpeed() * 2)
    else:
        boeing.accelerate()
    x+=1
print(biplane.getSpeed())
