# Turn-Based Logic Implementation Plan

## 1. Core Logic (`card.py`)
Enable adding cards to specific hands and checking for completion.

### `Board` Class
- **Empty Initialization**: Allow initializing an empty board (currently it forces a random fill).
- **`add_card(card, hand_index)`**: Method to place a drawn card into a specific row (hand).
- **`is_full()`**: Method to check if all 5 hands are complete.

### `Hand` Class
- **`is_full()`**: Check to know when a row has reached its limit (usually 5 cards).

## 2. Game Loop (`cli.py`)
Convert the straight-through script into a turn-based loop.

### Initialization
- Start players with empty boards instead of pre-filled ones.

### The Loop (`Game.play`)
- **State Tracking**: Keep an index of the `current_player`.
- **Turn Sequence**:
    1.  **Draw**: Pop one card from the `Deck`.
    2.  **Display**: Show the card and the current state of the player's board.
    3.  **Input**: Ask the user which hand (0-4) to place the card in.
    4.  **Validate**: Ensure that specific hand isn't full yet.
    5.  **Update**: Add the card to the board.
    6.  **Switch**: Change `current_player` to the next person.
- **Termination**: Check at the end of each turn to see if both players' boards are full.
