from random import shuffle as s
#from bubble_sort import bubble_sort 


class Deck:
    _suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    
    def __init__(self):
        cards = []
        for s in self._suits:  # Fill the deck with standard playing cards
            for val in range(1, 14):
                cards.append(self._Card(s, val))
        self.cards = cards

    def __iter__(self):
        return self.cards.__iter__()

    def __str__(self):  #TODO Fix this to state whether or not the deck is sorted or shuffled;
        return 'A deck of {self.size} cards'.format(self=self)


    @property  # Property to get the length of the cards list
    def size(self):
        return len(self.cards)

    @property  #TODO Implement a method to determine if the cards are sorted;
    def is_sorted(self):
        total_cards = self.size-1
        sorted_cards = 0
        for i in range(0, total_cards):
            if self.cards[i] < self.cards[i+1]:
                sorted_cards += 1
            if(sorted_cards == 51):
                return True
            else:
                return False

    def sort(self):  #TODO Implement a method to sort cards by suit and value;
        #return bubble_sort(self)
        pass


    def shuffle(self):  # Method to put cards list in random order
        shuffled_deck = s(self.cards)
        return shuffled_deck

    def search(self):  #TODO Implement a public search method;
        card = self._describe_card()


    def _describe_card(self): # User facing private function to create a card to search for
        print("What suit is the card?")  # Pick a suit
        prompt = ""
        i = 1
        for suit in self._suits: # Build prompt to pick suit
            prompt +='{}. {}\n'.format(i, suit)
            i += 1
        while True:
            s = int(input(prompt)) # Collect user info for suit
            v = int(input("Enter a number from 1 to 13 (1 = Ace, 11 = Jack, 12 = Queen, 13 = King): ")) # Collect user info for value
            if s in [1, 2, 3, 4] and v in [x for x in range(1, 14)]:
                card = self._Card(self._suits[s - 1], v)
                print("You chose :")
                print(card)  #TODO Remove this; only here for debugging.
                if(self.is_sorted):
                    print("The card is at index :")
                    print(self.cards[(s -1)*13 + v -1])
                    return (s-1)*13 + v -1
                else:
                    total_cards = self.size
                    for i in range(0, total_cards):
                        if self.cards[i] == card:
                            print("The card is at index :")
                            print(self.cards[i])
                            return i
            print("Invalid card, try again") # If invalid try again
        return card
        

    class _Card: # Private inner class to create a Card
        _suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

        def __init__(self, suit, value): # Need a suit and a value. Will be two integers. 0-3 for suit and 1-13 for value
            self.suit = suit
            self.value = value

        def __str__(self): # Print override
            return '{self.value_name} of {self.suit}'.format(self=self)

        def __eq__(self, card): # Equals override
            if self.suit != card.suit:
                return False
            if self.value != card.value:
                return False
            return True

        def __lt__(self, card): # Less than override
            if(self._suits.index(self.suit) < self._suits.index(card.suit)):
                return True
            elif((self._suits.index(self.suit) == self._suits.index(card.suit)) and (self.value < card.value)):
                return True
            else:
                return False

        def __gt__(self, card):  # Greater than override
            if(self._suits.index(self.suit) > self._suits.index(card.suit)):
                return True
            elif((self._suits.index(self.suit) == self._suits.index(card.suit)) and (self.value > card.value)):
                return True
            else:
                return False

        @property # Get proper suit name
        def suit_name(self):
            if self.suit == self._suits[0]:
                return 0
            elif self.suit == self._suits[1]:
                return 1
            elif self.suit == self._suits[2]:
                return 2
            elif self.suit == self._suits[3]:
                return 3
            else:
                raise ValueError()
        
        @property # Get proper value name
        def value_name(self):
            if self.value == 1:
                return "Ace"
            elif self.value == 11:
                return "Jack"
            elif self.value == 12:
                return "Queen"
            elif self.value == 13:
                return "King"
            else:
                return self.value

    


if __name__ == '__main__':  # Main method
    deck = Deck()  # Create empty Deck object
    deck.shuffle()
    print("Is the deck sorted? :", deck.is_sorted)
    deck.search()
    deck.sort()
    print("Is the deck sorted? :", deck.is_sorted)
    deck.search()
    print("=====================================")
    print("=====================================")
    deck.shuffle()
    print("Is the deck sorted? :", deck.is_sorted)
    for card in deck:
        print(card)
    deck.sort()
    print("Is the deck sorted? :", deck.is_sorted)
    for card in deck:
        print(card)