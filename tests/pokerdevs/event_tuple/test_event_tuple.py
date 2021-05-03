import pytest
import logging
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_events():
    yield ("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "UserClickedOnButton", "close_button")
    yield ("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, "UserLongPressed", 340, 420)

def serialize_event(event):
    return f"Event '{event[2]}' occurred at {event[1]} with ID: {event[0]}"


def test_event_tuple():
    logger.info(f"Starting the test !")
    tup_click = list(generate_test_events())[0]
    assert tup_click[0] == "b5796505-68fd-40d5-814a-9d31f3f084b0"
    assert tup_click[1] == 1619146052
    assert tup_click[2] == "UserClickedOnButton"
    assert tup_click[3] == "close_button"
    assert serialize_event(tup_click) == "Event 'UserClickedOnButton' occurred at 1619146052 with ID: b5796505-68fd-40d5-814a-9d31f3f084b0"
    tup_press = list(generate_test_events())[1]
    assert tup_press[0] == "1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf"
    assert tup_press[1] == 1619146123
    assert tup_press[2] == "UserLongPressed"
    assert tup_press[3] == 340
    assert tup_press[4] == 420
    assert serialize_event(tup_press) == "Event 'UserLongPressed' occurred at 1619146123 with ID: 1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf"

    #pytest.fail(f"YOU NEED TO FINISH THIS")
    