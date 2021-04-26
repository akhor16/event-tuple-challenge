import pytest
import logging
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_events():
    raise NotImplementedError

def serialize_event(event):
    raise NotImplementedError



def test_event_tuple():
    logger.info(f"Starting the test !")
    pytest.fail(f"YOU NEED TO FINISH THIS")