from abc import ABC, abstractmethod

class ClassificationStrategy(ABC):
    """
    Strategy base para classificações.
    Aplicação do padrão Strategy.
    """
    @abstractmethod
    def classify(self, value):
        pass

class WaterClassification(ClassificationStrategy):
    def classify(self, value):
        if value < 25:
            return 'Ótima'
        elif 25 <= value <= 50:
            return 'Boa'
        elif 50 < value <= 75:
            return 'Regular'
        elif 75 < value <= 100:
            return 'Ruim'
        else:
            return 'Péssima'

class EnergyClassification(ClassificationStrategy):
    def classify(self, value):
        if value < 10:
            return 'Ótima'
        elif 10 <= value <= 20:
            return 'Boa'
        elif 20 < value <= 30:
            return 'Regular'
        elif 30 < value <= 40:
            return 'Ruim'
        else:
            return 'Péssima'

# Implementar outras classificações conforme necessário
