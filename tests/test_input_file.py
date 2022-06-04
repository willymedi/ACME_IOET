from clases.input_file import InputFile
from clases.schedule import Schedule
import pytest
from clases.employee_schedule import EmployeeSchedule
import datetime
from unittest.mock import patch, mock_open
from interfaces.input_data import InputData

text = """RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
            RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
            ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
            ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"""

def test_validate_success_schedule():
    input : InputData =  InputFile("prueba.txt")
    assert input.validate_schedule("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00") 
    
def test_validate_fail_schedule():
    input : InputData =  InputFile("prueba.txt")
    assert not input.validate_schedule("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00") 

def test_get_schedule():
    input : InputData =  InputFile("prueba.txt")
    schedule: Schedule = input.get_schedule("MO10:00-12:00")
    assert schedule.entry_time == datetime.time(10,00)
    assert schedule.departure_time == datetime.time(12, 00) 
    

def test_get_employee_schedule():
    input : InputData =  InputFile("prueba.txt")
    employee_schedule: EmployeeSchedule = input.get_employee_schedule("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00")
    assert employee_schedule.employee == "RENE"
    assert len(employee_schedule.schedules) == 5
    assert employee_schedule.schedules["TU"].departure_time == datetime.time(12, 00)


@patch("builtins.open", new_callable=mock_open, read_data=text)
def test_input_file_sucess(mocker_data):
    input : InputData =  InputFile("prueba.txt")
    employee_schedules = input.input()
    assert len(employee_schedules) == 3
    assert employee_schedules[1].employee == "ASTRID"
    print(employee_schedules[1].employee)
    assert employee_schedules[0].count_schedule_ocurrences(employee_schedules[1].schedules) == 2
    