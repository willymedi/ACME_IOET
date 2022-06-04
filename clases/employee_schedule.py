from clases.schedule import Schedule
from typing import Dict


class EmployeeSchedule:
    
    def __init__(self, employee: str, schedules: Dict[str, Schedule]):
        self.employee = employee
        self.schedules = schedules
    
    
    def count_schedule_ocurrences(self, employes_schedule_to_compare: Dict[str, Schedule]) -> int:
        count = 0
        for day, schedule in self.schedules.items():
            if day in employes_schedule_to_compare and  schedule.share_schedule(employes_schedule_to_compare[day]):
                count += 1
        return count
    
                