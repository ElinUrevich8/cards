import random, re
from enum import Enum, IntEnum
from typing import Iterator


class Suit(Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"

class Rank(IntEnum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


SUIT_MAP = {
    'h': Suit.HEARTS,   'd': Suit.DIAMONDS,   'c': Suit.CLUBS,   's': Suit.SPADES,
    '♥': Suit.HEARTS,   '♦': Suit.DIAMONDS,   '♣': Suit.CLUBS,   '♠': Suit.SPADES
}

# Maps for printing (Enum -> Output)
SUIT_ASCII = {Suit.HEARTS: '♥', Suit.DIAMONDS: '♦', Suit.CLUBS: '♣', Suit.SPADES: '♠'}

RANK_ASCII = {
    Rank.ACE: 'A', Rank.KING: 'K', Rank.QUEEN: 'Q', Rank.JACK: 'J', Rank.TEN: '10',
    Rank.NINE: '9', Rank.EIGHT: '8', Rank.SEVEN: '7', Rank.SIX: '6', 
    Rank.FIVE: '5', Rank.FOUR: '4', Rank.THREE: '3', Rank.TWO: '2'
}

RANK_MAP = {
    'A': Rank.ACE, 'K': Rank.KING, 'Q': Rank.QUEEN, 'J': Rank.JACK, 
    'T': Rank.TEN, '10': Rank.TEN, # Handles the "10" case
    '9': Rank.NINE, '8': Rank.EIGHT, '7': Rank.SEVEN, '6': Rank.SIX, 
    '5': Rank.FIVE, '4': Rank.FOUR, '3': Rank.THREE, '2': Rank.TWO
}


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    @classmethod
    def random(cls) -> "Card":
        return Card(
          random.choice(list(Suit)),
          random.choice(list(Rank))
        )
    @classmethod
    def from_string(cls, hand_str: str) -> "Card":
        # The Pattern:
        # Part 1: (10|[2-9TJQKA]) -> Match "10" OR any single rank character
        # Part 2: ([shdc♥♦♣♠])    -> Match any valid suit character
        pattern = r"(10|[2-9TJQKA])([shdc♥♦♣♠])"
        
        # re.findall returns a list of tuple, e.g., [('A', 'h')]
        matches = re.findall(pattern, hand_str)

        if not matches:
            raise ValueError(f"Invalid hand string: {hand_str}")

        rank_str, suit_str = matches[0]
        rank = RANK_MAP[rank_str]
        suit = SUIT_MAP[suit_str]

        return cls(suit, rank)

    def __str__(self):
        return f"{RANK_ASCII[self.rank]}{SUIT_ASCII[self.suit]}"
    
    def __len__(self):
        return 1

    def __repr__(self):
        return f"Card(suit={self.suit.value}, rank={self.rank.value})"


class Deck:
    def __init__(self, shuffled: bool = True):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

        if shuffled:
            self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def draw_cards(self, count: int = 1) -> list[Card]:
        return [self.cards.pop() for _ in range(count)]

    def __str__(self):
        card_strs = [str(card) for card in self.cards]
        lines = []
        for i in range(0, len(card_strs), 13):
            line = ", ".join(card_strs[i : i + 13])
            lines.append(line)
        return ",\n".join(lines)

class Hand:
    """A hand is a collection of cards."""

    def __init__(self, cards: list[Card] = None):
        self.cards = cards

    @classmethod
    def random(cls, size: int = 5) -> "Hand":
        return Hand([Card.random() for _ in range(size)])

    @classmethod
    def from_string(cls, hand_str: str) -> "Hand":
        return Hand([Card.from_string(card_str) for card_str in hand_str.split()])

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self):
        if len(self) == 0:
            return "<Empty hand>"
        return ", ".join([str(card) for card in self.cards])
    
    def __repr__(self):
        return f"Hand(cards={self.cards})"

    def beats(self, other_hand: "Hand") -> bool:
        from comparehands import CompareHand 
        return CompareHand().beats(self, other_hand)

class Board:
    """A board is a collection of hands, each player has a board of typically 5 hands."""
    def __init__(self, deck: Deck):
        self.hands = []
        for _ in range(5):
            cards = deck.draw_cards(1) # Draw cards for ONE hand
            self.hands.append(Hand(cards)) # Create Hand object

    @classmethod
    def empty(cls) -> "Board":
        return Board([Hand() for _ in range(5)])

    @classmethod
    def random(cls, num_hands: int = 5) -> "Board":
        return Board([Hand.random() for _ in range(num_hands)])

    def __str__(self):
        # Create a nice indented list of hands:
        #   Hand 1: A♠, 10♥
        #   Hand 2: K♦, Q♣
        lines = []
        for i, hand in enumerate(self.hands, 1):
            lines.append(f"  Hand {i}: {hand}")
        return "\n".join(lines)
    

    #def add_card(self, card: Card, hand_index: int) -> None:
    #    self.hands[hand_index].add


if __name__ == "__main__":
    #hand = Hand.random()
    board = Board.random(5)

