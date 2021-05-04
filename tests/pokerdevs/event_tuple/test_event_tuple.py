import pytest
import logging
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_user_clicked_on_button_events():
    yield event_tuple.UserClickedOnButtonEvent(timestamp = 1619579189, event_id = "k3196505-99hh-55z5-555a-9d31f3z253v4", button_id = "close_button", event_type = "UserClickedOnButton")
    yield event_tuple.UserClickedOnButtonEvent("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "UserClickedOnButton", "close_button")


def generate_test_user_long_pressed_events():
    yield event_tuple.UserLongPressedEvent(y = 420, event_id = "2s5ss900-a8bb-a8bb-a8bb-6q5kk89ggggg", timestamp = 1619146778, event_type = "UserLongPressed", x = 88)
    yield event_tuple.UserLongPressedEvent("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, "UserLongPressed", 10, 48)

def serialize_event(event):
    return f"Event '{event.event_type()}' occurred at {event.timestamp()} with ID: {event.event_id()}"


def test_user_clicked_on_button():
    logger.info(f"Starting the test !")
    events = list(generate_test_user_clicked_on_button_events())
    event_0 = events[0]
    assert event_0.event_id() == "k3196505-99hh-55z5-555a-9d31f3z253v4"
    assert event_0.timestamp() == 1619579189
    assert event_0.event_type() == "UserClickedOnButton"
    assert event_0.button_id() == "close_button"
    assert serialize_event(event_0) == "Event 'UserClickedOnButton' occurred at 1619579189 with ID: k3196505-99hh-55z5-555a-9d31f3z253v4"

    event_1 = events[1]
    assert event_1.event_id() == "b5796505-68fd-40d5-814a-9d31f3f084b0"
    assert event_1.timestamp() == 1619146052
    assert event_1.event_type() == "UserClickedOnButton"
    assert event_1.button_id() == "close_button"
    assert serialize_event(event_1) == "Event 'UserClickedOnButton' occurred at 1619146052 with ID: b5796505-68fd-40d5-814a-9d31f3f084b0"
    
    
def test_user_long_pressed():
    events = list(generate_test_user_long_pressed_events())
    event_0 = events[0]
    assert event_0.event_id() == "2s5ss900-a8bb-a8bb-a8bb-6q5kk89ggggg"
    assert event_0.timestamp() == 1619146778
    assert event_0.event_type() == "UserLongPressed"
    assert event_0.x() == 88
    assert event_0.y() == 420
    assert serialize_event(event_0) == "Event 'UserLongPressed' occurred at 1619146778 with ID: 2s5ss900-a8bb-a8bb-a8bb-6q5kk89ggggg"

    event_1 = events[1]
    assert event_1.event_id() == "1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf"
    assert event_1.timestamp() == 1619146123
    assert event_1.event_type() == "UserLongPressed"
    assert event_1.x() == 10
    assert event_1.y() == 48
    assert serialize_event(event_1) == "Event 'UserLongPressed' occurred at 1619146123 with ID: 1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf"
    