import pytest
from comparehands import CompareHand
from enum import Enum

class HandCompareOutcome(Enum):
    WIN = 1
    LOSE = 2
    TIE = 3

@pytest.mark.parametrize("hand1_str, hand2_str, expected_result", 
[
    ("Ah Kh Qh Jh Th", HandFactory.three_of_a_kind(), HandCompareOutcome.WIN), # Royal Flush beats triple 2
    ("Kc Kd 5h 2s 3c", "Ah Ks Qd Js Ts", HandCompareOutcome.LOSE), # Pair of kings doesn't beat royal flush
    ("Ks Kd Ah 5c 2d", "Kh Kc Qs 5h 2s", HandCompareOutcome.WIN), # Pair of kings vs Pair of Kings, Kicker Ace beats Queen
    ("Ks Kd Ah 5c 2d", "Kh Kc As 5h 2s", HandCompareOutcome.LOSE), # Same set of cards, a tie
    ("Ks Kd Ah 6c 2d", "Kh Kc As 5h 2s", HandCompareOutcome.WIN), # Pair of Kings vs Pair of Kings, Kicker 6 beats 5
])

def test_beats(create_hand, hand1_str, hand2_str, expected_outcome):
    h1 = create_hand(hand1_str)
    h2 = create_hand(hand2_str)
    
    if (expected_outcome == HandCompareOutcome.WIN):
        assert h1.beats(h2) and not h2.beats(h1)
    elif (expected_outcome == HandCompareOutcome.LOSE):
        assert not h1.beats(h2) and h2.beats(h1)
    else:
        assert not h1.beats(h2) and not h2.beats(h1)


