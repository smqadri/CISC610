from random import shuffle as s
_suits = ["Diamonds", "Clubs", "Hearts", "Spades"] 

class Deck:
  _suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

  def __init__(self):
    cards = []
    for s in self._suits: # Fill the deck with standard playing cards
      for val in range(1, 14):
        cards.append(self._Card(s, val))
    self.cards = cards

  def __iter__(self):
    return self.cards.__iter__()

  def __str__(self): #TODO Fix this to state whether or not the deck is sorted or shuffled;
    return 'A deck of {self.size} cards'.format(self=self)

  @property # Property to get the length of the cards list
  def size(self):
    return len(self.cards)

  @property #TODO Implement a method to determine if the cards are sorted;
  def is_sorted(self):
    if str(self.cards[0]) == '10 of Diamonds' and str(self.cards[-1])== 'Queen of Spades':
      return True
    else:
      return False 

  def sort(self): #TODO Implement a method to sort cards by suit and value;
    deck_cards={}
    for j in self._suits:
      li=[]
      for i in self.cards:
        if j in str(i).split():
          li.append(str(i))
      deck_cards[j] = li.copy()
    li=[]
    for i, j in deck_cards.items():
      self.quickSort(j,0,12)
      li.extend(j)
    self.cards = li
    
  def partition(self, un_a, f_i, l_i):
    pivot = un_a[f_i]
    pivotIndex = f_i
    index_of_LE = l_i
    less_than_PI = index_of_LE
    greater_than_PI = f_i + 1

    while True:
      while un_a[greater_than_PI] < pivot and greater_than_PI < l_i:
        greater_than_PI += 1
      while un_a[less_than_PI] > pivot and less_than_PI >= f_i:
        less_than_PI -= 1
      if greater_than_PI < less_than_PI:
        temp = un_a[greater_than_PI]
        un_a[greater_than_PI] = un_a[less_than_PI]
        un_a[less_than_PI] = temp
      else:
        break
    un_a[pivotIndex] = un_a[less_than_PI]
    un_a[less_than_PI] = pivot
    return less_than_PI

  def quickSort(self, un_a, first, last):
    if last - first <= 0:
      return
    else:
      pp = self.partition(un_a, first, last)
      self.quickSort(un_a, first, pp-1)
      self.quickSort(un_a, pp+1, last)
  def shuffle(self): # Method to put cards list in random order
    shuffled_deck = s(self.cards)
    return shuffled_deck

  def search(self): #TODO Implement a public search method;
    card = self._describe_card()
  
  def _describe_card(self): # User facing private function to construct a card to search for
    print("What suit is the card?") # Pick a suit
    prompt = ""
    k=0
    i = 1
    for suit in self._suits: # Build prompt to pick suit
      prompt +='{}. {}\n'.format(i, suit)
      i += 1
    while True:
      k +=1
      s = int(input(prompt)) # Collect user info for suit
      v = int(input("Enter a number from 1 to 13 (1 = Ace, 11 = Jack, 12 = Queen, 13 = King): ")) # Collect user info for value
      if s in [1, 2, 3, 4] and v in [x for x in range(1, 14)]:
        card = self._Card(self._suits[s - 1], v)
        print(card) #TODO Remove this; only here for debugging.
        break
      print("Invalid card, try again") # If invalid try again   
    for j, i in enumerate(self.cards):
      if i==str(card):
          print(f"\n{card} is present in deck at index {j}.")


  class _Card: # Private inner class to construct a Card
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

if __name__ == '__main__': # Main method

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
