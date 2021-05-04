class UserClickedOnButtonEvent:
    # event_id_var
    # timestamp_var
    # event_type_var
    # button_id_var

    def __init__(self, event_id, timestamp, event_type, button_id):
        self.event_id_var = event_id
        self.timestamp_var = timestamp
        self.event_type_var = event_type
        self.button_id_var = button_id

    def event_id(self):
        return self.event_id_var

    def timestamp(self):
        return self.timestamp_var
        
    def event_type(self):
        return self.event_type_var
        
    def button_id(self):
        return self.button_id_var


class UserLongPressedEvent:
    # event_id_var
    # timestamp_var
    # event_type_var
    # x_var
    # y_var

    def __init__(self, event_id, timestamp, event_type, x, y):
        self.event_id_var = event_id
        self.timestamp_var = timestamp
        self.event_type_var = event_type
        self.x_var = x
        self.y_var = y

    def event_id(self):
        return self.event_id_var

    def timestamp(self):
        return self.timestamp_var
        
    def event_type(self):
        return self.event_type_var

    def x(self):
        return self.x_var

    def y(self):
        return self.y_var