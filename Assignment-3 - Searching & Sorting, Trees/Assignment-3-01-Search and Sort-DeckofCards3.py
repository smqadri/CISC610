from random import shuffle as s                                                 # Import shuffle function from random module
import bubble_sort as bs                                                        # Import bubble sort function from bubble_sort module



class Deck:                                                                     # Create a class for the deck of cards
    _suits = ["Diamonds", "Clubs", "Hearts", "Spades"]                          # Create a list of suits
    _sorted = False                                                             # Create a sorted variable
    _index_map = {}                                                             # Create an empty index map
    
    def __init__(self):                                                         # Create a deck of cards
        cards = []                                                              # Create an empty list of cards
        for s in self._suits:                                                   # Fill the deck with standard playing cards
            for val in range(1, 14):                                            # Loop through the values
                cards.append(self._Card(s, val))                                # Add the card to the deck
        self.cards = cards                                                      # Create a list of cards
        self._populate_index_map()                                              # Populate the index map

    def __iter__(self):                                                         # Create an iterator for the deck of cards
        return self.cards.__iter__()                                            # Return the iterator

    def __str__(self):  #TODO Fix this to state whether or not the deck is sorted or shuffled;
        return 'A deck of {self.size} cards.'.format(self=self)                 # Return the size of the deck


    @property                                                                   # Property to get the length of the cards list
    def size(self):                                                             # Property to get the length of the cards list
        return self.cards.__len__()                                             # Return the length of the cards list

    @property  #TODO Implement a method to determine if the cards are sorted;
    def is_sorted(self):                                                        # Property to determine if the cards are sorted
        total_cards = self.size - 1                                             # Get the total number of cards
        sorted_cards = 0                                                        # Set the number of sorted cards to 0
        for i in range(0, total_cards):                                         # Loop through the cards
            if self.cards[i] < self.cards[i+1]:                                 # If the card is less than the next card
                sorted_cards += 1                                               # Add 1 to the number of sorted cards
        if (sorted_cards == total_cards):                                       # If all the cards are sorted
            return True                                                         # Return true
        else:                                                                   # If not all the cards are sorted
            return False                                                        # Return false


    def sort(self):  #TODO Implement a method to sort cards by suit and value;
        bs.bubble_sort(self.cards)                                              # Sort the cards using bubble sort
        self._populate_index_map()                                              # Update the index map




    def shuffle(self):                                                          # Method to put cards list in random order
        shuffled_deck = s(self.cards)                                           # Shuffle the cards
        self._populate_index_map()                                              # Update the index map
        return shuffled_deck

    def search(self):  #TODO Implement a public search method;
        card = self._describe_card()                                            # Get the card to search for
        print("=====================================================")          # Divider
        print("=====================================================\n")        # Divider
        print("The card you searched for is: ", card)                           # Print the card
        index = self._index_map[card]                                           # Get the index of the card
        print("Found the card at index position: ", self._index_map[card])      # Print the index of the card


    def _describe_card(self):                                                   # User facing private function to create a card to search for
        print("What suit is the card?")                                         # Pick a suit
        prompt = ""
        i = 1
        for suit in self._suits:                                                # Build prompt to pick suit
            prompt +='{}. {}\n'.format(i, suit)                                 # Add the suit to the prompt
            i += 1
        while True:
            s = int(input(prompt))                                              # Collect user info for suit
            v = int(input("Enter a number from 1 to 13 (1 = Ace, 11 = Jack, 12 = Queen, 13 = King): \n")) # Collect user info for value
            if s in [1, 2, 3, 4] and v in [x for x in range(1, 14)]:            # If the suit and value are valid
                card = self._Card(self._suits[s - 1], v)                        # Create the card
                #print(card)  #TODO Remove this; only here for debugging.
                break
            print("Invalid card, try again")                                    # If invalid try again
        return card

    def _populate_index_map(self):                                              # Private function to populate the index map
        self._index_map.clear()                                                 # Clear the index map
        # key is the card, value is the index of card
        for i in range (self.size):                                             # Loop through the cards
            self._index_map[self.cards[i]]=i                                    # Add the card and index to the index map

    class _Card: # Private inner class to create a Card
        _suits = ["Diamonds", "Clubs", "Hearts", "Spades"] 


        def __init__(self, suit, value): # Need a suit and a value. Will be two integers. 0-3 for suit and 1-13 for value
            self.suit = suit
            self.value = value

        def __str__(self): # Print override
            return '{self.value_name} of {self.suit}'.format(self=self)         # Return the value and suit of the card

        def __eq__(self, card):                                                 # Equals override
            if self.suit != card.suit:                                          # If the suits are not equal
                return False
            if self.value != card.value:                                        # If the values are not equal
                return False
            return True

        def __lt__(self, card):                                                 # Less than override
             if(self._suits.index(self.suit) < self._suits.index(card.suit)):   # If the suit is less than the card's suit
                 return True
             elif((self._suits.index(self.suit) == self._suits.index(card.suit)) and (self.value < card.value)):        # If the suit is equal to the card's suit and the value is less than the card's value
                 return True
             else:
                 return False     

        def _gt_(self,card):                                                    # Greater than override
            if(self._suits.index(self.suit) > self._suits.index(card.suit)):    # If the suit is greater than the card's suit
                 return True
            elif((self._suits.index(self.suit) == self._suits.index(card.suit)) and (self.value > card.value)):         # If the suit is equal to the card's suit and the value is greater than the card's value
                 return True
            else:
                 return False    


        @property # Get proper suit name
        def suit_name(self):                                                    # Get the suit name
            if self.suit == _suits[0]:                                          # If the suit is Diamonds, return 0
                return 0
            elif self.suit == _suits[1]:                                        # If the suit is Clubs, return 1
                return 1
            elif self.suit == _suits[2]:                                        # If the suit is Hearts, return 2
                return 2
            elif self.suit == _suits[3]:                                        # If the suit is Spades, return 3
                return 3
            else:
                raise ValueError()                                              # If the suit is not valid, raise a value error
        
        @property # Get proper value name
        def value_name(self):                                                   # Get the value name
            if self.value == 1:                                                 # If the card value is 1, return Ace
                return "Ace"
            elif self.value == 11:                                              # If the card value is 11, return Jack
                return "Jack"
            elif self.value == 12:                                              # If the card value is 12, return Queen
                return "Queen"
            elif self.value == 13:                                              # If the card value is 13, return King
                return "King"
            else:
                return self.value                                               # If the card value is not 1, 11, 12, or 13, return the value


            if self.value != other.value:       # If the values are not equal
                return self.value > other.value     # Return the greater value
            return self.suit_name > other.suit_name     # Return the greater suit name

        def __repr__(self):         # Representation override
            return self.__str__()       # Return the string representation of the card

        def __hash__(self):         # Hash override
            return hash((self.suit, self.value))        # Return the hash of the card



if __name__ == '__main__':  # Main method
    

    print("Welcome to the Deck of Cards program!")  # Welcome message
    print("The deck is currently empty.\n")  # Empty deck message
    
    print("=====================================================\n")  # Divider
    print("***Creating a deck of cards***\n")  # Creating deck message
    deck = Deck()  # Create empty Deck object
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
    print("\n=====================================================\n")  # Divider
    
    
    '''
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    deck.shuffle()                          # Shuffle the deck
    print("\nDeck after shuffling :")
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    print("\nTo check if deck is sorted or not: ", deck.is_sorted)
    deck.sort()                         # Sort the deck
    print("\nDeck of cards after sorting.\n")
    print([str(i) for i in deck.cards])     # Print the cards in the deck
    print("To check if deck is sorted or not: ", deck.is_sorted)
    
    deck.search()                   # Search for a card in the deck
'''