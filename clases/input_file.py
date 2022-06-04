from typing import List
from  interfaces.input_data import InputData
from clases.schedule import Schedule
from clases.employee_schedule import EmployeeSchedule
import datetime
from config.days_weeks import DAYS_OF_WEEK

class InputFile(InputData):
    
    
    def __init__(self, filename):
        self.filename = filename
    
    
    def validate_schedule(self, line: str) -> bool: 
        name, schedules = line.split("=")
        for schedule in schedules.split(","):
            is_valid_entry_time_hour = schedule[2:4].isdigit()
            is_valid_entry_time_minute = schedule[5:7].isdigit()
            is_valid_departure_time_hour = schedule[8:10].isdigit()
            is_valid_departure_time_minute = schedule[11:13].isdigit()
            is_valid_time = is_valid_entry_time_hour and is_valid_entry_time_minute and is_valid_departure_time_hour and is_valid_departure_time_minute
            if len(schedule) != 13 or (schedule[0:2].upper() not in DAYS_OF_WEEK) or not is_valid_time:
                return False
        return True
    
    def get_schedule(self, schedule_str: str ) -> Schedule:
        entry_time_str, departure_time_str = schedule_str[2:].split('-')
        entry_time = datetime.time(int(entry_time_str[0:2]), int(entry_time_str[3:5]))
        departure_time = datetime.time(int(departure_time_str[0:2]), int(departure_time_str[3:5]))
        return Schedule(entry_time, departure_time)
    
    def get_employee_schedule(self, line: str) -> EmployeeSchedule:
        name, schedules_str = line.split('=')
        schedules={}
        for schedule_str in schedules_str.split(','):
            day = schedule_str[:2].upper()
            schedule = self.get_schedule(schedule_str)
            schedules[day] = schedule
        return EmployeeSchedule(name, schedules)
    
    def input(self) -> List[EmployeeSchedule]:
        employee_schedules = []
        with open(self.filename, "r") as file:
            for line in file:
                if self.validate_schedule(line.strip()):    
                    employee_schedule = self.get_employee_schedule(line.strip())
                    employee_schedules.append(employee_schedule)
        return employee_schedules
                        
                    
                    
                               
