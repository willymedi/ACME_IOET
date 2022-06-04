from  interfaces.show_results import ShowResults
from clases.employee_schedule import EmployeeSchedule
from typing import List

class ShowConsoleResults(ShowResults):

    def show(self, employee_schedules: List[EmployeeSchedule] ):
        size_employe_schedules = len(employee_schedules)
        for i in range(size_employe_schedules-1):
            for j in range(i+1, size_employe_schedules):
                concurrences = employee_schedules[i].count_schedule_ocurrences(employee_schedules[j].schedules)
                print(f'{employee_schedules[i].employee}-{employee_schedules[j].employee}: {concurrences}')