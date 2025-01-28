from abc import ABC, abstractmethod


class Scorable(ABC):
    """
    An abstract base class for objects that can calculate a score.

    Classes implementing this interface must define their own scoring logic
    by overriding the `calculate_score` method.
    """

    @abstractmethod
    def calculate_score(self) -> int:
        """
        Calculates the scores according to
        the rules of the class that implements it

        Returns:
            int: the calculated score
        """
        pass
