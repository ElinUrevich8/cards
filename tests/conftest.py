# file: tests/configtest.py
import pytest
from card import Hand

@pytest.fixture
def create_hand():
    def _builder(hand_or_hand_str):
        if isinstance(hand_or_hand_str, Hand):
            return hand_or_hand_str
        elif isinstance(hand_or_hand_str, str):
            return Hand.from_string(hand_or_hand_str)
        else:
            raise ValueError("Invalid type for create_hand fixture")
    return _builder
