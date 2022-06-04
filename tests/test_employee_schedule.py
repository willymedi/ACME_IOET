import pytest
import datetime 
from clases.schedule import Schedule
from clases.employee_schedule import EmployeeSchedule

@pytest.fixture
def employee_schedule_with_ocurrences():
    entry_time1 = datetime.time(10,15)
    departure_time1 = datetime.time(12,00)
    entry_time2 = datetime.time(10,00)
    departure_time2 = datetime.time(12,00)
    entry_time3 = datetime.time(13,00)
    departure_time3 = datetime.time(13,15)
    entry_time4 = datetime.time(12,00)
    departure_time4 = datetime.time(14,00)
    entry_time5 = datetime.time(20,00)
    departure_time5 = datetime.time(21,00)
    entry_time6 = datetime.time(20,00)
    departure_time6 = datetime.time(21,00)
    schedule1 =  Schedule(entry_time1, departure_time1)
    schedule2 = Schedule(entry_time2, departure_time2 )
    schedule3 = Schedule(entry_time3, departure_time3)
    schedule4 = Schedule(entry_time4, departure_time4)
    schedule5 = Schedule(entry_time5, departure_time5)
    schedule6 = Schedule(entry_time6, departure_time6)
    employee_schedule1 = EmployeeSchedule("Rene", {"MO":schedule1, "TH":schedule3, "SU": schedule1, "SU": schedule5 })
    employee_schedule2 = EmployeeSchedule("Tita", {"MO": schedule2, "TH":schedule4, "TU": schedule2, "SU": schedule6})
    return employee_schedule1, employee_schedule2

def test_employee_schedule_with_ocurrences(employee_schedule_with_ocurrences):
    assert employee_schedule_with_ocurrences[0].count_schedule_ocurrences(employee_schedule_with_ocurrences[1].schedules) == 3
    assert employee_schedule_with_ocurrences[1].count_schedule_ocurrences(employee_schedule_with_ocurrences[0].schedules) == 3




@pytest.fixture
def employee_schedule_without_ocurrences():
    entry_time1 = datetime.time(8,00)
    departure_time1 = datetime.time(9,00)
    entry_time2 = datetime.time(10,00)
    departure_time2 = datetime.time(12,00)
    schedule1 =  Schedule(entry_time1, departure_time1)
    schedule2 = Schedule(entry_time2, departure_time2)
    employee_schedule1 = EmployeeSchedule("Rene", {"TU": schedule1, "SU": schedule1})
    employee_schedule2 = EmployeeSchedule("Ramiro", {"TU":schedule2, "SA": schedule2})
    return employee_schedule1, employee_schedule2    

def test_schedule_not_range(employee_schedule_without_ocurrences):
    assert employee_schedule_without_ocurrences[0].count_schedule_ocurrences(employee_schedule_without_ocurrences[1].schedules) == 0
    assert employee_schedule_without_ocurrences[1].count_schedule_ocurrences(employee_schedule_without_ocurrences[0].schedules) == 0