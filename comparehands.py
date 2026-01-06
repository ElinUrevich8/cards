from card import Hand
from strength import EvaluatedHand

class CompareHand:
    def beats(self, hand1: Hand, hand2: Hand) -> bool:
        """Compare two hands and return:
        - true if hand1 is stronger
        - false if hand2 is stronger or equal
        """
        evaluated_hand1 = EvaluatedHand(hand1)
        evaluated_hand2 = EvaluatedHand(hand2)

        if evaluated_hand1.strength > evaluated_hand2.strength:
            return True
        elif evaluated_hand1.strength < evaluated_hand2.strength:
            return False
        # If strengths are equal, compare kickers
        for kicker1, kicker2 in zip(evaluated_hand1.kickers, evaluated_hand2.kickers):
            if kicker1 > kicker2:
                return True
            elif kicker1 < kicker2:
                return False

        return False