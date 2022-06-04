import pytest
import datetime 
from clases.schedule import Schedule

@pytest.fixture
def schedule_in_range():
    entry_time1 = datetime.time(10,00)
    departure_time1 = datetime.time(12,00)
    entry_time2 = datetime.time(10,00)
    departure_time2 = datetime.time(12,00)
    schedule1 =  Schedule(entry_time1, departure_time1)
    schedule2 = Schedule(entry_time2, departure_time2 )
    return schedule1, schedule2


def test_schedule_in_range(schedule_in_range):
    assert schedule_in_range[0].share_schedule(schedule_in_range[1])
    assert schedule_in_range[1].share_schedule(schedule_in_range[0])



@pytest.fixture
def schedule_not_in_range():
    entry_time1 = datetime.time(8,00)
    departure_time1 = datetime.time(9,00)
    entry_time2 = datetime.time(10,00)
    departure_time2 = datetime.time(12,00)
    schedule1 =  Schedule(entry_time1, departure_time1)
    schedule2 = Schedule(entry_time2, departure_time2)
    return schedule1, schedule2    

def test_schedule_not_range(schedule_not_in_range):
    assert not schedule_not_in_range[0].share_schedule(schedule_not_in_range[1])
    assert not schedule_not_in_range[1].share_schedule(schedule_not_in_range[0])