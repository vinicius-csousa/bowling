from abc import ABC, abstractmethod

class Scorable(ABC):
    @abstractmethod
    def calculate_score(self) -> int:
        pass
