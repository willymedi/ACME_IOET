from abc import abstractmethod
from abc import ABCMeta
from clases.employee_schedule import EmployeeSchedule
from typing import List

class ShowResults(metaclass=ABCMeta):
    @abstractmethod
    def show(self, employee_schedules: List[EmployeeSchedule]  ):
        pass
