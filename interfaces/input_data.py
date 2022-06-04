from abc import abstractmethod
from abc import ABCMeta


class InputData(metaclass=ABCMeta):
    @abstractmethod
    def input(self):
        pass
