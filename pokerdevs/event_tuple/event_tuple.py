import calendar;
import time;
import secrets
import ulid, uuid
from math import floor

class UserClickedOnButtonEvent:

    def __init__(self, event_type, button_id):
        self.event_id_var = ulid.new()
        self.event_type_var = event_type
        self.button_id_var = button_id

    def event_id(self):
        return self.event_id_var

    def timestamp(self):
        #initial event_id_var.timestamp().int value is in milliseconds, it is converted to standard seconds timestamp
        return floor(self.event_id_var.timestamp().int/1000)
        
    def event_type(self):
        return self.event_type_var
        
    def button_id(self):
        return self.button_id_var


class UserLongPressedEvent:

    def __init__(self, event_type, x, y):
        self.event_id_var = ulid.new()
        self.event_type_var = event_type
        self.x_var = x
        self.y_var = y

    def event_id(self):
        return self.event_id_var

    def timestamp(self):
        #initial event_id_var.timestamp().int value is in milliseconds, it is converted to standard seconds timestamp
        return floor(self.event_id_var.timestamp().int/1000)
        
    def event_type(self):
        return self.event_type_var

    def x(self):
        return self.x_var

    def y(self):
        return self.y_var
    