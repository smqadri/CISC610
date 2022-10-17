
import deck_of_cards as dc                                                      # Import deck of cards function from deck_of_cards module

if __name__ == '__main__':
    print("Welcome to the Deck of Cards program!")  # Welcome message
    print("The deck is currently empty.\n")  # Empty deck message
    
    print("=====================================================\n")  # Divider
    print("***Creating a deck of cards***\n")  # Creating deck message
    deck = dc.Deck()  # Create empty Deck object
    print("The deck has {} cards.\n".format(deck.size))  # Print the size of the deck
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    print("\nThe deck is currently sorted: ", deck.is_sorted)  # Print if the deck is sorted
    
    print("\n=====================================================\n")  # Divider
    print("***Shuffling the deck***\n")  # Shuffle message
    deck.shuffle()  # Shuffle the deck
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    print("\nThe deck is currently sorted: ", deck.is_sorted)  # Print if the deck is sorted
    
    print("\n=====================================================\n")  # Divider
    print("***Sorting the deck***\n")  # Sort message
    deck.sort()  # Sort the deck
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    print("\nThe deck is currently sorted: ", deck.is_sorted)  # Print if the deck is sorted
    print("\n=====================================================\n")  # Divider

    print("***Searching for a card***\n")  # Search message
    card = deck.search()  # Search for a card
    print("The current state of the deck is: ", deck._deckstate)  # Print the state of the deck
    print("\n=====================================================\n")  # Divider
    

