'''
' Tester code for LinkedHeap for Assignment 04
'''

from LinkedHeap import LinkedHeap

# SET THIS FLAG TO TRUE TO PAUSE OUTPUT
pause = False

#1) Test the LinkedHeap constructor
print("------------------------------------------------------------")
print("1) Test the LinkedHeap constructor")
print("------------------------------------------------------------")

lh = LinkedHeap()

if pause:
    input()
else:
    print()

#2) Test accessing an empty LinkedHeap
print("------------------------------------------------------------")
print("2) Test accessing an empty LinkedHeap")
print("------------------------------------------------------------")

try:
    print("None:\t= " + str(lh.peek()))
except:
    print("None:\t= None (via exception)")

try:
    print("None:\t= " + str(lh.delete()))
except:
    print("None:\t= None (via exception)")

if pause:
    input()
else:
    print()

#3) Test the LinkedHeap add method with ints as keys
print("------------------------------------------------------------")
print("3) Test the LinkedHeap add method with ints keys")
print("------------------------------------------------------------")

lh.insert(5, 10)

print("peek:   (5, 10)\t\t= " + str(lh.peek()))

lh.insert(2, 1)

print("peek:   (2, 1)\t\t= " + str(lh.peek()))

lh.insert(23, "My Password is Taco")

print("peek:   (2, 1)\t\t= " + str(lh.peek()))

lh.insert(-10, "Baklava")

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(0, "Should be second")

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(123, "Last")

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

if pause:
    input()
else:
    print()

lh.insert(-5, "Weird, right?")

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(0, "Should be first")

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(47, 555.55)

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(1, ["A", "list", "of", "stuff"])

print("peek:   (-10, 'Baklava')\t= " + str(lh.peek()))

lh.insert(-15, "¡Top!")

print("peek:   (-15, '¡Top!')\t= " + str(lh.peek()))

if pause:
    input()
else:
    print()

#4) Test the LinkedHeap min and remove_min methods
print("------------------------------------------------------------")
print("4) Test the LinkedHeap min and remove_min methods")
print("------------------------------------------------------------")

print("delete: (-15, '¡Top!')\t\t= " + str(lh.delete()))
print()

print("peek:   (-10, 'Baklava')\t\t= " + str(lh.peek()))
print("delete: (-10, 'Baklava')\t\t= " + str(lh.delete()))
print()

print("peek:   (-5, 'Weird, right?')\t= " + str(lh.peek()))
print("delete: (-5, 'Weird, right?')\t= " + str(lh.delete()))
print()

print("peek:   (0, 'Should be first')\t= " + str(lh.peek()))
print("delete: (0, 'Should be first')\t= " + str(lh.delete()))
print()

print("peek:   (0, 'Should be second')\t= " + str(lh.peek()))
print("delete: (0, 'Should be second')\t= " + str(lh.delete()))

if pause:
    input()
else:
    print()

print("peek:   (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(lh.peek()))
print("delete: (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(lh.delete()))
print()

print("peek:   (2, 1)\t\t\t= " + str(lh.peek()))
print("delete: (2, 1)\t\t\t= " + str(lh.delete()))
print()

print("peek:   (5, 10)\t\t\t= " + str(lh.peek()))
print("delete: (5, 10)\t\t\t= " + str(lh.delete()))
print()

print("peek:   (23, 'My Password is Taco')\t= " + str(lh.peek()))
print("delete: (23, 'My Password is Taco')\t= " + str(lh.delete()))
print()

print("peek:   (47, 555.55)\t\t= " + str(lh.peek()))
print("delete: (47, 555.55)\t\t= " + str(lh.delete()))
print()

print("peek:   (123, 'Last')\t\t= " + str(lh.peek()))
print("delete: (123, 'Last')\t\t= " + str(lh.delete()))

if pause:
    input()
else:
    print()

#5) Test the LinkedHeap add method with floats as keys
print("------------------------------------------------------------")
print("5) Test the LinkedHeap add method floats as keys")
print("------------------------------------------------------------")

lh.insert(5, 10)
lh.insert(2.15, 1)
lh.insert(23.5, "My Password is Taco")
lh.insert(-10.4, "Baklava")
lh.insert(0.6, "Should be second")
lh.insert(123.467, "Last")
lh.insert(-4.9, "Weird, right?")
lh.insert(0.6, "Should be first")
lh.insert(47, 555.55)
lh.insert(1.0000007, ["A", "list", "of", "stuff"])
lh.insert(-14.55, "¡Top!")

print("peek:   (-14.55, '¡Top!')\t= " + str(lh.peek()))
print()

print("delete: (-14.55, '¡Top!')\t\t  = " + str(lh.delete()))
print("delete: (-10.4, 'Baklava')\t\t  = " + str(lh.delete()))
print("delete: (-4.9, 'Weird, right?')\t  = " + str(lh.delete()))
print("delete: (0.6, 'Should be first')\t  = " + str(lh.delete()))
print("delete: (0.6, 'Should be second')\t  = " + str(lh.delete()))
print("delete: (1.0000007, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(lh.delete()))
print("delete: (2.15, 1)\t\t\t  = " + str(lh.delete()))
print("delete: (5, 10)\t\t\t  = " + str(lh.delete()))
print("delete: (23.5, 'My Password is Taco') = " + str(lh.delete()))
print("delete: (47, 555.55)\t\t  = " + str(lh.delete()))
print("delete: (123.467, 'Last')\t\t  = " + str(lh.delete()))
print()


try:
    print("peek:   None\t= " + str(lh.peek()))
except:
    print("peek:   None\t= None (via exception)")

if pause:
    input()
else:
    print()

#6) Test the LinkedHeap add method with strings as keys
print("------------------------------------------------------------")
print("6) Test the LinkedHeap add method strings as keys")
print("------------------------------------------------------------")

lh.insert("Baklava", 10)
lh.insert("apescat!", 1)
lh.insert("zoo", "My Password is Taco")
lh.insert("!2", "Baklava")
lh.insert("Apescat!", "Second")
lh.insert("æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦", "Last")
lh.insert("2.7", "Weird, right?")
lh.insert("Apescat!", "First")
lh.insert("åpescat!", 555.55)
lh.insert("apes", ["A", "list", "of", "stuff"])
lh.insert("!!", "¡Top!")

print("peek:   ('!!', '¡Top!')\t= " + str(lh.peek()))
print()

print("delete: ('!!', '¡Top!')\t\t  = " + str(lh.delete()))
print("delete: (!2, 'Baklava')\t\t  = " + str(lh.delete()))
print("delete: ('2.7', 'Weird, right?')\t  = " + str(lh.delete()))
print("delete: ('Apescat!', 'First')\t  = " + str(lh.delete()))
print("delete: ('Apescat!', 'Second')\t  = " + str(lh.delete()))
print("delete: ('Baklava', 10)\t\t  = " + str(lh.delete()))
print("delete: ('apes', ['A', 'list', 'of', 'stuff'])\n\t  = " + str(lh.delete()))
print("delete: ('apescat!', 1)\t\t  = " + str(lh.delete()))
print("delete: ('zoo', 'My Password is Taco')= " + str(lh.delete()))
print("delete: ('åpescat!', 555.55)\t  = " + str(lh.delete()))
print("delete: ('æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦', 'Last') = " + str(lh.delete()))
print()

try:
    print("peek:   None\t= " + str(lh.peek()))
except:
    print("peek:   None\t= None (via exception)")

if pause:
    input()
else:
    print()

#7) Try to test the underlying heap structure. MAY NOT WORK!
print("------------------------------------------------------------")
print("7) Try to test the underlying heap structure. MAY NOT WORK!")
print("------------------------------------------------------------")

lh.insert(5, 10)
lh.insert(2, 1)
lh.insert(47, 555.55)
lh.insert(23, "My Password is Taco")
lh.insert(0, "Should be second")
lh.insert(123, "Last")
lh.insert(-5, "Weird, right?")
lh.insert(0, "Should be first")
lh.insert(-10, "Baklava")
lh.insert(1, ["A", "list", "of", "stuff"])
lh.insert(-15, "¡Top!")

pointer = None

if pointer is None:
    try:
        pointer = lh._root
    except:
        pass

if pointer is None:
    try:
        pointer = lh.root
    except:
        pass

if pointer is None:
    try:
        pointer = lh._root_node
    except:
        pass

if pointer is None:
    try:
        pointer = lh.root_node
    except:
        pass

if pointer is None:
    try:
        pointer = lh._r
    except:
        pass

if pointer is None:
    try:
        pointer = lh.r
    except:
        pass

if pointer is None:
    try:
        pointer = lh._head
    except:
        pass

if pointer is None:
    try:
        pointer = lh.head
    except:
        pass

if pointer is None:
    try:
        pointer = lh._head_node
    except:
        pass

if pointer is None:
    try:
        pointer = lh.head_node
    except:
        pass

if pointer is None:
    try:
        pointer = lh._data
    except:
        pass

if pointer is None:
    try:
        pointer = lh.data
    except:
        pass

if pointer == None:
    print("Root node unidentified. Check the internal structure.")
else:
    print("Element of each node will be printed each time it's seen")
    print("\tusing a depth-first search")
    print("------------------------------------------------------------")
    print("(-15, '¡Top!')\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_left()
    print("(-10, 'Baklava')\t= " + str(pointer.get_element()))
    pointer = pointer.get_left()
    print("(0, 'Should be first')\t= " + str(pointer.get_element()))
    pointer = pointer.get_left()
    print("(23, 'My Password is Taco')\t= " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))
    print()

    pointer = pointer.get_parent()
    print("(0, 'Should be first')\t= " + str(pointer.get_element()))
    pointer = pointer.get_right()
    print("(2, 1)\t\t\t= " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))
    print()

    pointer = pointer.get_parent()
    print("(0, 'Should be first')\t= " + str(pointer.get_element()))
    pointer = pointer.get_parent()
    print("(-10, 'Baklava')\t= " + str(pointer.get_element()))
    pointer = pointer.get_right()
    print("(-5, 'Weird, right?')\t= " + str(pointer.get_element()))
    pointer = pointer.get_left()
    print("(5, 10)\t\t\t= " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))

    if pause:
        input()
    else:
        print()

    pointer = pointer.get_parent()
    print("(-5, 'Weird, right?')\t= " + str(pointer.get_element()))
    pointer = pointer.get_right()
    print("(1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))
    print()

    pointer = pointer.get_parent()
    print("(-5, 'Weird, right?')\t= " + str(pointer.get_element()))
    pointer = pointer.get_parent()
    print("(-10, 'Baklava')\t= " + str(pointer.get_element()))
    pointer = pointer.get_parent()
    print("(-15, '¡Top!')\t\t= " + str(pointer.get_element()))
    pointer = pointer.get_right()
    print("(0, 'Should be second')\t= " + str(pointer.get_element()))
    pointer = pointer.get_left()
    print("(123, 'Last')\t\t= " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))
    print()

    pointer = pointer.get_parent()
    print("(0, 'Should be second')\t= " + str(pointer.get_element()))
    pointer = pointer.get_right()
    print("(47, 555.55)\t\t= " + str(pointer.get_element()))
    print("leaf.get_left()\t\t= " + str(pointer.get_left()))
    print("leaf.get_right()\t= " + str(pointer.get_right()))
    print()

    pointer = pointer.get_parent()
    print("(0, 'Should be second')\t= " + str(pointer.get_element()))
    pointer = pointer.get_parent()
    print("(-15, '¡Top!')\t\t= " + str(pointer.get_element()))
    print("root.get_parent()\t= " + str(pointer.get_parent()))
