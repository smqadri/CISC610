from random import shuffle as s



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
        if str(self.cards[0]) == '10 of Diamonds' and str(self.cards[-1])== 'Queen of Spades':
            return True
        else:
            return False 

    def partition(unsorted_array, first_index, last_index):
        pivot = unsorted_array[first_index]
        pivot_index = first_index
        index_of_last_element = last_index
        less_than_pivot_index = index_of_last_element
        greater_than_pivot_index = first_index + 1
        while True:
            while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
                greater_than_pivot_index += 1
            while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
                less_than_pivot_index -= 1
            if greater_than_pivot_index < less_than_pivot_index:
                temp = unsorted_array[greater_than_pivot_index]
                unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
                unsorted_array[less_than_pivot_index] = temp
            else:
                break
        unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
        unsorted_array[less_than_pivot_index] = pivot
        return less_than_pivot_index



    def sort(self):  #TODO Implement a method to sort cards by suit and value;
        deck_cards={}
        for j in self._suits:
            li=[]
            for i in self.cards:
                if j in str(i).split():
                    li.append(str(i))
            deck_cards[j] = li.copy()
        li=[]
        for i, j in deck_cards.items():
            self.quick_sort(j,0,12)
            li.extend(j)
        self.cards = li

    def quick_sort(unsorted_array, first, last):
        if last - first <= 0:
            return
        else:
            partition_point = partition(unsorted_array, first, last)
            self.quick_sort(unsorted_array, first, partition_point-1)
            self.quick_sort(unsorted_array, partition_point+1, last)



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
                print(card)  #TODO Remove this; only here for debugging.
                break
            print("Invalid card, try again") # If invalid try again
        return card
                

    class _Card: # Private inner class to create a Card
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

        @property # Get proper suit name
        def suit_name(self):
            if self.suit == _suits[0]:
                return 0
            elif self.suit == _suits[1]:
                return 1
            elif self.suit == _suits[2]:
                return 2
            elif self.suit == _suits[3]:
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

    
    #deck.shuffle()
    #deck.search()

    print([str(i) for i in deck.cards])
    deck.shuffle()
    print("\nDeck after shuffling :")
    print([str(i) for i in deck.cards])
    print("\nTo check if deck is sorted or not: ", deck.is_sorted)
    deck.sort()
    print("\nDeck of cards after sorting.\n",deck.cards)
    print("To check if deck is sorted or not: ", deck.is_sorted)
    print()
    deck.search()
