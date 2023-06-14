# Notas de Head First Object-Oriented Analysis and Design

## Apendix b

Capitulo repaso de conceptos de Orientación a objetos.

### Airplane class

```python
class Airplane:
    def __init__(self, speed):
        self._speed = speed

    def setSpeed(self, speed):
        self._speed = speed
    
    def getSpeed(self):
        return self._speed
```