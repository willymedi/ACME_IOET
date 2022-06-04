import datetime

class Schedule:
    
    def __init__(self, entry_time: object, departure_time: object):
        self.entry_time = entry_time
        self.departure_time = departure_time
        
    def share_schedule(self, schedule_to_compare: object) -> bool:
        if self.entry_time >= schedule_to_compare.entry_time:
            return self.entry_time <= schedule_to_compare.departure_time
        else:
            return schedule_to_compare.entry_time <= self.departure_time