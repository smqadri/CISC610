from random import shuffle as s
from bubble_sort import bubble_sort
_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

class Deck:
  _suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
  _sorted = False
  _index_map ={}

  def __init__(self):
    cards = []
    for s in self._suits: # Fill the deck with standard playing cards
      for val in range(1, 14):
        cards.append(self._Card(s, val))
    self.cards = cards
    self._populate_index_map()

  def __iter__(self):
    return self.cards.__iter__()

  def __str__(self): #TODO Fix this to state whether or not the deck is sorted or shuffled;
    return 'A deck of {self.size} cards'.format("sorted" if self._sorted else "shuffled", self=self)

  @property # Property to get the length of the cards list
  def size(self):
    return len(self.cards)

  @property #TODO Implement a method to determine if the cards are sorted;
  def is_sorted(self):
    return self._sorted

  def sort(self): #TODO Implement a method to sort cards by suit and value;
    bubble_sort(self.cards)
    self._populate_index_map()
    self._sorted = True

  def shuffle(self): # Method to put cards list in random order
    shuffled_deck = s(self.cards)
    self._sorted = False
    self._populate_index_map()
    return shuffled_deck

  def search(self): #TODO Implement a public search method;
    card = self._describe_card()
    print(card)
    # constant look up as we populate index map
    index = self._index_map[card]
    print(index)
    print(self.cards[index])

  def _describe_card(self): # User facing private function to create a card to search for
    print("What suit is the card?") # Pick a suit
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
        print(card) #TODO Remove this; only here for debugging.
        break
      print("Invalid card, try again") # If invalid try again
    return card


  def _populate_index_map(self):
    self._index_map.clear()
    # key is the card, value is the index of card
    for i in range (self.size):
      self._index_map[self.cards[i]]=i

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
      #compare value of card first then suits

    def __gt__(self, other):
      if self.value != other.value:
        return self.value > other.value
        return self.suit_name > other.suit_name

    def __repr__(self):
      return self.__str__()

    def __hash__(self):
      return hash((self.suit, self.value))

if __name__ == '__main__': # Main method
  '''deck = Deck() # Create empty Deck object
  print(deck)
  print(deck.cards)
  deck.sort()
  print(deck.cards)
  deck.shuffle()
  print(deck.cards)
  deck.search()'''

  deck = Deck() # Create empty Deck object
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