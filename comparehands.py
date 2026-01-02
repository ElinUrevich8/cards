from card import Hand
from strength import EvaluatedHand

class CompareHand:
    def beats(self, hand1: Hand, hand2: Hand) -> int:
        """Compare two hands and return:
        - 1 if hand1 is stronger
        - -1 if hand2 is stronger
        - 0 if they are equal
        """
        evaluated_hand1 = EvaluatedHand(hand1)
        evaluated_hand2 = EvaluatedHand(hand2)

        if evaluated_hand1.strength() > evaluated_hand2.strength():
            return 1
        elif evaluated_hand1.strength() < evaluated_hand2.strength():
            return -1
        # If strengths are equal, compare kickers
        for kicker1, kicker2 in zip(evaluated_hand1.kickers(), evaluated_hand2.kickers()):
            if kicker1 > kicker2:
                return 1
            elif kicker1 < kicker2:
                return -1

        # Continue with other hand rankings...

        return 0  # Placeholder for equal hands