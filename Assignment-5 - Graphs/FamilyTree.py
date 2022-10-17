from graph import Graph

class Person:                                       # Person class
    def __init__(self, name, pid, gender, age):
        self.name = name
        self.id = pid
        self.age = age
        self.gender = gender
    
class FamilyTree:                                   # FamilyTree class
    def __init__(self):                             # Constructor
        self.graphTree = Graph()
    
    def addFamilyMember(self, name, gender, age, pid):      # Add a person
        try:
            assert (pid not in self.graphTree.personId),"Person already exists"
            assert (name not in self.graphTree.person),"Person already exists"
            newPerson = Person(name, pid, gender, age)
            self.graphTree.insert(newPerson)
        except AssertionError as msg:
            print(msg)

    def editFamilyMember(self, name, new_name, new_gender, new_age):        # Edit a person
        try:
            assert (name in self.graphTree.person),"Person not found"
            self.graphTree.edit(name, new_name, new_gender, new_age)
        except AssertionError as msg:
            print(msg)

    def addRelationship(self, name1, name2, relation):                      # Add a relation
        try:
            assert (name1 != name2),"Cannot add relation to self"
            self.graphTree.addRelation(name1, name2, relation)
        except AssertionError as msg:
            print(msg)

    def removeFamilyMember(self, name):                                     # Remove a person
        try:
            assert (name in self.graphTree.person),"Person not found"
            self.graphTree.remove(name)
        except AssertionError as msg:
            print(msg)

    def getPerson(self, name):                                              # Get a person
        try:
            assert(name in self.graphTree.person),"Person not found"
            self.graphTree.getPerson(name)
        except AssertionError as msg:
            print(msg)

    def print(self):                                                        # Print the family tree
        self.graphTree.print()

    




if __name__ == "__main__":
    
    familyTree_WH = FamilyTree()


    #Add family members
    familyTree_WH.addFamilyMember("Patrick Earnshaw", "M", "51","001")          
    familyTree_WH.addFamilyMember("Hannah Earnshaw", "F", "50","002")
    familyTree_WH.addFamilyMember("Catherine Earnshaw", "F", "22","003")
    familyTree_WH.addFamilyMember("Hindley Earnshaw", "M", "21","004")
    familyTree_WH.addFamilyMember("Andrew Linton", "M", "55","005")
    familyTree_WH.addFamilyMember("Dolores Linton", "F", "53","006")
    familyTree_WH.addFamilyMember("Isabella Linton", "F", "30","007")
    familyTree_WH.addFamilyMember("Edgar Linton", "M", "28","008")
    familyTree_WH.addFamilyMember("Heathcliff Linton", "M", "27","009")
    familyTree_WH.addFamilyMember("Frances Byler", "M", "21","010")
    familyTree_WH.addFamilyMember("Hareton Earnshaw", "M", "22","011")
    familyTree_WH.addFamilyMember("Cathy Linton", "F", "22","012")
    familyTree_WH.addFamilyMember("Linton HeathCliff", "M", "22","013")
    
    #Family1 Relations
    familyTree_WH.addRelationship("Patrick Earnshaw", "Hannah Earnshaw", "Spouse")
    familyTree_WH.addRelationship("Catherine Earnshaw", "Patrick Earnshaw", "Child")
    familyTree_WH.addRelationship("Catherine Earnshaw", "Hannah Earnshaw", "Child")
    familyTree_WH.addRelationship("Hindley Earnshaw", "Patrick Earnshaw", "Child")
    familyTree_WH.addRelationship("Hindley Earnshaw", "Hannah Earnshaw", "Child")
    familyTree_WH.addRelationship("Hindley Earnshaw", "Catherine Earnshaw", "Sibling")
    
    #Family2 Relations
    familyTree_WH.addRelationship("Andrew Linton", "Dolores Linton", "Divorced")
    familyTree_WH.addRelationship("Isabella Linton", "Andrew Linton", "Child")
    familyTree_WH.addRelationship("Isabella Linton", "Dolores Linton", "Child")
    familyTree_WH.addRelationship("Edgar Linton", "Andrew Linton", "Child")
    familyTree_WH.addRelationship("Edgar Linton", "Dolores Linton", "Child")
    familyTree_WH.addRelationship("Edgar Linton", "Isabella Linton", "Sibling")
    familyTree_WH.addRelationship("Heathcliff Linton", "Andrew Linton", "Adopted")
    familyTree_WH.addRelationship("Heathcliff Linton", "Dolores Linton", "Adopted")
    
    #Family3 Relations
    familyTree_WH.addRelationship("Hindley Earnshaw", "Frances Byler", "Spouse")
    familyTree_WH.addRelationship("Hareton Earnshaw", "Hindley Earnshaw", "Adopted")
    familyTree_WH.addRelationship("Hareton Earnshaw", "Frances Byler", "Adopted")
    
    #Family4 Relations
    familyTree_WH.addRelationship("Catherine Earnshaw", "Edgar Linton", "Spouse")
    familyTree_WH.addRelationship("Catherine Earnshaw", "Cathy Linton", "Parent")
    familyTree_WH.addRelationship("Edgar Linton", "Cathy Linton", "Parent")
    
    #Family5 Relations
    familyTree_WH.addRelationship("Isabella Linton", "Linton HeathCliff", "Parent")
    
    #Family6 Relations
    familyTree_WH.addRelationship("Heathcliff Linton", "Linton HeathCliff", "Parent")
    
    #Family7 Relations
    familyTree_WH.addRelationship("Hareton Earnshaw", "Cathy Linton", "Spouse")
    
    #Family8 Relations
    familyTree_WH.addRelationship("Linton HeathCliff", "Cathy Linton", "Divorced")

    
    
    
    
    

    familyTree_WH.print()

    programOpen = True                             
    while programOpen:
        print("\n\n Welcome to the Wuther Heights Family Tree Software")
        print("\nChoose the following options:")
        print("1: View the Family Tree")
        print("2: Add a Family Member") 
        print("3: Remove a Family Member")
        print("4: Edit a Family Member")
        print("5: Add a Relationship")
        print("6: Get a Family Member details")
        print("7: Exit")
        choice = int(input("Enter your choice: "))

        

        if choice ==1:
            familyTree_WH.print()
        
        elif choice ==2:
            print('Enter Member Details to Add to the Family Tree')
            newName = input('Name: ')
            newGender = input('Gender (M/F): ')
            newAge = input('Age: ')
            newID = input('ID: ')
            fatherName = input("Enter Father's Name: ")
            motherName = input("Enter Mother's Name: ")
            familyTree_WH.addFamilyMember(newName, newGender, newAge, newID)
            familyTree_WH.addRelationship(newName, fatherName, "Child")
            familyTree_WH.addRelationship(newName, motherName, "Child")
            print("\nMember added with below details: \n")
            print(familyTree_WH.getPerson(newName))
        
        elif choice ==3:
            print('Enter the name of the member to be removed:')
            remName = input('Name: ')
            print("\nMember removed with below details: \n")
            print(familyTree_WH.getPerson(remName))
            familyTree_WH.removeFamilyMember(remName)
        
        elif choice ==4:
            print('Enter the name of the member to be edited:')
            Name = input("\nEnter the name of the person: ")
            print("Current Details: ")
            print(familyTree_WH.getPerson(Name))
            print('Enter the new details:')
            newName = input('New Name: ')
            newGender = input('Gender (M/F): ')
            newAge = input('Age: ')
            familyTree_WH.editFamilyMember(Name, newName, newGender, newAge)
            print("\nMember Updated with below details: \n")
            print(familyTree_WH.getPerson(newName))
        
        elif choice ==5:
            print('Enter Member Details to Add Relationship')
            newName1 = input('Name 1: ')
            newName2 = input('Name 2: ')
            relationship = input('Enter the Relationship (Spouse, Parent, Sibling, Child, Divorced, Adopted): ')
            familyTree_WH.addRelationship(newName1, newName2, relationship)
            print("\nUpdated Details: \n")
            print(familyTree_WH.getPerson(newName1))
        
        elif choice ==6:
            getPerson = input("\nEnter the name of the person you want to find: ")
            print(familyTree_WH.getPerson(getPerson))
        
        elif choice ==7:
            print('\nThank you for using the Wuther Heights Family Tree Software\nGoodbye!\n')
            programOpen = False
        
        else:
            print('Invalid Input')




