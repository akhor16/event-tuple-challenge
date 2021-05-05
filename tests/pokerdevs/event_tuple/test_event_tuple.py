import pytest
import logging
import calendar
import time
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_user_clicked_on_button_events():
    yield event_tuple.UserClickedOnButtonEvent(button_id = "close_button", event_type = "UserClickedOnButton")
    yield event_tuple.UserClickedOnButtonEvent("UserClickedOnButton", "close_button")


def generate_test_user_long_pressed_events():
    yield event_tuple.UserLongPressedEvent(y = 420, event_type = "UserLongPressed", x = 88)
    yield event_tuple.UserLongPressedEvent("UserLongPressed", 10, 48)


def serialize_event(event):
    return f"Event '{event.event_type()}' occurred at {event.timestamp()} with ID: {event.event_id()}"


def test_user_clicked_on_button():
    logger.info(f"Starting the test !")
    events = list(generate_test_user_clicked_on_button_events())
    event_0 = events[0]
    logger.info(event_0.event_id())


    timestamp = calendar.timegm(time.gmtime())
    assert event_0.timestamp() > timestamp - 60 and event_0.timestamp() < timestamp + 60
    assert event_0.event_type() == "UserClickedOnButton"
    assert event_0.button_id() == "close_button"
    info_text = serialize_event(event_0)
    logger.info(info_text)

    event_1 = events[1]
    timestamp = calendar.timegm(time.gmtime())
    assert event_1.timestamp() > timestamp - 60 and event_1.timestamp() < timestamp + 60

    assert event_1.event_type() == "UserClickedOnButton"
    assert event_1.button_id() == "close_button"
    logger.info(serialize_event(event_1))

    
def test_user_long_pressed():
    events = list(generate_test_user_long_pressed_events())
    event_0 = events[0]
    timestamp = calendar.timegm(time.gmtime())
    assert event_0.timestamp() > timestamp - 60 and event_0.timestamp() < timestamp + 60
    assert event_0.event_type() == "UserLongPressed"
    assert event_0.x() == 88
    assert event_0.y() == 420
    logger.info(serialize_event(event_0))

    event_1 = events[1]
    timestamp = calendar.timegm(time.gmtime())
    assert event_1.timestamp() > timestamp - 60 and event_1.timestamp() < timestamp + 60

    assert event_1.event_type() == "UserLongPressed"
    assert event_1.x() == 10
    assert event_1.y() == 48
    logger.info(serialize_event(event_1))
