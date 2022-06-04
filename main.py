from interfaces.input_data import InputData
from interfaces.show_results import ShowResults
from typing import List
from clases.employee_schedule import EmployeeSchedule
from clases.input_file import InputFile
from clases.show_console_results import ShowConsoleResults



input_file: InputData =  InputFile("prueba.txt")
employee_schedules: List[EmployeeSchedule] =  input_file.input()
show_results: ShowResults = ShowConsoleResults()
show_results.show(employee_schedules)
