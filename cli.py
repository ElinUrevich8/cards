#!/usr/bin/env python
"""
Simple CLI Game Template
"""

from card import Deck, Board, Hand
import sys

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.board = Board(deck)
    
    def __str__(self):
        # Print the name, then a newline, then the board's string representation
        return f"{self.name}:\n{self.board}"
    
    def __repr__(self):
        return f"Player(name={self.name}, board={self.board})"
        

class Game:
    """Base game class with core game loop functionality."""
    
    def __init__(self):
        self.running = True
        self.score = 0
        self.players = []
        self.deck = Deck()
        
    def display_welcome(self):
        """Display welcome message."""
        print("=" * 40)
        print("Welcome to the Game!")
        print("=" * 40)
        print()
        
    def display_menu(self):
        """Display game menu."""
        print("\n--- Menu ---")
        print("1. Play")
        print("2. Instructions")
        print("3. Quit")
        print()
        
    def get_user_input(self, prompt: str) -> str:
        """Get input from user with error handling."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGame interrupted. Goodbye!")
            sys.exit(0)
            
    def handle_menu_choice(self, choice: str):
        """Handle menu selection."""
        if choice == "1":
            self.play()
        elif choice == "2":
            self.show_instructions()
        elif choice == "3":
            self.quit()
        else:
            print("Invalid choice. Please try again.")
            
    def play(self):
        """Main game logic - override in subclasses."""
        print("\nGame started!")
        name1 = self.get_user_input("Choose a name for the first player: ")
        name2 = self.get_user_input("Choose a name for the second player: ")
        player1 = Player(name1, self.deck)
        player2 = Player(name2, self.deck)
        self.players.append(player1)
        self.players.append(player2)
        print(f"printing both players\n{player1}\n{player2}")
        print("Game ended. Score: 0")
        
    #TODO polish later    
    def show_instructions(self):
        """Display game instructions."""
        print("\n--- Instructions ---")
        print(f"This is a chinese poker game. \n Each player has 5 hands, and in each turn the player decides in which hand to put the card.\n \
            You can't put a card in a hand if you haven't finished all the hands.\n \
            The game ends when all the hands are finished.\n \
            The player with the best hands wins.\n \
            The hands are evaluated using standart pocker rules.")
        print()
        
    def quit(self):
        """Exit the game."""
        print("\nThanks for playing! Goodbye!")
        self.running = False
        
    def run(self):
        """Main game loop."""
        self.display_welcome()
        
        while self.running and len(self.players) < 2:
            self.display_menu()
            choice = self.get_user_input("Enter your choice: ")
            self.handle_menu_choice(choice)

def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
