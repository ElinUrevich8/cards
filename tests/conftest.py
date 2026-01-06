# file: tests/configtest.py
import pytest
from card import Card, Hand

@pytest.fixture
def create_hand():
    def _builder(hand_str):
        return Hand.from_string(hand_str)
    return _builder
