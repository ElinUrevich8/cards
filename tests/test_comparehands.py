import pytest
from comparehands import CompareHand

@pytest.mark.parametrize("hand1_str, hand2_str, expected_result", 
[
    ("Ah Kh Qh Jh Th", "2h 2d 2c 3s 4d", True), # Royal Flush beats triple 2 
    ("Kc Kd 5h 2s 3c", "Ah Ks Qd Js Ts", False), # Pair of kings doesn't beat royal flush
    ("Ks Kd Ah 5c 2d", "Kh Kc Qs 5h 2s", True), # Pair of kings vs Pair of Kings, Kicker Ace beats Queen
    ("Ks Kd Ah 5c 2d", "Kh Kc As 5h 2s", False), # Same set of cards, a tie
    ("Ks Kd Ah 6c 2d", "Kh Kc As 5h 2s", True), # Pair of Kings vs Pair of Kings, Kicker 6 beats 5
])

def test_beats(create_hand, hand1_str, hand2_str, expected_result):
    h1 = create_hand(hand1_str)
    h2 = create_hand(hand2_str)
    
    assert h1.beats(h2) == expected_result